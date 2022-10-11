# coding: utf-8
import arcpy

arcpy.env.workspace ="C:\\Users\\Frank\\Documents\\UCM\\ENGR180\\Lab3-1\\Lab3-1\\Lab3-1.gdb"
in_raster= "DiffNBR_ModBuild"

reclass_field = "VALUE"

remap = RemapRange([[-0.727323,-0.500000, 1], 
                    [-0.500000, -0.250000, 2], 
                    [-0.25, -0.1, 3], 
                    [-0.1, 0, 4], 
                    [0, 0.1, 5], 
                    [0.1, 0.25, 6], 
                    [0.25, 0.5, 7], 
                    [0.5, 0.89, 8]])

reclass_NBR= arcpy.sa.Reclassify(in_raster, reclass_field, remap, 'NODATA')
