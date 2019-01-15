import numpy.core._methods
import numpy.lib.format
import numpy as np
from io import StringIO

# https://github.com/biocore/biom-format
# http://biom-format.org/documentation/quick_usage_examples.html#examples

from biom import parse_table, Table

dir = "C:/Projekti/PycharmProjects/UMCGMicrobiomeWeb/example_data"
path_tax = dir + '/example1_metaphlan.txt'
path_tax_marged = dir + 'example_metaphlan_merged.tsv'

with open(path_tax) as f:
    table = parse_table(f)
    print("version ", table.format_version)
    print("id ", table.table_id)
    print("dtype ", table.dtype)
    print("type ", table.type)
    print("version ", table.format_version)
    print("generated_by ", table.generated_by)
    print("table_id ", table.table_id)
    print("ids ", table.ids())  # ['Metaphlan2_Analysis']
    # print("ids ", table.to_json())

    # with open('c:/tmp/metha.json', 'w') as file:
    #     file.write(table.to_json("janko"))

    table = table.norm(axis='sample', inplace=False)

    for id in table.ids():
        print("id ", id)
        # d = table.data(id, axis='sample')
        for p in table.iter_data(axis='sample'):
            print(p)
