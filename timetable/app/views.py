from django.shortcuts import render, redirect, get_object_or_404
from .models import TimeTable, TimeTableForm, UpdateTimeTableForm
from django.contrib.auth.decorators import login_required


def Home(request):
    tb = TimeTable.objects.all()
    return render(request, 'app/home.html', {'tb': tb})


@login_required(login_url='accounts:login')
def UpdateTB(request):
    tb = TimeTable.objects.all()
    return render(request, 'app/update.html', {'tb': tb})


@login_required(login_url='accounts:login')
def Update(request, pk):
    update_tb = TimeTable.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTimeTableForm(request.POST, instance=update_tb)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    else:
        form = UpdateTimeTableForm()
    context = {
        'form': form
    }
    return render(request, 'app/update_tb.html', context)


@login_required(login_url='accounts:login')
def Add(request):
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TimeTableForm()
    context = {
        'form': form
    }
    return render(request, 'app/add.html', context)
