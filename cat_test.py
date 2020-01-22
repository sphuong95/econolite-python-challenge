"""
    Title: Econolite Python Programming Exercise 1

    Task: Write a Python 3 program that takes 2 arguments:

    The first argument is the path to a directory that contains INI files describing features of different breeds of cats,
    where each INI files contains one section that is the name of the breed, and that section contains key-value pairs,
    where each key is the name of a feature of that breed, and the value description of that feature.

    The second argument is the name of one of these features.

    The program must print the description of the given feature for each breed, in the format of "<Breed Name>: <Feature Description>".

    By: Shaquile Phuong
    Date: 01/08/2020


    Planning:
        1: Figure out how to accept arguments needed (check)
        2: Read all the INI files in a directory (check)
        3: Find a way to organize the files in a list (check)
        4: Match key pairs with arguments and print it out! (check)
        5. Handle bad input? How to solve invalid INI files?

"""

import argparse, os, glob
import configparser

#Checks if the path is valid
def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

#require the two arguments needed to pass
arg_parser = argparse.ArgumentParser(description = 'Listing different cat breed features...')
#First argument needs to be a path to a directory
arg_parser.add_argument('path', type=dir_path, help='This is the path to the directory containing INI files. It should be formatted relative to where the program is located')

#Second Argument needs to take in one of the following choices
#choices=['color', 'hairLength', 'origin', 'fluffiness']
arg_parser.add_argument('option', choices=['color', 'hairLength', 'origin', 'fluffiness'], help='Please choose one of the following descriptions about cat breeds: [color], [hairLength], [origin], [fluffiness]')
args = arg_parser.parse_args()

arg_path = args.path #directory 
arg_dsc = args.option #cat breed description

#os.chdir() changes the current working directory to the given path
os.chdir(arg_path)
cfg_parser = configparser.ConfigParser()
#This line will make is inputted into the argument as is. Corrected fix that made all arguments lowercase
cfg_parser.optionxform = str

#loop through the current directory and read all INI files
'''
for file in glob.glob('*.ini'):
    cfg_parser.read(file)
'''
for file in glob.glob('*.ini'):
    try:
        cfg_parser.read(file)
    except configparser.Error as err:
        print('Could not parse the following file:', err)

#created a dictionary with all cat breeds and their descriptions
cat_dictionary = {}
for section in cfg_parser.sections():
    cat_dictionary[section] = {}
    for key in cfg_parser.options(section):
        cat_dictionary[section][key] = cfg_parser.get(section, key)

#print(cat_dictionary)
#print(cat_dictionary['Russian Blue']['hairLength'])

#loop through the dictionary with the description argument that was passed
#and print out the correct values
for section in cat_dictionary:
    for key in cat_dictionary[section]:
        if key == arg_dsc:
            print(section + ': ' + cat_dictionary[section][key])
