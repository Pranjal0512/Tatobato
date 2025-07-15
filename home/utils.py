from django.db import connection

def create_customer(name, email, phone, address):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO Customers (name, email, phone_no, address)
            VALUES (%s, %s, %s, %s)
            """,
            [name, email, phone, address]
        )