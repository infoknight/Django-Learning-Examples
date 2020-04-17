from django.shortcuts import render
from django.http import HttpResponse
from signup.registration_form import  UserForm, UserProfileInfoForm    #Import user input data directly from form and add to the model

# Create your views here.
def index(request):
    #return HttpResponse("<em>Hello World!<em>")
    index_dict = {'insert_me' : "Inserted in views by Template Tag"}
    return render(request, "signup/index.html", context=index_dict)

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
            profile.user = user         #To ensure one-to-one mapping between users and profiles

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
        
            registered = True           #Change var "registered" = True after saving the information

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'signup/registration.html',
                 {'registered':registered,
                  'user_form' :user_form,
                  'profile_form' : profile_form})

def datasheet(request):
    #customers_list = UserForm.objects.order_by("username")
    customers_list = UserForm()
    customer_dict = {'signup':customers_list}
    return render(request, "signup/datasheet.html", context=customer_dict)
