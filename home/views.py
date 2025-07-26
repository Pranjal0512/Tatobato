from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django API backend is running!")
@api_view(['POST'])
def register(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        print(f"Got: name={name}, email={email}, password={password}")  # DEBUG

        if not name or not email or not password:
            return Response({"error": "All fields are required"}, status=400)

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Customers (name, email, phone_no) VALUES (%s, %s, %s)",
                [name, email, password]
            )

        return Response({"message": "User registered!"}, status=201)

    except Exception as e:
        print("Error:", e)  # DEBUG
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Customers WHERE email = %s AND phone_no = %s", [email, password])
        user = cursor.fetchone()

    if user:
        return Response({"message": "Login successful"})
    else:
        return Response({"error": "Invalid credentials"}, status=401)
