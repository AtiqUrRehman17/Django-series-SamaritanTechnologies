from django.shortcuts import render
from .forms import ChaiVarietyForm
from .models import Store   # import your model

# Create your views here.
def all_stuff(request):
    return render(request, 'intern_project/all_stuff.html')


def store_view(request):
    stores = None
    form = ChaiVarietyForm()   # initialize form first

    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)

        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(
                chai_varity=chai_varity
            )

    return render(
        request,
        'intern_project/chai_stores.html',
        {
            'stores': stores,
            'form': form
        }
    )