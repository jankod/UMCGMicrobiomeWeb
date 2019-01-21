from django.core.management import BaseCommand

from app.util.demo.read_file_demo import demo1, demo2


class Command(BaseCommand):

    def handle(self, *args, **options):
        demo2()
        pass
