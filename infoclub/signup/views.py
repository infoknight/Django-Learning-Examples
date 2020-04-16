from django.shortcuts import render
from django.http import HttpResponse
from signup.models import regModel      
from signup.registration_form import newregForm    #Import user input data directly from form and add to the model

# Create your views here.
def index(request):
    #return HttpResponse("<em>Hello World!<em>")
    index_dict = {'insert_me' : "Inserted in views by Template Tag"}
    return render(request, "signup/index.html", context=index_dict)

def regView(request):
    formObj = newregForm()
    form_dict = {'call_form' : formObj}
    
    if request.method == "POST":
        formObj = newregForm(request.POST)

        if formObj.is_valid():
            formObj.save(commit = True)
            return index(request)
    return render(request, "signup/registration.html", context=form_dict)

def datasheet(request):
    customers_list = regModel.objects.order_by("first_name")
    customer_dict = {'signup':customers_list}
    return render(request, "signup/datasheet.html", context=customer_dict)
