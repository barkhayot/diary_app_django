from django.shortcuts import render, redirect
from . models import Letter
from . forms import LetterForm

def index(request):
    letters = Letter.objects.order_by('-date_posted')

    context = {'letters': letters}
    return render (request, 'letters/index.html', context)

def add(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else :

        form = LetterForm()

    context = {'form': form }
    return render(request, 'letters/add.html', context)