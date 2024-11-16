import shapefile
import argparse
from shapely.geometry import shape

def process_polyline(input_file, output_file, attribute_name, auto_balance):
    # Open the input shapefile
    reader = shapefile.Reader(input_file)
    shape_type = reader.shapeType

    # Check if the shapefile is of type POLYLINE
    if shape_type != 3:
        print(f"ERROR: {input_file} is not a POLYLINE shapefile.")
        return
    
    # Prepare the writer for the output file
    writer = shapefile.Writer(output_file)
    writer.shapeType = 3  # Ensure the output is POLYLINE

    # Set autoBalance based on input flag
    writer.autoBalance = auto_balance == '1'

    # Copy fields and add the new attribute for length
    fields = reader.fields[1:]
    fields.append([attribute_name, 'N', 10, 4])  # New field for length
    writer.fields = fields

    # Iterate through the shapefile and calculate lengths
    for record, shape_obj in zip(reader.records(), reader.shapes()):
        polyline = shape(shape_obj.__geo_interface__)  # Convert shape to Shapely object
        length = polyline.length
        writer.record(*record, length)
        writer.shape(shape_obj)

    writer.close()
    print(f"Processing complete. Output saved to {output_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process POLYLINE shapefiles and calculate lengths.")
    parser.add_argument("-i", "--input", required=True, help="Input shapefile")
    parser.add_argument("-o", "--output", required=True, help="Output shapefile")
    parser.add_argument("-a", "--attribute", required=True, help="Attribute name for length values")
    parser.add_argument("-b", "--auto_balance", choices=['0', '1'], default='0', help="Whether to auto-balance fields")
    args = parser.parse_args()

    process_polyline(args.input, args.output, args.attribute, args.auto_balance)
