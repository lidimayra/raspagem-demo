from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from urllib.request import urlopen

def index(request):
    return render(request, 'demo/index.html')

def fatec(request):
    query = request.GET.get('q', '')
    teachers  = []

    url = f'http://www.fatecjd.edu.br/portal/sobre-nos/corpo-docente/'
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    lines = soup.tbody.findAll('tr')

    if (len(query)) > 0:
        for line in lines:
            name = line.td.text
            if query.upper() in name:
                teachers.append(line.text)

    context_dict = { 'raw_values': teachers }
    return render(request, 'demo/fatec.html', context_dict)

def seti(request):
    query = request.GET.get('q', '')

    url = f'http://seti.ufla.br/'
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    boxes = soup.findAll('div', { 'class': 'box-nome-palestrante' })

    talks = []

    if (len(query)) > 0:
        for box in boxes:
            name = box.text
            if query.upper() in name:
                speaker = box.find('p', { 'class': 'nome-palestrante' }).text
                talk  = box.find('p', { 'class': 'palestra' }).text
                company = box.find('p', { 'class': 'empresa-palestrante' }).text
                talks.append({ 'Palestrante': speaker, 'Empresa': company, 'Palestra': talk })

    context_dict = { 'talks': talks }
    return render(request, 'demo/seti.html', context_dict)
