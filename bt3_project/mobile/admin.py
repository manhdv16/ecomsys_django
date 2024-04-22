from django.contrib import admin
from .models import Brand, Mobile

# Đăng ký model Brand
admin.site.register(Brand)

# Đăng ký model Mobile
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'price')  # Hiển thị các trường trong danh sách
    search_fields = ('model_name', 'brand__name')    # Cho phép tìm kiếm theo tên và thương hiệu
