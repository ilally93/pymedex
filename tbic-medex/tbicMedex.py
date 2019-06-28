'''
Created on Jun 26, 2019

@author: ilall

sys.argv[0] = tbicMedex.py
sys.argv[1] = path to medexHome
sys.argv[2] = input folder
sys.argv[3] = output folder

python3 tbicMedex.py arg1 arg2 arg3
'''
from medex.medex import MedEx
from medex.medex import build_medex_obj
from medex.utils import sys_url
import os
import sys

input_folder = os.path.join(os.getcwd(), sys.argv[2])
output_folder = os.path.join(os.getcwd(), sys.argv[3])

def tbicMedex():
# Create a medex object with a path to the location of the MedEx installation.
    medexHome= sys.argv[1]
    m = MedEx(sys_url(medexHome))

# Run the application with an absolute URL to the input directory and output directory.
# Note that 'sys_url' is not necessary, it simply expands the user symbols and formats
# the URL to the system preferred.
    m.parse(sys_url(input_folder), sys_url(output_folder))

##   parsed = build_medex_obj(sys_url(output_folder, "data_medications_001.txt"))
#    parsed = build_medex_obj(os.path.join("output/data_medications_001.txt"))

##    for line in parsed:
##       print(line)
    
def main():
    tbicMedex()
    
main()
    