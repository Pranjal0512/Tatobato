from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import create_customer

@api_view(['GET', 'POST'])
def home(request):
    return render (request, "index.html")
        # Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        create_customer(name, email, phone, address)

        return render(request, 'index.html', {'message': 'Customer added successfully!'})

    return render(request, 'index.html')