import geopandas as gpd
import argparse

def process_geojson(input_file, output_file, attribute_name):
    # Load the GeoJSON file into a GeoDataFrame
    gdf = gpd.read_file(input_file)

    # Assuming you want to add a new column (attribute)
    gdf[attribute_name] = "New Attribute Value"  # Modify as per your needs

    # Save the modified GeoDataFrame back to GeoJSON
    gdf.to_file(output_file, driver='GeoJSON')
    print(f"GeoJSON processing complete. Output saved to {output_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process GeoJSON files and modify attributes.")
    parser.add_argument("-i", "--input", required=True, help="Input GeoJSON file")
    parser.add_argument("-o", "--output", required=True, help="Output GeoJSON file")
    parser.add_argument("-a", "--attribute", required=True, help="Attribute name to add")
    args = parser.parse_args()

    process_geojson(args.input, args.output, args.attribute)
