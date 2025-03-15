import sys
import json
import os
import geopandas as gpd
import rasterio
from rasterio.mask import mask

def crop_raster(input_raster, input_shapefile):
    try:
        # Read the shapefile
        gdf = gpd.read_file(input_shapefile)

        # Read the raster file
        with rasterio.open(input_raster) as src:
            # Crop the raster with the shapefile geometry
            out_image, out_transform = mask(src, gdf.geometry, crop=True)

            # Update metadata for the output raster
            out_meta = src.meta.copy()
            out_meta.update({
                "driver": "GTiff",
                "height": out_image.shape[1],
                "width": out_image.shape[2],
                "transform": out_transform
            })

            # Construct output file name in the current directory
            output_raster = os.path.join(os.getcwd(), "cropped_raster.tif")

            # Write the Cropped raster to a new file
            with rasterio.open(output_raster, "w", **out_meta) as dest:
                dest.write(out_image)

        return output_raster  # Return the path to the output raster

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Indicate failure

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python crop_raster.py <input_raster> <input_shapefile>")
        sys.exit(1)

    input_raster = sys.argv[1]
    input_shapefile = sys.argv[2]

    output_file = crop_raster(input_raster, input_shapefile)

    if output_file:
        print(f"Raster successfully cropped and saved as {output_file}.")
    else:
        print(json.dumps({"error": "Cropping failed"}))
