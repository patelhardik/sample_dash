from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def dashboard(request):
    context = {
        'dropdown1': '',
        'dropdown2': '',
        'dropdown3': '',
        'dropdown4': '',
        'dropdown5': ''
    }

    if request.method == 'POST':
        # Get the submitted values
        context['dropdown1'] = request.POST.get('dropdown1', '')
        context['dropdown2'] = request.POST.get('dropdown2', '')
        context['dropdown3'] = request.POST.get('dropdown3', '')
        context['dropdown4'] = request.POST.get('dropdown4', '')
        context['dropdown5'] = request.POST.get('dropdown5', '')

        # Process the data as needed
        # For example, you could save the data to the database

        # Redirect back to the original page with the submitted values
        
        print(f"Dropdown1 = {context['dropdown1']}")
        print(f"Dropdown2 = {context['dropdown2']}")
        print(f"Dropdown3 = {context['dropdown3']}")
        print(f"Dropdown4 = {context['dropdown4']}")
        print(f"Dropdown5 = {context['dropdown5']}")
        return render(request, 'dashboard.html', context)

    return render(request, 'dashboard.html', context)



