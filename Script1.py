import arcpy, numpy
from arcpy.sa import * 
"""
arcpy.CheckOutExtension("Spatial")
afolderpath = r"C:\Khalid\Assignment_06"
aGDB= "Orange_County_GCS.gdb"
nGDB= "Orange_County_PCS.gdb"


arcpy.CreateFileGDB_management(r"C:\Khalid\Assignment_06", "Orange_County_PCS.gdb")

arcpy.env.workspace = afolderpath + "\\" + aGDB
aFC=arcpy.ListFeatureClasses()
aRS=arcpy.ListRasters()
for x in aRS:
    if arcpy.Raster(x).spatialReference.type=='Geographic':
        outfile= afolderpath + "\\" + nGDB + "\\" + x
        arcpy.ProjectRaster_management(x, outfile, 26946, "", 30)

for x in aFC:
    if arcpy.Describe(x).SpatialReference.type=='Geographic':
        outfile= afolderpath + "\\" + nGDB + "\\" + x
        arcpy.Project_management(x, outfile, 26946)


inZoneData = "ZipCodes"
zoneField = "ZIP"
inClassData = "NLCD_2011"
classField = "VALUE"
outTable = r"C:\Khalid\Assignment_06\Orange_County_PCS.gdb\areatable01"
TabulateArea(inZoneData, zoneField, inClassData, classField, outTable)
"""
arcpy.env.workspace= r"C:\Khalid\Assignment_06\Orange_County_PCS.gdb"
anArray= arcpy.da.FeatureClassToNumPyArray('areatable01', "*")

print (anArray["VALUE_41"] + anArray["VALUE_42"] + anArray["VALUE_43"]) / (anArray["VALUE_21"] + anArray["VALUE_22"] + anArray["VALUE_23"] + anArray["VALUE_24"])

"""
aFile= open(r"C:\Khalid\Assignment_06\msg.txt", "w")
with arcpy.da.SearchCursor('areatable01', "*") as cursor:
    for aRow in cursor:
         print "ZIP: {} \t Ratio: {}".format(aRow[1], (aRow[8]+aRow[9]+aRow[10])/(aRow[3]+aRow[4]+aRow[5]+aRow[6]))
         aFile.write("ZIP: {}  Ratio: {}\n".format(aRow[1], (aRow[8]+aRow[9]+aRow[10])/(aRow[3]+aRow[4]+aRow[5]+aRow[6])))
         
aFile.close()
"""
