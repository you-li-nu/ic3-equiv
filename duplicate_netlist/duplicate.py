#!/usr/bin/python3
import sys
import os
from optparse import OptionParser



def main():
    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            filepath=subdir+os.sep+file
            
            if filepath.endswith(".aig") and not filepath.endswith("syn.aig") and not filepath.endswith("stu.aig"):
                print (filepath)

    

if __name__ == '__main__':
    main()
