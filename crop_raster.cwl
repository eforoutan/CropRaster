cwlVersion: v1.2
class: CommandLineTool
 
hints:
  DockerRequirement:
    dockerPull: "eforoutan/crop_raster:latest"
  NetworkAccess:
    networkAccess: true
 
inputs:
  
  input_raster:
    type: File
    inputBinding:
      position: 1
  
  input_shapefile:
    type:
      - File
      - Directory
    inputBinding:
      position: 2
 
outputs:
  cropped_raster_output:
    type: File
    outputBinding:
      glob: "cropped_raster.tif"
 