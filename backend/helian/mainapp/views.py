from django.shortcuts import render, HttpResponse
from .models import User, Company
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import csv
# Create your views here.

def home(request):
    return render(request, "home.html")

def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users":users})

def generate_companies(request):
    csv_file_path = 'constituents.csv'
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            company = Company.objects.create(
                symbol=row['Symbol'],
                name=row['Name'],
                sector=row['Sector']
            )
            company.save()
    return HttpResponse("Companies generated and added to the database.")

@csrf_exempt
def new_user(request):
    if request.method == 'POST':
        # Extract data from the POST request
        print(request.body)
        print()
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')

        # Create a new User object and save it to the database
        user = User.objects.create(name=name, email=email)

        return JsonResponse({'message': 'Thanks for signing up! Check back for future updates to Helian.'}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)