from django.shortcuts import render

from guitarradar.guitars.models import Guitar, Brand


def guitar_detail(request):
    guitar = Guitar.objects.get(
        brand__name=request.GET.get('brand'),
        model_name=request.GET.get('model_name')
    )
    return render(request, 'guitars/guitar.html', {'guitar': guitar})


def brand_detail(request):
    brand = Brand.objects.get(
        brand__name=request.GET.get('brand')
    )
    return render(request, 'guitars/brand.html', {'brand': brand})
