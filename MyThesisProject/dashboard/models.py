from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    is_set50 = models.BooleanField(default=True)

    def __str__(self):
        return self.symbol

class UserPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_investment = models.DecimalField(max_digits=10, decimal_places=2, default=5000.00)
    
    # --- ฟิลด์ที่เพิ่มใหม่ตามเอกสารข้อ 8.2.3 ---
    duration_years = models.IntegerField(default=10) # ระยะเวลาการลงทุน (ปี)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, default=1000000.00) # เป้าหมายทางการเงิน
    
    selected_stocks = models.TextField(default="ADVANC,AOT,CPALL,KBANK,PTT") 

    def __str__(self):
        return f"Plan of {self.user.username}"