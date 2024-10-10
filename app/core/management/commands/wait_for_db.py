"""
Django command to wait for db connection
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database connection"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db connection...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2Error):
                self.stdout.write("Database unavailable...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
