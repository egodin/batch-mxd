# batch-mxd
Utility to batch update Arcmap *.mxd files (author, thumbnails, tags).

Version 0.1a
Author = Etienne Godin

Usage = This program was prepare to bulk update ESRI's Arcmap files (*.mxd)
   Current implementation recursively search for mxd files based on a provided root directory
   and update/delete the values function on what was provided in input:
       author = arcpy.mapping.MapDocument.author
       tags =  arcpy.mapping.MapDocument.tags
       thumbnails = arcpy.mapping.MapDocument.deleteThumbnail()
           and arcpy.mapping.MapDocument.makeThumbnail()
 Require arcpy to work
