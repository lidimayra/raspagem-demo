from django.core.management.base import BaseCommand
from django.db import IntegrityError
from demo.models import CallNotice
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://prosas.com.br/editais/2653-1o-premio-projeteee-de-arquitetura-bioclimatica-categoria-estudante'

        html = urlopen(url)
        soup = BeautifulSoup(html.read(), 'html.parser')

        title = soup.h1.text
        description = soup.find('div', { 'class': 'summernote_description' }).text

        notice = CallNotice(title=title, description=description, url=url)
        try:
            notice.save()
        except IntegrityError:
            print("A notice with this URL is already present")
