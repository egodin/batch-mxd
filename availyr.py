# -*- coding: ascii -*-
# availyr.py
# 26/01/2017
# Etienne Godin @etiennegodin egodin5@uwo.ca
#
# USAGE
# This script reads all the layers available in the ArcMap table of content of a give MXD file, checks if the layers are spatially located in the current view, disable those who are not in the current view and enable those in the current view.
#
# 1. Use a copy of the main mxd file that you will be working with. We need to know the full path for the mxd file, such as C:\MAPS\GIS\aworkingmxdfile.mxd
#
# 2. Have all the layers you wish to work with in the table of content in ArcMap. At this stage, it is not important if the layers are checked as visible or not
#
# 3. In ArcMap, using the zoom-in zoom-out hand tool, have the active view filling your workscreen.
#
# 4. Save the mxd file in ArcMap
#
# 5. Know the path for this script file. such as c:\my\script\availyr.py
#
# 6. Open the script file using a text editor - such as vi, notepad++ (not MS-Word) as unexcpected text can be inserted in the code
#
# 7. Set the path for your MXD file used as input for the script - this was saved during step 1 in MXDPATHIN = r"C:\path\to\mxd\fileIN.mxd" - only characters between quotes can be changed.
#
# 8. Set the output MXD file in MXDPATHOUT= r"C:\path\to\mxd\fileOUT.mxd" - this will be the one to work with after the process is complete
#
# 9. In ArcMap, in the dropdown menus: Geoprocessing -> Python
#
# 10. A window will appear, and a prompt will show >>> this is where we will type a command to activate this script
#
# 11. Type execfile(r'c:\a\pathonmyhardisk\availyr.py') after the >>> 
#
# 12. It will do things. When it is done, open the output file referred in Step 8
#
# 13. Only the layers visible in your screen when you ran the script will be selected in the table of content.
# See my email for any questions / comments / feedback


import arcpy

MXDPATHIN = r"C:\archive\postdoc\uwo\DEVON\2017\GIS\Field2017.mxd"
MXDPATHOUT = r"C:\archive\postdoc\uwo\DEVON\2017\GIS\Field2017v2.mxd"

mxd = arcpy.mapping.MapDocument(MXDPATHIN)

df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

layers = arcpy.mapping.ListLayers(mxd, "*", df)

for layer in layers:
    if not df.extent.disjoint(layer.getExtent()):
        print layer.name + " is found to be in the current view extent"
        if layer.supports("VISIBLE"):
            print layer.name + " is supporting the VISIBLE property"
            if layer.visible is False:
                print "This layer was not visible, now set to visible"
                layer.visible = True
            else:
                print "This layer was already set to visible - nothing was changed"
        else:
            print layer.name + " is NOT supporting the VISIBLE property"
    else:
        print layer.name + " is found to be absent from the current view extent."
        if layer.supports("VISIBLE"):
            print layer.name + " is supporting the VISIBLE property"
            if layer.visible is True:
                print "This layer was visible, now set to non-visible"
                layer.visible = False
            else:
                print "This layer was already set to non-visible - nothing was changed"
        else:
            print layer.name + " is NOT supporting the VISIBLE property"

print "Saving " +  MXDPATHOUT
mxd.saveACopy(MXDPATHOUT)
