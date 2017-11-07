from django.core.management.base import BaseCommand
from django.db import IntegrityError
from demo.models import CallNotice
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = []
        for suffix in self.suffixes():
            url = 'https://prosas.com.br/editais/' + suffix
            self.create_call_notice(url)

    def suffixes(self):
        return [
            '2653-1o-premio-projeteee-de-arquitetura-bioclimatica-categoria-estudante',
            '3080-2o-edital-fomento-a-cultura-da-periferia-de-sao-paulo',
            '2774-segunda-chamada-cepf-cerrado-2017',
            '3062-premio-off-flip-de-literatura-contos'
        ]

    def create_call_notice(self, url):
        html = urlopen(url)
        soup = BeautifulSoup(html.read(), 'html.parser')

        title = soup.h1.text
        description = soup.find('div', { 'class': 'summernote_description' }).text

        notice = CallNotice(title=title, description=description, url=url)
        try:
            notice.save()
        except IntegrityError:
            print("A notice with this URL is already present")
