import logging
from time import sleep
from typing import List

from django.core.files.uploadedfile import InMemoryUploadedFile

log = logging.getLogger("app")

FILE_TYPE_TAXONOMY = 'taxonomy'
FILE_TYPE_TAXONOMY_MERGED = 'taxonomy_merged'
FILE_TYPE_PATHWAY = 'pathway'
FILE_TYPE_PATHWAY_MERGED = 'pathway_merged'

TaxonomyList = List[str]


class TaxonomyAbundance:

    def __init__(self, abundance: float = 0, taxes: TaxonomyList = []):
        self.abundance = abundance
        self.taxes = taxes

    def __str__(self):
        return f"{self.abundance} {self.taxes}"


TaxonomyAbundanceList = List[TaxonomyAbundance]


class TaxonomyParserResult:

    def __init__(self, sample_name: str = "", taxonomy_abundance: TaxonomyAbundanceList = []):
        self.sample_name = sample_name
        self.taxonomy_abundance = taxonomy_abundance


class TaxonomyParser:

    def __init__(self, file_content: str):
        self.file_content = file_content

    def parse(self) -> TaxonomyParserResult:
        result = TaxonomyParserResult()

        for l in self.file_content.splitlines():

            if l.startswith("#SampleID"):
                sp = l.split('\t')
                result.sample_name = sp[1].strip()
                continue

            if l.startswith("#"):
                continue

            if l.startswith("k__Bacteria"):
                taxonomy = self.parse_tax_line(l)
                result.taxonomy_abundance.append(taxonomy)

        return result

    @staticmethod
    def parse_tax_line(line: str) -> TaxonomyAbundance:
        """
        Parse eg: k__Bacteria|p__Actinobacteria	0.84814
        :param line:
        :return: TaxonomyAbundance
        """
        taxonomy = TaxonomyAbundance()
        split = line.split("\t")
        taxonomy.abundance = float(split[1])
        tax_line = split[0]

        if "|" in tax_line:
            taxes = tax_line.split("|")
            taxonomy.taxes.extend(taxes)
        else:
            taxonomy.taxes.append(tax_line)

        return taxonomy


# threadPoll = ThreadPoolExecutor(max_workers=4)
FileList = List[InMemoryUploadedFile]

# TODO krivo, samo jedan file se parsa!!!
def parse_taxonomy_files(files: FileList) -> TaxonomyParserResult:
    for f in files:
        tax_parser = TaxonomyParser(f.read().decode("UTF-8"))
        tax_result = tax_parser.parse()
        return tax_result


def run_parse_in_background(file_type, files):
    # threadPoll.submit(task)
    pass


def task():
    for i in range(10):
        print("poll parse ", i, " ")
        sleep(2)
