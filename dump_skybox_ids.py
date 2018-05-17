import string
from module_info import *
from process_common import *
from module_skyboxes import *

def save_python_header():
  file = open("./ID_skyboxes.txt","w")
  for i_item in xrange(len(skyboxes)):
    file.write("sky_%s = %d\n"%(convert_to_identifier(skyboxes[i_item][0]),i_item))
  file.close()

def save_skyboxes():
  file = open(export_dir + "/data/skyboxes.txt","w")
  file.write("%d\n"%len(skyboxes))
  for skybox in  skyboxes:
    file.write("%s %d %f %f %f %s\n"%(skybox[0],skybox[1],skybox[2],skybox[3],skybox[4],skybox[5]))
    file.write(" %f %f %f "%skybox[6])
    file.write(" %f %f %f "%skybox[7])
    file.write(" %f %f %f "%skybox[8])
    file.write(" %f %d\n"%skybox[9])
  file.close()

print "Exporting skyboxes..."
save_python_header()
save_skyboxes()