from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,medicineForm
from django.contrib.auth.decorators import login_required
from.models import medicine


# Create your views here.


def home(request):
    return render(request,"home.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created ')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})   

@login_required()
def profile(request):
    if 'serh' in request.GET:
        vb=request.GET['serh']
        obj=medicine.objects.filter(name__icontains=vb)
    else:    
        obj=medicine.objects.all()
    return render(request, 'profile.html',{'data':obj})


def create(request):
        if request.method == "POST":
            form = medicineForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('profile')
            return redirect('profile')
        else:
            form = medicineForm
            context = {
                'form':form
            }       

            return render(request, 'add.html',context)    

def update(request,id):
    obj=medicine.objects.get(id=id)
    form=medicineForm(instance=obj)

    if request.method=='POST':
        form=medicineForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context={
        'form':form
    }
    return render(request,'update.html',context)




def delete(request,id):
    obj = medicine.objects.get(id=id)
    obj.delete()
    return redirect('profile')
    return render(request,'delete.html',{'data':obj})