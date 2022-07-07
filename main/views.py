from django.shortcuts import render
from .forms import NewsForm
from django.shortcuts import redirect
from .models import News


def index(request):
    form = NewsForm()
    news = News.objects.order_by('-id').all()
    return render(request, 'main/index.html', context={
        'form': form,
        'news': news
    })


def upload(request):
    form = NewsForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'main/index.html', context={
            'form': form
        })
    form.save()
    return redirect('/')