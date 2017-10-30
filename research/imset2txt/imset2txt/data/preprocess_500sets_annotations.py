'''
    Select the image sets from Parks dataset (3500 sets) that
    were annotated by Hive's internal team, and save them with
    new folder names as 1, 2, 3...
    Create a json file that has mapping of folder names (1, 2..)
    with real names and tags("Parks").
'''

import json
import csv
from collections import OrderedDict
import shutil

inputDir = "/local-scratch2/ajakash/aabdujyo/2017_set_compression/Data/"
outputDir = "/local-scratch2/ajakash/aabdujyo/2017_set_compression/models/" \
            "research/imset2txt/imset2txt/data/500/"
annotationFile = inputDir + "annotations_hive/annotations_set1_541.csv"

mapping = OrderedDict()

with open(annotationFile, 'rb') as ann:
    annData = csv.reader(ann)
    count = 0
    count_real = 0
    for row in annData:
        if row[0].encode('utf-8') == "filepath":
            continue
        print row

        if row[2].encode('utf-8') == "NO_TEXT":
            count = count + 1
        elif len(row[0].encode('utf-8')) > 1:
            count_real = count_real + 1

            # Enter all details in captions.json
            # FOR WRONGLY ENCODED ', THIS REQUIRES ' ENTERED FROM VIM
            mapping[str(count_real)] = {"caption": row[2].encode('utf-8'),
                                        "tag" : "Parks",
                                        "location" : row[1].encode('utf-8')}

            # Copy the folder with image set and save with name
            # as a folder number (1, 2, ...)
            # FOR WRONGLY ENCODED ', THIS REQUIRES ' ENTERED FROM LIBRE CALC
            #shutil.copytree(inputDir + "Parks_3500/" + row[1],
            #                outputDir + str(count_real))

print mapping
print count, count_real

with open('500.json', 'w') as f:
    json.dump(mapping, f)