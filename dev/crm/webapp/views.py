# Imports
#----------------------------------------------------------------
from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

# to logout
from django.contrib.auth.models import auth
# to auth username/password
from django.contrib.auth import authenticate

# auth users can see dashboard
from django.contrib.auth.decorators import login_required

# import model for Record
from . models import Record

# notifications
from django.contrib import messages

#----------------------------------------------------------------

# Create your views here.

def home(request):

    return render(request, 'webapp/index.html')

#----------------------------------------------------------------
# Register a user 

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()
            messages.success(request, "Uspešno kreiran nalog!")
            return redirect('login')

    context = {'form': form}

    return render(request, 'webapp/register.html', context = context)

#----------------------------------------------------------------
# Login a user

def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            
            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')

        else:
            messages.error(request, "Pogrešno uneseni podaci!")

    context = {'form2':form}

    return render(request, 'webapp/login.html', context = context)

#----------------------------------------------------------------
# Dashboard 


@login_required(login_url='login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context = context)


#----------------------------------------------------------------
# Create a Record

@login_required(login_url='login')
def create(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, "Zahtev snimljen!")
            return redirect('dashboard')
    
    context = {'cForm': form}

    return render(request, 'webapp/create-record.html', context = context)

#----------------------------------------------------------------
# Update a Record

@login_required(login_url = 'login')
def update(request, pk):

    record = Record.objects.get(id = pk)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":

        form = UpdateRecordForm(request.POST, instance=record)
    
        if form.is_valid():

            form.save()
            messages.success(request, "Zahtev izmenjen!")
            return redirect('dashboard')
        
    context = {'uForm': form}

    return render(request, "webapp/update-record.html", context = context)

#----------------------------------------------------------------
# Read / View a Singular Record
@login_required(login_url='login')
def read_record(request, pk):

    all_records = Record.objects.get(id = pk)

    context = {'records': all_records}

    return render(request, 'webapp/view-record.html', context = context)

#----------------------------------------------------------------
# Delete a Record

@login_required(login_url='login')
def delete(request,pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Zahtev obrisan!")

    return redirect('dashboard')



#----------------------------------------------------------------
# Logout a User

def logout(request):

    auth.logout(request)

    messages.success(request, "Uspešna odjava!")

    return redirect('login')


