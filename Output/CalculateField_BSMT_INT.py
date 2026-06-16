# Code was used from here: http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/calculate-field.htm
# Modified by: Michael Warren
# Description: Use CalculateField with a codeblock to calculate values


# Import system modules
# Not sure if all are needed, but may help in debugging...
import sys, os, arcpy, traceback
 
# Set environment settings
# Change as necessary
# arcpy.env.workspace = "C:/Users/mwarr012/Desktop/Geostats/Geostats.gdb"
arcpy.env.workspace = "C:/Users/mwarr012/Desktop/Geostats/Geostats.gdb"
 
# Set local variables
# Make sure to change/modify and define the data type of field of "BSMT", in this case
# We are defining the field as a string, "str" for BSMT.
inTable = "FFE_Final"
fieldName = "BSMT_INT"
expression = "getClass(str(!BSMT!))"
codeblock = """def getClass(BSMT):
    if BSMT == "Pier":
    	return 1
    if BSMT == "Crawl Space":
        return 2
    if BSMT == "Concrete Slab":
    	return 3
    if BSMT == "Basement":
        return 4
    else:
        return 0"""
 # Execute AddField
try:
    arcpy.AddField_management(inTable, fieldName, "SHORT")

# Execute CalculateField 
    arcpy.CalculateField_management(inTable, fieldName, expression, "PYTHON_9.3", 
                                codeblock)

    print ("Calculated String of Field 'BSMT' to integer in field 'BSMT_INT'")
except Exception:
    e = sys.exc_info()[1]
    print(e.args[0])
