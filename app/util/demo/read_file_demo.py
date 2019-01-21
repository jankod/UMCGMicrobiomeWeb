import datetime
from pprint import pprint
from time import time

from django.core.files.uploadedfile import InMemoryUploadedFile

from app.models import TaxonomyAbundance, Sample, TaxonomyIdAbundance
from app.util import file_parser
from app.util.file_parser import parse_taxonomy_file, TaxonomyParser, TaxonomyMergedParser, \
    TaxonomyAbundanceParserResult, TaxonomyParserResult


def demo2():
    path = 'C:/Data/PBF/Projekti/2018-UMCGMicrobiomeWeb/example_data/example_metaphlan_merged.tsv'

    with open(path) as fp:
        lines = fp.read()
        tax_parser = TaxonomyMergedParser(lines)
        tax_result = tax_parser.parse()
        sample = Sample.objects.first()

        tax_id_abundance_list = []
        count_result = 0
        r: TaxonomyParserResult
        for r in tax_result:
            count_result += 1
            print(f" radim {count_result} od {len(tax_result)}  {datetime.datetime.now().time()}")

            tax: TaxonomyAbundanceParserResult
            for tax in r.taxonomy_abundances:
                if tax.abundance <= 0:
                    continue
                model: TaxonomyAbundance = tax.to_model()
                tax_id_abundance = model.to_int_model()
                # pprint(tax_id_abundance)
                tax_id_abundance.sample = sample
                tax_id_abundance_list.append(tax_id_abundance)

                if len(tax_id_abundance_list) > 10_000:
                    print(f"spremam  10 000")
                    TaxonomyIdAbundance.objects.bulk_create(tax_id_abundance_list)
                    tax_id_abundance_list.clear()

            TaxonomyIdAbundance.objects.bulk_create(tax_id_abundance_list)
            tax_id_abundance_list.clear()


def demo1():
    path = 'C:/Data/PBF/Projekti/2018-UMCGMicrobiomeWeb/example_data/example_metaphlan_merged.tsv'

    with open(path) as fp:
        lines = fp.read()
        print("start ", time())
        # tax_parser = TaxonomyParser(lines)
        tax_parser = TaxonomyMergedParser(lines)
        tax_result = tax_parser.parse()

        print(f"finish {time()} dobio {tax_result.__sizeof__()} {len(tax_result)}")
