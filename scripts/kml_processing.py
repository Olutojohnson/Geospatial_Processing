from pykml import parser
import xml.etree.ElementTree as ET
import argparse

def process_kml(input_file, output_file, attribute_name):
    # Parse the KML file
    with open(input_file, 'r') as f:
        root = parser.parse(f).getroot()

    # Add a new attribute or modify existing data
    for elem in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
        new_data = ET.SubElement(elem, 'ExtendedData')
        data = ET.SubElement(new_data, 'Data', name=attribute_name)
        data.text = "New Data"

    # Write the modified KML to a new file
    with open(output_file, 'wb') as f:
        f.write(ET.tostring(root))

    print(f"KML processing complete. Output saved to {output_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process KML files and modify attributes.")
    parser.add_argument("-i", "--input", required=True, help="Input KML file")
    parser.add_argument("-o", "--output", required=True, help="Output KML file")
    parser.add_argument("-a", "--attribute", required=True, help="Attribute name to add")
    args = parser.parse_args()

    process_kml(args.input, args.output, args.attribute)
