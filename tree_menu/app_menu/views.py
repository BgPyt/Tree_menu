from django.shortcuts import render


def root_site(request):
    return render(request, 'app_menu/index.html')

def item_detail(request, slug):
    return render(request, 'app_menu/items-detail.html')







