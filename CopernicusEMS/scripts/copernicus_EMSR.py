#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import zipfile
import shutil
import glob
import shapefile

###############################################################################

folder_input_zip = "/home/geofrizz/Downloads/Copernicus/EMSR190/"
folder_output_zip = "/home/geofrizz/Downloads/Copernicus/EMSR190/temp/"
array_id = ["_01","_02","_03","_04","_05","_06","_07","_08","_09","_10","_11","_12","_13","_14","_15","_16","_17","_18","_19","_20","_21","_22","_23","_28","_29","_30","_31","_32"]
folder_input_shp = folder_output_zip
folder_output_shp = "/home/geofrizz/Downloads/Copernicus/EMSR190/EMSR190_input/"
array_elements = ['settlements_poly_grading', 'hydrography_line_grading', 'physiography_line', 'transportation_line_grading']
folder_input_merge = folder_output_shp
folder_output_merge = "/home/geofrizz/Downloads/Copernicus/EMSR190/EMSR190/"

###############################################################################

def extract_zipped_files (file_name):
    #pass
    print file_name
    file_name_in=folder_input_zip+file_name
    with zipfile.ZipFile(file_name_in, "r") as z:
        z.extractall(folder_output_zip)
    
def clean_folder ():
    #pass
    folder_del = folder_output_zip + "*.*"
    files = sorted(glob.glob(folder_del))
    for f in files:
        os.remove(f)
    for element in array_elements:
        folder_del = folder_output_shp + element + "/*.*"
        files = sorted(glob.glob(folder_del))
        for f in files:
            os.remove(f)
    for element in array_elements:
        folder_del = folder_output_merge + element + "_merged.*"
        files = sorted(glob.glob(folder_del))
        for f in files:
            os.remove(f)
            
            
clean_folder()
#exit()

for file in sorted(os.listdir(folder_input_zip)):
    for id in array_id:
        if id in file:
            if file.endswith(".zip"):
                extract_zipped_files(file)

for file in sorted(os.listdir(folder_input_shp)):
    for element in array_elements:
        if element in file:
            file_move_name_in = folder_input_shp + file
            file_move_name_out = folder_output_shp + element + "/" + file
            shutil.move(file_move_name_in,file_move_name_out)

for category in array_elements:
    folder_input_in = folder_input_merge + category + '/*.shp'
    folder_input_out = folder_output_merge + category + '_merged.shp'
    files = sorted(glob.glob(folder_input_in))
    w = shapefile.Writer()
    for f in files:
        r = shapefile.Reader(f)
        w._shapes.extend(r.shapes())
        w.records.extend(r.records())
        w.fields = list(r.fields)
    w.save(folder_input_out)
    folder_input_in = folder_input_merge + category + '/*.prj'
    folder_input_out = folder_output_merge + category + '_merged.prj'
    files = sorted(glob.glob(folder_input_in))
    for f in files:
        shutil.copy(f,folder_input_out)
        break

print "Finito !"
