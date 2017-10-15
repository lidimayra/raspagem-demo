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
    speakers  = []

    url = f'http://seti.ufla.br/'
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    boxes = soup.findAll('div', { 'class': 'box-nome-palestrante' })

    if (len(query)) > 0:
        for box in boxes:
            name = box.text
            if query.upper() in name:
                speakers.append(box.text)

    context_dict = { 'raw_values': speakers }
    return render(request, 'demo/seti.html', context_dict)
