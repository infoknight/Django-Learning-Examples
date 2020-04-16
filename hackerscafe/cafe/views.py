from django.shortcuts import render
from django.http import HttpResponse
from cafe.signup import signupForm
from cafe.models import signupModel

# Create your views here.
def index(request):
    index_dict = {'insert_me' : 'Click <a href="www.google.com">here</a> for cyber flash news'}
    return render(request, "cafe/index.html", context=index_dict)

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




