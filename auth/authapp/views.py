# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import UserData
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

@csrf_exempt
def Create_User(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        password = data.get('password', '')

        # Use Django's User model for creating users with hashed passwords
        new_user = UserData.objects.create(name=name, password=make_password(password))
        new_user.save()
        return JsonResponse({'message': 'User created successfully!'})

    return JsonResponse({'message': 'Invalid request method.'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        password = data.get('password', '')

        user = UserData.objects.filter(name=name).first()

        if user and check_password(password, user.password):
            # User login successful, you can generate authentication tokens here
            return JsonResponse({'message': 'Login successful!'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid request method.'})