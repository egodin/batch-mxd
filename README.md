# batch-mxd
Utilities helping automate generic and repetitive processes in ESRI's Arcmap. 

Version 0.1b
Author = Etienne Godin

*********
setmxd.py
*********

Utility to batch update Arcmap *.mxd files (author, thumbnails, tags).

Usage = This program was prepare to bulk update ESRI's Arcmap files (*.mxd)

Current implementation recursively search for mxd files based on a provided root directory and update/delete the values function on what was provided in input:
       
author = arcpy.mapping.MapDocument.author

tags =  arcpy.mapping.MapDocument.tags
thumbnails = arcpy.mapping.MapDocument.deleteThumbnail()
           and arcpy.mapping.MapDocument.makeThumbnail()

Require arcpy to work


**********
availyr.py
**********

Usage = This script reads all the layers available in the ArcMap table of content of a give MXD file, checks if the layers are spatially located in the current view, disable those who are not in the current view and enable those in the current view. This is useful when working with huge datasets and numerous layers - it help keep the environment more functional, by limiting visible layers.

Current implementation require one mxd file, with the view and layers required to work. A copy of this mxd file (IN) will provide the (OUT) with only the visible layers for any given view.

1. Use a copy of the main mxd file that you will be working with. We need to know the full path for the mxd file, such as C:\MAPS\GIS\aworkingmxdfile.mxd

2. Have all the layers you wish to work with in the table of content in ArcMap. At this stage, it is not important if the layers are checked as visible or not

3. In ArcMap, using the zoom-in zoom-out hand tool, have the active view filling your workscreen.

4. Save the mxd file in ArcMap

5. Know the path for this script file. such as c:\my\script\availyr.py

6. Open the script file using a text editor - such as vi, notepad++ (not MS-Word) as unexcpected text can be inserted in the code

7. Set the path for your MXD file used as input for the script - this was saved during step 1 in MXDPATHIN = r"C:\path\to\mxd\fileIN.mxd" - only characters between quotes can be changed.

8. Set the output MXD file in MXDPATHOUT= r"C:\path\to\mxd\fileOUT.mxd" - this will be the one to work with after the process is complete

9. In ArcMap, in the dropdown menus: Geoprocessing -> Python

10. A window will appear, and a prompt will show >>> this is where we will type a command to activate this script

11. Type execfile(r'c:\a\pathonmyhardisk\availyr.py') after the >>> 

12. It will do things. When it is done, open the output file referred in Step 8
