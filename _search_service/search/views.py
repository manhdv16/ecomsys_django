import requests
from django.http import JsonResponse

def search_products(request):
    query = request.GET.get('q', '')
    if query:
        book_response = requests.get(f'http://localhost:8000/book/api/search?q={query}')
        mobile_response = requests.get(f'http://localhost:8000/mobile/api/search?q={query}')
        clothes_response = requests.get(f'http://localhost:8000/clothes/api/search?q={query}')
        
        if book_response.status_code == 200:
            books = book_response.json()
        if mobile_response.status_code == 200:
            mobiles = mobile_response.json()
        if clothes_response.status_code == 200:
            clothes = clothes_response.json()
 
        result = {
            'books': books if book_response.status_code == 200 else [],
            'mobiles': mobiles if mobile_response.status_code == 200 else [],
            'clothes': clothes if clothes_response.status_code == 200 else []
        }
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'error': 'Không có từ khóa tìm kiếm được cung cấp.'}, status=400)
