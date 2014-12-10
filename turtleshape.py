import arcpy, turtle
from arcpy import env
                          
turtle.speed()                                   		                
raphael = turtle.Turtle()
raphael.color('red')

arcpy.env.overwriteOutput = True 
path = "F:/UWTacoma/GIS_501_AU_2014/lab_4/"
fc = "turtles.shp"		
spatialref = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.management.CreateFeatureclass(path, fc, "POLYGON", "", "", "", spatialref)


cursIns = arcpy.da.InsertCursor(path + fc, ["SHAPE@"])

#Create an empty array  and point object to create features
point = arcpy.Point()
array = arcpy.Array()		

print ("This program draws shapes depending on the numbers you enter.")
num_sides = int(raw_input("Enter the number of sides for an equilateral polygon the turtle will draw: "))


angle = int(360/num_sides)

for num_side in range (num_sides):
    raphael.forward(125)
    raphael.left(angle)
    point.X, point.Y=raphael.position()
    array.add(point)

    polygon = arcpy.Polygon(array)
    cursIns.insertRow([polygon])
    
del cursIns

print "all done"
