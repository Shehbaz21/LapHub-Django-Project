from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def Apple_Mackbook(request):
    return render(request, 'apple_mackbook.html')

def hp_laptop(request):
    return render(request, 'hp_laptop.html')

def dell_laptop(request):
    return render(request, 'dell_laptop.html')  

def contact_us(request):
    return render(request, 'contact_us.html')   
  

