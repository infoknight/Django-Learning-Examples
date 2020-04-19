from django.shortcuts import render
from cafe.signup import signupForm, UserForm, UserProfileInfoForm
from cafe.models import signupModel
#Login 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    index_dict = {'insert_me' : 'Click <a href="www.google.com">here</a> for cyber flash news'}
    return render(request, "cafe/index.html", context=index_dict)

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
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            
            registered = True           #Change var "registered" = True after saving the information
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'cafe/signup.html',
                 {'registered':registered,
                  'profile_form':profile_form,
                  'user_form':user_form})

def signup(request):
    #Create a user signup form and include the object here
    formObj   = signupForm()
    form_dict = {'call_form' : formObj}

    if request.method == "POST":
        formObj       = signupForm(request.POST)

        if formObj.is_valid():
            formObj.save(commit = True)
            return index(request)
    return render(request, "cafe/signup.html", context=form_dict)

def memberslist(request):
    members_list  = signupModel.objects.order_by("first_name")
    customer_dict = {'members' : members_list}
    return render(request, "cafe/members-list.html", context=customer_dict)

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
        return render(request, 'cafe/login.html', {})       #Empty context dict





