import requests
from django.http import JsonResponse

def search_products(request):
    query = request.GET.get('q', '')
    if query:
        try:
            book_response = requests.get(f'http://localhost:8001/book/api/search?q={query}')
            mobile_response = requests.get(f'http://localhost:8001/mobile/api/search?q={query}')
            clothes_response = requests.get(f'http://localhost:8001/clothes/api/search?q={query}')
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': f'Request failed: {e}'}, status=500)

        books = book_response.json() if book_response.status_code == 200 else []
        mobiles = mobile_response.json() if mobile_response.status_code == 200 else []
        clothes = clothes_response.json() if clothes_response.status_code == 200 else []

        result = {
            'books': books,
            'mobiles': mobiles,
            'clothes': clothes
        }
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'error': 'No search query provided.'}, status=400)
