import time 

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for DB...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(self.style.WARNING('DB connection failed, retrying...'))
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('DB Connected!'))