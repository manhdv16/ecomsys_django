from django.http import JsonResponse
import requests

def process_payment(request):
    payment_data = request.POST.get('payment_data')
    
    payment_response = requests.post('http://payment-service-url.com/process-payment', 
    data=payment_data)
    
    # Xử lý và trả về kết quả cho người dùng
    if payment_response.status_code == 200:
        return JsonResponse({'message': 'Payment processed successfully'})
    else:
        return JsonResponse({'message': 'Payment failed'})
