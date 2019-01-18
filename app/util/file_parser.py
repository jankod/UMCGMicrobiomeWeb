import logging
from time import sleep
from typing import List

from django.core.files.uploadedfile import InMemoryUploadedFile

from app.models import TaxonomyAbundance

log = logging.getLogger("app")

FILE_TYPE_TAXONOMY = 'taxonomy'
FILE_TYPE_TAXONOMY_MERGED = 'taxonomy_merged'
FILE_TYPE_PATHWAY = 'pathway'
FILE_TYPE_PATHWAY_MERGED = 'pathway_merged'

TaxonomyList = List[str]


class TaxonomyAbundanceParserResult:

    def __init__(self):
        self.abundance = -1
        self.taxes = []

    def to_model(self) -> TaxonomyAbundance:
        ta = TaxonomyAbundance()
        ta.abundance = self.abundance
        for t in self.taxes:
            if t.startswith("k__"):
                ta.rank1_kingdom = t[3:]
                continue
            if t.startswith("p__"):
                ta.rank2_phylum = t[3:]
                continue
            if t.startswith("c__"):
                ta.rank3_class = t[3:]
                continue
            if t.startswith("o__"):
                ta.rank4_order = t[3:]
                continue
            if t.startswith("f__"):
                ta.rank5_family = t[3:]
                continue
            if t.startswith("g__"):
                ta.rank6_genus = t[3:]
                continue
            if t.startswith("s__"):
                ta.rank7_species = t[3:]
                continue
            if t.startswith("t__"):
                ta.rank8_strain = t[3:]
                continue

            log.warning(f"Unknown rannk '{t}'")

        return ta

    def __str__(self):
        return f"{self.abundance} {self.taxes}"


TaxonomyAbundanceList = List[TaxonomyAbundanceParserResult]


class TaxonomyParserResult:

    def __init__(self, sample_name: str = "", taxonomy_abundance: TaxonomyAbundanceList = []):
        self.sample_name = sample_name
        self.taxonomy_abundances = taxonomy_abundance

    def normalise(self):
        max_value = 0
        min_value = 99943243
        for t in self.taxonomy_abundances:
            if t.abundance > max_value:
                max_value = t.abundance
            if t.abundance < min_value:
                min_value = t.abundance

        for t in self.taxonomy_abundances:
            before = t.abundance

            t.abundance = (t.abundance - min_value) / (max_value - min_value)


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
                result.taxonomy_abundances.append(taxonomy)

        return result

    @staticmethod
    def parse_tax_line(line: str) -> TaxonomyAbundanceParserResult:
        """
        Parse eg: k__Bacteria|p__Actinobacteria	0.84814
        :param line:
        :return: TaxonomyAbundance
        """
        taxonomy = TaxonomyAbundanceParserResult()
        split = line.split("\t")
        taxonomy.abundance = float(split[1])
        tax_line = split[0]

        if "|" in tax_line:
            taxes = tax_line.split("|")
            taxonomy.taxes.extend(taxes)
        else:
            taxonomy.taxes.append(tax_line)

        return taxonomy


class TaxonomyMergedParser:
    def __init__(self, file_content: str):
        self.file_content = file_content

    def parse(self) -> List[TaxonomyParserResult]:
        result: List[TaxonomyParserResult] = []
        count = 0
        for l in self.file_content.splitlines():
            count += 1
            if l.startswith("SampleID"):
                split = l.split('\t')
                split.pop(0)
                for sample_name in split:
                    result.append(TaxonomyParserResult(sample_name=sample_name))
                continue

            if l.startswith("#"):
                continue

            if count % 200 == 0:
                log.debug(f"Sada sam na count {count}")

            if l.startswith("k__"):
                split = l.split("\t")
                taxonomy_path = split.pop(0)
                i = 0
                while i < len(split):
                    abundance = split[i]
                    result[i].taxonomy_abundances.append(TaxonomyParser.parse_tax_line(f"{taxonomy_path}\t{abundance}"))
                    i += 1

        return result


def parse_taxonomy_file(file: InMemoryUploadedFile) -> TaxonomyParserResult:
    tax_parser = TaxonomyParser(file.read().decode("UTF-8"))
    tax_result = tax_parser.parse()
    return tax_result


def parse_taxonomy_merged_file(file: InMemoryUploadedFile) -> List[TaxonomyParserResult]:
    parser = TaxonomyMergedParser(file.read().decode("UTF-8"))
    return parser.parse()


def run_parse_in_background(file_type, files):
    # threadPoll.submit(task)
    # threadPoll = ThreadPoolExecutor(max_workers=4)
    pass


def task():
    for i in range(10):
        print("poll parse ", i, " ")
        sleep(2)
