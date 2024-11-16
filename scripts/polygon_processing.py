import shapefile
import argparse
from shapely.geometry import shape

def process_polygon(input_file, output_file, area_attribute, perimeter_attribute, auto_balance):
    # Open the input shapefile
    reader = shapefile.Reader(input_file)
    shape_type = reader.shapeType

    # Check if the shapefile is of type POLYGON
    if shape_type != 5:
        print(f"ERROR: {input_file} is not a POLYGON shapefile.")
        return
    
    # Prepare the writer for the output file
    writer = shapefile.Writer(output_file)
    writer.shapeType = 5  # Ensure the output is POLYGON

    # Set autoBalance based on input flag
    writer.autoBalance = auto_balance == '1'

    # Copy fields and add new attributes for area and perimeter
    fields = reader.fields[1:]
    fields.append([area_attribute, 'N', 10, 4])
    fields.append([perimeter_attribute, 'N', 10, 4])
    writer.fields = fields

    # Iterate through the shapefile and calculate area and perimeter
    for record, shape_obj in zip(reader.records(), reader.shapes()):
        polygon = shape(shape_obj.__geo_interface__)  # Convert shape to Shapely object
        area = polygon.area
        perimeter = polygon.length
        writer.record(*record, area, perimeter)
        writer.shape(shape_obj)

    writer.close()
    print(f"Processing complete. Output saved to {output_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process POLYGON shapefiles and calculate area and perimeter.")
    parser.add_argument("-i", "--input", required=True, help="Input shapefile")
    parser.add_argument("-o", "--output", required=True, help="Output shapefile")
    parser.add_argument("-a", "--area_attribute", required=True, help="Attribute name for area values")
    parser.add_argument("-p", "--perimeter_attribute", required=True, help="Attribute name for perimeter values")
    parser.add_argument("-b", "--auto_balance", choices=['0', '1'], default='0', help="Whether to auto-balance fields")
    args = parser.parse_args()

    process_polygon(args.input, args.output, args.area_attribute, args.perimeter_attribute, args.auto_balance)
