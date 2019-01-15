from typing import List, Any

import numpy.core._methods
import numpy.lib.format
import numpy as np

# https://github.com/biocore/biom-format
# http://biom-format.org/documentation/quick_usage_examples.html#examples

from biom import parse_table

# FIRST pip install biom-format
from scipy._lib.decorator import __init__

from app.util.file_parser import TaxonomyParser


def parse_biom_format(path):
    with open(path) as f:
        table = parse_table(f)
        print("version ", table.format_version)
        #   print(" "+ table.)

        # print(table)
        return table





path_tax = 'C:/Data/PBF/Projekti/2018-UMCGMicrobiomeWeb/example_data/example1_metaphlan.txt'
path_tax_marged = 'C:/Data/PBF/Projekti/2018-UMCGMicrobiomeWeb/example_data/example_metaphlan_merged.tsv'

path_pathway = 'C:/Data/PBF/Projekti/2018-UMCGMicrobiomeWeb/example_data/example1_pathabundance.tsv'
path_pathway_marged = 'C:/Data/PBF/Projekti/2018-UMCGMicrobiomeWeb/example_data/example_pathways_humann2_merged.tsv'


def custom_analyse():
    parser = TaxonomyParser(path_tax)
    sample = parser.parse()

    print(sample)


def biom_analise():
    # parser = TaxonomyParser(path_tax)
    # sample = parser.parse()
    # print(sample)
    t = parse_biom_format(path_tax)
    # Normalizirano
    normed = t.norm(axis='sample', inplace=False)
    # print(t.ids())  # ['Metaphlan2_Analysis']
    # print(t.type)  # None
    # print(t.ids(axis='observation')) # array  ['k__Bacteria' 'k__Bacteria|p__Bacteroidetes'....

    d = t.data('Metaphlan2_Analysis')

    print(t.matrix_data)


custom_analyse()
