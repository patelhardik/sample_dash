from django.shortcuts import render

def dashboard(request):
    context = {
        'selectview': request.POST.get('selectview', ''),
        'hw_rev': request.POST.get('hw_rev', ''),
        'apk': request.POST.get('apk', ''),
        'kpi': request.POST.get('kpi', ''),
        'bspview': request.POST.get('bspview', '')
    }
    print(f"selectview = {context['selectview']}")
    print(f"hw_rev = {context['hw_rev']}")
    print(f"apk = {context['apk']}")
    print(f"kpi = {context['kpi']}")
    print(f"bspview = {context['bspview']}")

    return render(request, 'dashboard.html', context)



