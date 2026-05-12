from django.shortcuts import render

# Create your views here.
def all_stuff(request):
    return render(request, 'intern_project/all_stuff.html')