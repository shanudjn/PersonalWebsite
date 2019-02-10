from django.shortcuts import render
import requests, json
from .models import Contact

# Create your views here.

def index(request):
    if (request.method=="POST"):
        #the parameter inside the get method refers to the name given to the input field in the html file
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        #print(first_name)

        r = requests.get('http://api.icndb.com/jokes/random?firstName='+ first_name +'&lastName='+ last_name)
        joke = json.loads(r.text).get('value').get('joke')
        print(joke)
        return render(request,'mysite/index.html',{'joke':joke})
    else:
        return render(request,'mysite/index.html')
def portfolio(request):
    return render(request,'mysite/portfolio.html')
def contact(request):
    #the parameter inside the get method refers to the name given to the input field in the html file
    if (request.method == 'POST'):
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")

        c = Contact(email=email, subject=subject, message=message)
        c.save()

        return render(request,'mysite/thank.html')

    else:
        return render(request,'mysite/contact.html')
