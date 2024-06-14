# views.py
from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    if request.method == 'POST':
        # Handle form submission
        dropdown1 = request.POST.get('dropdown1')
        dropdown2 = request.POST.get('dropdown2')
        dropdown3 = request.POST.get('dropdown3')
        dropdown4 = request.POST.get('dropdown4')
        dropdown5 = request.POST.get('dropdown5')
        # Process the form data as needed
        # return HttpResponse("Form submitted successfully")
        print(f"Dropdown1 = {dropdown1}")
        print(f"Dropdown2 = {dropdown2}")
        print(f"Dropdown3 = {dropdown3}")
        print(f"Dropdown4 = {dropdown4}")
        print(f"Dropdown5 = {dropdown5}")
    return render(request, 'dashboard.html')
