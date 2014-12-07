import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_6/data/Exercise09"
fcpath = "F:/UWTacoma/GIS_501_AU_2014/lab_6/data/Exercise09/Results/"
arcpy.env.overwriteOutput = True

if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    raster = arcpy.sa.Raster("elevation")
    slope = arcpy.sa.Slope(raster, "PERCENT_RISE")
    slope.save(fcpath + "slope")
    aspect = arcpy.sa.Aspect(raster)
    aspect.save(fcpath + "aspect")
    myremap = RemapValue([[41,1], [42,2], [43,3]])
    outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")
    outreclass.save(fcpath + "forested")

else:
    print "Spatial Analyst license is not available."
        
slope1 = slope < 20
slope2 = slope > 5
goodslope = slope1 & slope2
goodslope.save(fcpath + "goodslope")

aspect1 = aspect < 270
aspect2 = aspect > 150
southasp = aspect1 & aspect2
southasp.save(fcpath + "southasp")

arcpy.CheckInExtension("spatial")
