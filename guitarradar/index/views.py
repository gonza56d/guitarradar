
from django.shortcuts import render

from guitarradar.guitars.models import Guitar


def main(request):
    guitars = Guitar.objects.all()[:100]
    return render(request, 'index/main.html', {'guitars': guitars})
