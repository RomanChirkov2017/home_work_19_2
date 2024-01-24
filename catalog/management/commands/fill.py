from django.core.management import BaseCommand, call_command
import os

from django.db import ProgrammingError, IntegrityError

from config.settings import BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        path = os.path.join(BASE_DIR, 'fixtures_data.json')

        try:
            call_command('loaddata', path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid fixtures: {e}', self.style.NOTICE)
        else:
            self.stdout.write('OK', self.style.SUCCESS)

