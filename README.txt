OVERVIEW --->
This script was made by Roman Zaytsev expressly for GridCure as part of their
coding challenge for the Data Engineer (Python) position.

ASSUMPTIONS MADE --->
1. Input files are both ordered by item_id in descending order
2. Every item_id is in both input files
3. There are always 2 input files, with names configured below
4. Date field is formatted in one of two formats: '%m/%d/%Y' or '%Y-%m-%dT%H:%M:%S'

CONFIGURE --->
CONFIGURATION global variables below are to configure input names, output names, etc.

RUN --->
A Python 3.6 virtual env is included in this project. To run this script, simply
run `./bin/python script.py` from the base directory!

OUTPUT --->
Output will be generated in the configured directory; a sample output file was
created ./output/output.csv after running this program once.