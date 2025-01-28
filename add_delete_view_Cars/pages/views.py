from django.shortcuts import render,redirect,get_object_or_404
from .models import Car
from .forms import CarForm
# Create your views here.
def list(request):
    cars=Car.objects.all()
    return render(request,'cars/list.html',{'cars':cars})

def add(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:list')  # قم بتوجيه المستخدم إلى صفحة نجاح
    else:
        form = CarForm()
    return render(request, 'cars/add.html', {'form': form})

def delete(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            year = form.cleaned_data['year']
            car = get_object_or_404(Car, brand=brand, year=year)
            car.delete()
            return redirect('pages:list')
    else:
        form = CarForm()
    return render(request, 'cars/delete.html', {'form': form})