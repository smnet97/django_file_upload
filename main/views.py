from django.shortcuts import render
from .forms import NewsForm
from django.shortcuts import redirect


def index(request):
    form = NewsForm()
    return render(request, 'main/index.html', context={
        'form': form
    })

def upload(request):
    form = NewsForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'main/index.html', context={
            'form': form
        })
    form.save()
    return redirect('/')