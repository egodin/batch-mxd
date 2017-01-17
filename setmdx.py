# Program Name = setmdx.py
# Version 0.1a
# Date = 17/01/2017
# Author = Etienne Godin
# Usage = This program was prepare to bulk update ESRI's Arcmap files (*.mxd)
#   Current implementation recursively search for mxd files based on a provided root directory
#   and update/delete the values function on what was provided in input:
#       author = arcpy.mapping.MapDocument.author
#       tags =  arcpy.mapping.MapDocument.tags
#       thumbnails = arcpy.mapping.MapDocument.deleteThumbnail()
#           and arcpy.mapping.MapDocument.makeThumbnail()
# Require arcpy to work
#
# Import modules
import arcpy, os

# Set working path.
# This is the root directory where the search for ArcGIS *.mxd file would start.
# This search is recursive.
path = r"C:\your\path\here"

# Set default author name.
# Possible values for chgAuthor is True or False
# If chgAuthor is set to True, a valid string must be assigned to author
# author can be empty to delete existing values (author = "")
chgAuthor = False
author = "Your Name"

# Set default tag. Tags can be separated by a comma if there is more than one.
# Possible values for chgTags is True or False
# If chgTags = True, a valid string must be assigned to tags
# tags can be empty to delete existing values (tags = "")
chgTags = False
tags = "project,map,projection"

# Thumbnails maintenance. The following values are allowed for refThumbs:
# 0 do nothing
# 1 generate thumb for each mxd files
# 2 delete thumb for each mxd file
# 3 update thumb for each mxd file (delete then generate)
refThumbs = 0

extension = "*.mxd"

cmptmdx = 0

os.chdir(path)

for root, dirs, files in os.walk(path):
    workspace = arcpy.env.workspace = root
    mxdList = arcpy.ListFiles(extension)

    for mxdDocument in mxdList:
        filePath = os.path.join(workspace, mxdDocument)
        mxd = arcpy.mapping.MapDocument(filePath)

        if chgAuthor is True:
            mxd.author = author

        if chgTags is True:
            mxd.tags = tags

        if refThumbs == 1:
            mxd.makeThumbnail()

        elif refThumbs == 2:
            mxd.deleteThumbnail()

        elif refThumbs == 3:
            mxd.deleteThumbnail()
            mxd.makeThumbnail()

        cmptmdx += 1
        mxd.save()
        del mxd

print "Report:"

if chgAuthor is True:
    print "The author field was updated for " + str(cmptmdx) + " file(s) "

if chgTags is True:
    print "The tag field was updated for " + str(cmptmdx) + " file(s) "

if refThumbs == 1:
    print "The thumb was generated for " + str(cmptmdx) + " file(s) "

if refThumbs == 2:
    print "The thumb was deleted for " + str(cmptmdx) + " file(s) "

if refThumbs == 3:
    print "The thumb was updated for " + str(cmptmdx) + " file(s) "
