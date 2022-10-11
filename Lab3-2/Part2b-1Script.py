# coding: utf-8
print("HelloWorld")
# HelloWorld
import arcpy
arcpy.env.workspace = "C:\\Users\\Frank\\Documents\\UCM\\ENGR180\\Lab3-1\\Lab3-1\\Lab3-1.gdb"
in_features = "CARiversAndCreeksPRJ"
clip_features = "MariposaCountyBoundary"
out_feature_class = "MarCoRiversAndCreeks_PY"
arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
# <Result 'C:\\Users\\Frank\\Documents\\UCM\\ENGR180\\Lab3-1\\Lab3-1\\Lab3-1.gdb\\MarCoRiversAndCreeks_PY'>

import arcpy 
arcpy.env.workspace = "C:\\Users\\Frank\\Documents\\UCM\\ENGR180\\Lab3-1\\Lab3-1\\Lab3-1.gdb" 
string = "Hello World"
