from typing import List, Any

import numpy.core._methods
import numpy.lib.format
import numpy as np

# https://github.com/biocore/biom-format
# http://biom-format.org/documentation/quick_usage_examples.html#examples

from biom import parse_table

# FIRST pip install biom-format
from scipy._lib.decorator import __init__


def parse_biom_format(path):
    with open(path) as f:
        table = parse_table(f)
        print("version ", table.format_version)
        #   print(" "+ table.)

        # print(table)
        return table


class SampleTaxonomy:
    taxes: List[str]

    def __init__(self, name=""):
        self.name = name
        self.abundance = 0
        self.taxes = []

    def __str__(self):
        return self.name


class TaxonomyParser:
    def __init__(self, file_path):

        self.path = file_path
        self.sampleTaxonomy = SampleTaxonomy()

    def parse(self) -> SampleTaxonomy:

        with open(self.path) as fp:
            lines = fp.readlines()
            for l in lines:
                if l.startswith("#SampleID"):
                    sp = l.split('\t')
                    self.sampleTaxonomy.name = sp[1].strip()
                    continue
                if l.startswith("k__Bacteria"):
                    self.parse_tax_line(l)

        return self.sampleTaxonomy

    def parse_tax_line(self, l):
        split = l.split("\t")
        abundance = float(split[1])
        tax_line = split[0]

        if "|" in tax_line:
            taxes = tax_line.split("|")
            self.sampleTaxonomy.abundance = abundance
            self.sampleTaxonomy.taxes.extend(taxes)
        else:
            self.sampleTaxonomy.taxes.append(tax_line)


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
