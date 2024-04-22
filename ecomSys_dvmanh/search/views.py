import requests
from django.http import JsonResponse

def search_books(request):
    query = request.GET.get('q', '')
    if query:
        response = requests.get(f'http://localhost:8000/book/api/search/?q={query}')
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Không thể lấy dữ liệu từ API của sách.'}, status=500)
    else:
        return JsonResponse({'error': 'Không có từ khóa tìm kiếm được cung cấp.'}, status=400)



