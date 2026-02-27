from django.shortcuts import render, HttpResponse
from App.models import Contact
from App.models import Index
from App.models import Menu
from App.models import Payement
from App.models import Checkout1

# Create your views here.


def index(request):
    obj = Index.objects.all()
    return render(request, 'website.html', {'obj': obj})
    # return HttpResponse("Hello world")


def button_basic(request):
    dests = Menu.objects.all()
    return render(request, 'Button_basic.html', {'dests': dests})


def menu(request):
   dests = Menu.objects.all()
   return render(request, 'menu.html', {'dests': dests})


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("You are on Services")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("You are on About")


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()

    return render(request, 'contact.html')
    # return HttpResponse("You are on Contact")


def search(request):
    name = request.GET['query']
    if name:
        # obj = Index.objects.all()

        allposts = Index.objects.filter(shop_name__icontains=name)
        return render(request, 'website.html', {'obj': allposts})
    else:
        return render(request, 'search.html')

def cart(request):
    name = request.GET['query']

def checkout(request):
   dests1 = Menu.objects.all()
   return render(request, 'checkout.html', {"dest1": dests1})

def final(request):
   return render(request, 'final.html')

def Checkout1(request):
    product = 'Cake'
    quantity = '0'
    if request.method == "POST":
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip1 = request.POST.get('zip')

        #print(name, email, address)


        c1 = Checkout1(name=name, email=email, address=address, city=city, state=state, zip=zip1, product=product, quantity=quantity)
        c1.save()
    return render(request, 'final.html')