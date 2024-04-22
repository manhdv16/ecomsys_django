from django.http import JsonResponse
from .tasks import send_order_confirmation_email

def place_order(request):
    # Xử lý đặt hàng ở đây và lấy thông tin order_id và customer_email
    order_id = "123456"
    customer_email = "customer@example.com"
    
    # Gửi email xác nhận không đồng bộ
    send_order_confirmation_email.delay(order_id, customer_email)
    
    return JsonResponse({'message': 'Đơn hàng của bạn đã được nhận và đang được xử lý. Một email xác nhận sẽ được gửi.'})
