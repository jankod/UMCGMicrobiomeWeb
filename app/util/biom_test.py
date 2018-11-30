import numpy.core._methods
import numpy.lib.format
import numpy as np

# https://github.com/biocore/biom-format
# http://biom-format.org/documentation/quick_usage_examples.html#examples

from biom import  parse_table

# FIRST pip install biom-format

def ajde():
    with open('C:/Data/PBF/Projekti/2018-UMCGMicrobiomeWeb/example_data/example1_metaphlan.txt') as f:
        table = parse_table(f)
        print(table)


## ajde()