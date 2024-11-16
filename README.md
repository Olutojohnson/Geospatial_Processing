# Geospatial Processing Scripts

This project contains various Python scripts designed for geospatial data processing across multiple file formats. These scripts demonstrate how to manipulate geospatial files (such as shapefiles, GeoJSON, KML, etc.), calculate geometries, and modify attributes. The code provided serves as an example for typical geospatial tasks, but the underlying functionality can be extended to handle a wide range of geospatial processing workflows.

## Features

- **POINTZ Processing**: Extracts Z values from POINTZ shapefiles and adds them as attributes to the shapefile.
- **Polyline Processing**: Calculates the length of polylines in shapefiles and appends the results as new attributes.
- **Polygon Processing**: Computes the area and perimeter of polygons and appends the results to the shapefile's attribute table.
- **GeoJSON Processing**: Modifies attributes and geometry in GeoJSON files, with the flexibility to add or change data.
- **KML Processing**: Handles KML files, adding or modifying attributes and coordinates.

## Extending Functionality

The functionality provided in these scripts is not limited to the examples shown. The code is modular and flexible, and can be adapted for other geospatial processing tasks, such as:

- **Coordinate transformations** (e.g., reprojecting shapefiles from one spatial reference system to another)
- **Spatial analysis** (e.g., buffering, clipping, intersection, union)
- **Geospatial visualization** (e.g., creating maps or plotting geometries with custom styling)
- **Complex attribute manipulation** (e.g., conditional field updates, calculations based on existing attributes)

The provided scripts serve as a foundation for these and many other geospatial processing tasks. You can modify them to fit your needs, add new functions, or integrate with other libraries and tools to expand the scope of operations.

## Installation

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```
##  Usage

Each script can be run from the command line with the following syntax:

```bash
python <script_name.py> -i <input_file> -o <output_file> -a <attribute_name> -b <auto_balance (0 or 1)>
```

For example, to process a POINTZ shapefile and append the Z values as an attribute:

```bash
python pointz_processing.py -i input.shp -o output.shp -a Depth -b 1
```

## Scripts

- **pointz_processing.py**: Add Z values from POINTZ shapefiles to a specified attribute.
- **polyline_processing.py**: Calculate the length of lines in polyline shapefiles.
- **polygon_processing.py**: Calculate the area and perimeter of polygons.
- **geojson_processing.py**: Modify attributes and geometry in GeoJSON files.
- **kml_processing.py**: Modify KML files, including attributes and coordinates.

## Example Use Cases

- **Extracting Elevation from Point Clouds**: Use the pointz_processing.py script to extract elevation (Z value) from a POINTZ shapefile and store it in a custom attribute like "Elevation".
- **Calculating Polyline Lengths**: Use the polyline_processing.py script to calculate the length of roads or other linear features from a polyline shapefile, and append this value to an attribute.
- **Analyzing Land Area**: The polygon_processing.py script allows you to calculate areas and perimeters of land parcels or other polygon-based features.
- **Modifying GeoJSON Data**: With geojson_processing.py, you can update attributes or geometry in a GeoJSON file for use in web mapping applications or further geospatial analysis.
- **Handling KML Files**: The kml_processing.py script allows you to modify KML files for use in Google Earth or other KML-compatible software.

## Customizing the Code

The provided scripts are designed to be easily customized to fit specific use cases. You can modify them by:

-Changing the types of calculations performed (e.g., calculating distances, areas, or other geometric properties).
-Adding new fields and attributes based on different geometric or spatial data.
-Integrating with other libraries for advanced geospatial analysis, like **GDAL**, **Pyproj**, or **Shapely**.
-Adding support for other file formats like **PostGIS**, **MapInfo**, **DXF**, or **GPX**.

Feel free to fork this repository, extend the functionality, and build on the examples to suit your specific needs.
