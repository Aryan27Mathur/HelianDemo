from django.shortcuts import render, HttpResponse
from .models import User, Company, ETF
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd
import csv
import re
from PyPDF2 import PdfFileReader
from io import BytesIO
#import pandas as pd
# Create your views here.

def home(request):
    return render(request, "home.html")

def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users":users})

def generate_companies(request):
    csv_file_path = r"C:\Users\aryan\OneDrive\Documents\Helian\HelianDemo\backend\helian\mainapp\constituents.csv"   
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            company = Company.objects.create(
                symbol=row['Symbol'],
                name=row['Name'],
                sector=row['Sector']
            )
            company.save()
            print(str(row['Name']) + " saved!")
    return HttpResponse("Companies generated and added to the database.")

# def generate_etfs(request):

#     df = pd.read_csv("C:/Users/am943/Downloads/etfs_details_type_fund_flow.csv", header=0)

#     esg_data = df[["Symbol", "ETF Name", "ESG Score"]]
#     etfs = []
#     for index, row in df.iterrows():
#         etf_instance = ETF(
#             symbol=row['Symbol'],
#             name=row['ETF Name'],
#             vf_esg_score=row['ESG Score']
#         )
#         etfs.append(etf_instance)
#         print(str(row['ETF Name']) + " saved!")
#     ETF.objects.bulk_create(etfs, ignore_conflicts=True)
#     return HttpResponse("Companies generated and added to the database.")
   

@csrf_exempt
def add_esg_report(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            symbol = payload.get('symbol')
            esg_report = payload.get('esg_report')

            if not symbol or not esg_report:
                return JsonResponse({'error': 'Symbol and esg_report fields are required'}, status=400)

            company = Company.objects.get(symbol=symbol)
            company.esg_report = esg_report
            company.save()

            return JsonResponse({'success': 'ESG report link updated successfully'})

        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company with provided symbol does not exist'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

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

@csrf_exempt
def update_esg_score(request):
    if request.method == 'POST':
        # Extract data from the POST request
        print(request.body)
        print()
        data = json.loads(request.body)
        is_etf = (data.get('etf') == "yes")
        symbol = data.get('symbol')
        total_score = data.get('total_score')
        e_score = data.get('e_score')
        s_score = data.get('s_score')
        g_score = data.get('g_score')

        # Create a new User object and save it to the database
        if(is_etf):
            #do something
            pass
        Company.objects.filter(symbol=symbol).update(yf_t_score=total_score, yf_e_score = e_score, yf_s_score = s_score, yf_g_score = g_score)

        return HttpResponse(f"score for {symbol} updated", status=201)

    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def get_all_company_symbols(request):
    symbols = [item['symbol'] for item in Company.objects.all().values("symbol")]
    print(symbols)

    return HttpResponse(",".join(symbols), status=200)

@csrf_exempt
def post_portfolio(request):
    if request.method == 'POST':
        print('testing')
        file_data = request.FILES['file']
        file_content = file_data.file.read()

        pdf_stream = BytesIO(file_content)

        pdf_reader = PdfFileReader(pdf_stream)

        # Extract text from each page of the PDF file

        start_pattern = r'Portfolio Summary'
        end_pattern = r'Total Securities'

        total_text=""
        for page_num in range(pdf_reader.getNumPages()):
            if(page_num == 0):
                continue
            page = pdf_reader.getPage(page_num)
            total_text += page.extract_text()

        start_match = re.search(start_pattern, total_text)
        end_match = re.search(end_pattern, total_text)

        if start_match and end_match:

            # Extract the text between start and end points
            table_text = total_text[start_match.end():end_match.start()]
            
            lines = [line.strip() for line in table_text.split('\n') if line.strip()]
            data_lines = lines[1:]
            data = [(data_lines[i] + ' ' + data_lines[i+1]).replace('%', '% ') for i in range(0, len(data_lines), 2)]

            # Split each line by space to create a 2D array
            split_data = []
            for line in data:
                first_item, rest_items = line.split('%', 1)
                split_data.append([first_item.strip('%').strip()] + rest_items.strip().split())

            print(split_data)

            df = pd.DataFrame(split_data, columns=["Securities Held in Account", "Sym/Cusip", "Acct Type", "Qty", "Price", "Mkt Value", "Est. Dividend Yield", "% of Total Portfolio"])
            print(df.head())

            tickers_and_percentages = df[['Sym/Cusip', "Mkt Value", '% of Total Portfolio']].to_dict(orient='records')
            # Create a JSON object
            payload = {
                "portfolio": tickers_and_percentages
            }
            print(payload)
        else:
            return None
        return JsonResponse(payload)
        # except Exception as e:
        #     # Handle any exceptions that occur during file writing
        #     return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)





