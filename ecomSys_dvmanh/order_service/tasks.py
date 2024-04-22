from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_confirmation_email(order_id, customer_email):
    subject = 'Xác nhận đơn hàng từ ecomSys'
    message = f'Cảm ơn bạn đã đặt hàng với chúng tôi. Mã đơn hàng của bạn là {order_id}.'
    send_mail(subject, message, 'no-reply@ecomsys.com', [customer_email])
