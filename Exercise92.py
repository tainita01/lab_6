try:
    import arcpy
    env = arcpy.env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_6/data/Exercise09/"
    arcpy.env.overwriteOutput = True
    arcpy.management.CreateFileGDB(env + "Results/", "New.gdb")


##Convert Multiple Raster Dataset to FGDB
    arcpy.RasterToGeodatabase_conversion("landcover.tif",env + "Results/New.gdb")


except:
    print "Raster To Geodatabase example failed."
    print arcpy.GetMessages()
