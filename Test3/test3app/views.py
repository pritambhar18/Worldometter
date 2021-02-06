from django.shortcuts import render
import csv, io
# Create your views here.
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from tablib import Dataset
from .filters import UserFilter
from .models import reg_table, log_table
from django.views.generic import TemplateView
from .forms import reg_tableForm
# from .visualization import Visualization
# from.resources import SelectionForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import *
from django.contrib.sessions.models import Session

from .resources import SelectionForm
from .visualization import Visualization


def demo(request):
    return render(request, "demo.html")


def index(request):
    return render(request, "index.html")


def reg(request):
    # desk = destination()
    return render(request, "registration.html")  # ,{'desk1':desk})


def handelreg(request):
    if request.method == 'POST':
        aid = request.POST['aid']
        fname = request.POST['fname']
        birthdate = request.POST['birthdate']
        email = request.POST['email']
        nationality = request.POST['nationality']
        location = request.POST['location']
        domain = request.POST['domain']
        branch = request.POST['branch']
        gender = request.POST['gender']
        joiningdate = request.POST['joiningdate']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']
        if len(aid) > 4:
            messages.error(request, "Associate id must be under four digit")
            return redirect("reg")
        if reg_table.aidExits():
            messages.error(request, "Associate id already Registerd....")
            return redirect("reg")
        if len(fname) < 20:
            messages.error(request, "Associate id must be under four digit")
            return redirect("reg")
        if len(email) < 10:
            messages.error(request, "Associate id must be under four digit")
            return redirect("reg")
        if reg_table.isExits(email):
            messages.error(request, "Email_id already Registerd....")
            return redirect("reg")
        if password <6:
            messages.error(request, "Password too short....... ")
        if password != confirmpass:
            messages.error(request, "Password does not match")
            return redirect("reg")
        sgn = reg_table(aid=aid, fname=fname, email=email, birthdate=birthdate, nationality=nationality,
                        location=location, domain=domain, branch=branch, gender=gender, joiningdate=joiningdate,
                        password=password, confirmpass=confirmpass)
        sgn.save()
        messages.success(request, "success")
        return redirect('index')
    else:
        return render(request, "reg")


# login
def login(request):
    if request.method == 'POST':
        loginid = request.POST['loginid']
        loginpass = request.POST['loginpass']

        user = auth.authenticate(username=loginid, password=loginpass)
        print(user)
        if user is None:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")
        else:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
    else:
        return HttpResponse("404- Not found")


# logout
def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('demo')


# upload
def upload(request):
    # declaring template
    template = "uploadcsv.html"
    data = reg_table.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be aid, fname, birthdate,email,nationality,location,domain,branch,gender,joiningdate ',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = reg_table.objects.update_or_create(
            aid=column[0],
            fname=column[1],
            birthdate=column[2],
            email=column[3],
            nationality=column[4],
            location=column[5],
            domain=column[6],
            branch=column[7],
            gender=column[8],
            joiningdate=column[9],
            password=column[10],
            confirmpass=column[11]
        )

    context = {}

    return render(request, "uploadcsv.html")


# Display
def show(request):
    employees = reg_table.objects.all()
    return render(request, "show.html", {'employees': employees})


# edit
def edit(request, id):
    employee = reg_table.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


# Update
def update(request, id):
    employee = reg_table.objects.get(id=id)
    form = reg_tableForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("show")
    else:
        print(form.errors)
    return render(request, 'edit.html', {'employee': employee})


# Delete
def destroy(request, id):
    if request.method=="POST":
        employee = reg_table.objects.get(id=id)
        employee.delete()
        return redirect("show")
    else:
        return HttpResponse("404- Not found")


# search
def searchposts(request):
    if request.GET['q']:
        q = request.GET['q']
        books = reg_table.objects.filter(Q(fname__icontains=q) | Q(aid__icontains=q) | Q(location__icontains=q))
        return render(request, 'search.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


# Admin Registration
def AdminTable(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        #   confirmpass=request.POST['confirmpass']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password)
        user.save()
        return redirect('/')

    else:
        return HttpResponse("404- Not found")


def adminreg(request):
    return render(request, "adminreg.html")


def delete(request):
    return render(request, "delete.html")

# visualization

def visualization(request):
    if request.method != 'POST':
        return render(request, 'visualization.html', {
            "form": SelectionForm()
        })
    else:
        try:
            form = SelectionForm(request.POST)
            choice = ""
            if form.is_valid():
                choice = form.cleaned_data['selection']
            content = ""
            v = Visualization()
            if choice == 'BAR':
                content = v.get_bar_plots(fields=['location'])
            else:
                content = v.get_charts(fields=['location'])
        except Exception  as e:
            print(e)
            return render(request, 'visualization.html',
                          {
                              "error_message": "Some error while getting visualization {}".format(e),
                              "form": SelectionForm()
                          }
                          )

    return render(request, 'visualization.html', {"data": content, "form": SelectionForm()})




