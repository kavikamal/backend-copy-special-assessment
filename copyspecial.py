#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse
import zipfile


"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    result_paths=[]
    for root, dirs, files in os.walk(dir): 
        r = re.compile(r"\w+__\w+\.\w+")
        new_files_list = filter(r.match, files)
        for file in new_files_list:
                p=os.path.join(root,file)
                result_paths.append(os.path.abspath(p))
    return result_paths

def copy_to(paths, dir):
    print 'inside the copy',dir,paths

    if not os.path.exists(dir):
        print 'no dir'
        os.mkdir(dir)
    for path in paths:
        shutil.copy(path, dir)    


def zip_to(paths, zippath):    
    print 'inside the zip'
    with zipfile.ZipFile(zippath, 'w') as myzip:
        for f in paths:   
            myzip.write(f)
def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('from_dir', help='from directory of special files')
    args = parser.parse_args()

    print args
    if not args:
        parser.print_usage()
        sys.exit(1)

    if args.tozip:
        zip_to(get_special_paths('.'),args.tozip)
    elif args.todir:
        copy_to(get_special_paths('.'),args.todir)
    else:
        print get_special_paths('.')    

      

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
  
if __name__ == "__main__":
    main()
