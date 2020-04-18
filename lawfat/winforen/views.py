from django.shortcuts import render
from winforen.forms import registrationForm, UserForm
from winforen.models import registrationModel
#Login 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required                     #decorator; MUST BE ABOVE THE REQUIRED FUNCTION; Automatically checks if a user is logged in
def user_logout(request):           #Logout the already loggedin user; use decorator above to check if user is loggedin
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):          #Special page for only the loggedin users
    return HttpResponse("Congratulations! : You have successfully loggedin!")

def register(request):

    registered = False              #Create a var "registered"

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True           #Change var "registered" = True after saving the information
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration.html',
                 {'registered':registered,
                  'user_form' :user_form})

def memberslist(request):
        members_list  = registrationModel.objects.order_by("first_name")
        customer_dict = {'members' : members_list}
        return render(request, "members-list.html", context=customer_dict)

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')         #Get username from login.html
        password = request.POST.get('password')         #Get password from login.html

        user = authenticate(username=username, password=password)   #built-in user authentication
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("You are not registered")

        else:
            print("Failed login attempt detected : ")
            print("Username : {} and Password : {}".format(username, password)) #Prints failed login attempts to console
                                                                                #Later redirect to error log file
            return HttpResponse("Please check your credentials and login again")

    else:
        return render(request, 'login.html', {})       #Empty context dict





