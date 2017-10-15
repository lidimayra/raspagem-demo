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
