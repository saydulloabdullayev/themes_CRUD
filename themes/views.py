# themes/views.py

from django.shortcuts import render, redirect
from .models import Theme

def theme_list(request):
    themes = Theme.objects.all()
    return render(request, 'themes/theme_list.html', {'themes': themes})

def theme_detail(request, pk):
    theme = Theme.objects.get(pk=pk)
    return render(request, 'themes/theme_detail.html', {'theme': theme})

def theme_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Theme.objects.create(title=title, description=description)
        return redirect('theme_list')
    return render(request, 'themes/theme_form.html')

def theme_update(request, pk):
    theme = Theme.objects.get(pk=pk)
    if request.method == 'POST':
        theme.title = request.POST.get('title')
        theme.description = request.POST.get('description')
        theme.save()
        return redirect('theme_list')
    return render(request, 'themes/theme_form.html', {'theme': theme})

def theme_delete(request, pk):
    theme = Theme.objects.get(pk=pk)
    theme.delete()
    return redirect('theme_list')
