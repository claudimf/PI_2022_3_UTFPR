from django.core.management.base import BaseCommand
from django.core import management

import os


class Command(BaseCommand):
    help = 'Show all available styles'

    def handle(self, *args, **kwargs):
        self.stdout.write('\n- - - - -')
        self.stdout.write(self.style.HTTP_SERVER_ERROR('\nimportacao das fixtures do projeto'))

        # geolocalizacao

        self.stdout.write(self.style.HTTP_NOT_MODIFIED('\nprocesssando app: crypto_games'))

        diretorio_fixtures = 'crypto_games/fixtures/'
        fixtures = sorted(os.listdir(diretorio_fixtures))

        for fixture in fixtures:
            self.stdout.write(self.style.SQL_KEYWORD('\nmodel: ' + fixture))
            management.call_command('loaddata', diretorio_fixtures + fixture)

        self.stdout.write(self.style.SUCCESS('\nimportado com sucesso\n'))