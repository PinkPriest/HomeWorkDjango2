from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_all = Phone.objects.all()
    sort = request.GET.get('sort')
    queryset = phones_all
    if sort == ('min_price'):
        context = {'phones': queryset.order_by('price')}
    elif sort == ('max_price'):
        context = {'phones': queryset.order_by('-price')}
    elif sort == ('name'):
        context = {'phones': queryset.order_by('name')}
    else:
        context = {'phones': queryset}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone,}
    return render(request, template, context)
