from django.contrib import admin
from .models import Stock, UserPlan

# ปรับแต่งตารางรายชื่อหุ้น
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'is_set50') # แสดง 2 คอลัมน์ให้ดูง่าย
    search_fields = ('symbol',) # เพิ่มช่องค้นหาชื่อหุ้น
    list_filter = ('is_set50',) # เพิ่มตัวกรองด้านขวา
    ordering = ('symbol',) # เรียงตามตัวอักษร A-Z

# ปรับแต่งตารางแผนการลงทุนของผู้ใช้
@admin.register(UserPlan)
class UserPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'monthly_investment', 'duration_years', 'target_amount')
    search_fields = ('user__username',) # ค้นหาจากชื่อคนได้
    list_filter = ('duration_years',)