FROM python:3.9-slim

# Install necessary system packages and Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends libexpat1 && \
    pip install geopandas rasterio && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY crop_raster.py /app/crop_raster.py

# Set the ENTRYPOINT to the Python script
ENTRYPOINT ["python", "/app/crop_raster.py"]
