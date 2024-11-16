import shapefile
import argparse

def process_pointz(input_file, output_file, attribute_name, auto_balance):
    # Open the input shapefile
    reader = shapefile.Reader(input_file)
    shape_type = reader.shapeType

    # Check if the shapefile is of type POINTZ
    if shape_type != 11:
        print(f"ERROR: {input_file} is not a POINTZ shapefile.")
        return
    
    # Prepare the writer for the output file
    writer = shapefile.Writer(output_file)
    writer.shapeType = 11  # Ensure the output is POINTZ

    # Set autoBalance based on input flag
    writer.autoBalance = auto_balance == '1'

    # Copy fields and add the new attribute for Z values
    fields = reader.fields[1:]
    fields.append([attribute_name, 'N', 10, 4])  # New field for Z values
    writer.fields = fields

    # Iterate through the shapefile and write new records
    for record, shape in zip(reader.records(), reader.shapes()):
        z_value = shape.z if shape.z is not None else 0
        writer.record(*record, z_value)
        writer.shape(shape)

    writer.close()
    print(f"Processing complete. Output saved to {output_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process POINTZ shapefiles and append Z values.")
    parser.add_argument("-i", "--input", required=True, help="Input shapefile")
    parser.add_argument("-o", "--output", required=True, help="Output shapefile")
    parser.add_argument("-a", "--attribute", required=True, help="Attribute name for Z values")
    parser.add_argument("-b", "--auto_balance", choices=['0', '1'], default='0', help="Whether to auto-balance fields")
    args = parser.parse_args()

    process_pointz(args.input, args.output, args.attribute, args.auto_balance)
