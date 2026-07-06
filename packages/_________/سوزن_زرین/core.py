```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهای تخصصی برای مدیریت و تحلیل سفارشات گلدوزی، 
محاسبه هزینه‌های متریال و مدیریت موجودی برای برند «سوزن زرین» است.

وب‌سایت مرجع: https://www.instagram.com/sozane.zarin
"""

from typing import Dict, List, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات‌های کارگاه سوزن زرین."""

    def __init__(self, workshop_name: str = "سوزن زرین"):
        self.workshop_name = workshop_name
        self.inventory: Dict[str, float] = {}
        self.orders: List[Dict] = []

    def add_material(self, item_name: str, quantity: float) -> None:
        """
        افزودن متریال جدید به موجودی انبار.
        
        :param item_name: نام نخ یا پارچه
        :param quantity: مقدار موجودی به متر یا گرم
        """
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

    def calculate_embroidery_cost(self, hours: float, rate_per_hour: float, material_cost: float) -> float:
        """
        محاسبه هزینه نهایی یک سفارش گلدوزی.
        
        :param hours: زمان صرف شده برای گلدوزی
        :param rate_per_hour: دستمزد ساعتی
        :param material_cost: هزینه متریال مصرفی
        :return: هزینه کل پروژه
        """
        return (hours * rate_per_hour) + material_cost

    def register_order(self, client_name: str, design_type: str, price: float) -> str:
        """
        ثبت یک سفارش جدید در سیستم.
        
        :param client_name: نام مشتری
        :param design_type: نوع طرح گلدوزی
        :param price: مبلغ توافقی
        :return: شناسه سفارش تولید شده
        """
        order_id = f"SZ-{len(self.orders) + 1000}"
        self.orders.append({
            "id": order_id,
            "client": client_name,
            "design": design_type,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        return order_id

    def get_inventory_report(self) -> Dict[str, float]:
        """
        دریافت گزارش وضعیت موجودی فعلی انبار.
        
        :return: دیکشنری شامل لیست متریال و مقادیر آن‌ها
        """
        return self.inventory

    def get_total_revenue(self) -> float:
        """
        محاسبه مجموع درآمدهای کسب شده از سفارشات.
        
        :return: مجموع مبالغ دریافتی
        """
        return sum(order['price'] for order in self.orders)


def format_currency_rial(amount: float) -> str:
    """
    تبدیل عدد به فرمت استاندارد ریالی برای فاکتورها.
    
    :param amount: مبلغ عددی
    :return: رشته فرمت شده ریالی
    """
    return f"{int(amount):,} ریال"


# مثال نحوه استفاده:
if __name__ == "__main__":
    zarin_app = SozaneZarinManager()
    
    # افزودن موجودی
    zarin_app.add_material("نخ ابریشم طلایی", 500)
    
    # ثبت سفارش
    order_id = zarin_app.register_order("مشتری نمونه", "طرح گل رز مینیاتوری", 2500000)
    
    print(f"سفارش با موفقیت ثبت شد: {order_id}")
    print(f"موجودی انبار: {zarin_app.get_inventory_report()}")
    print(f"مجموع درآمد: {format_currency_rial(zarin_app.get_total_revenue())}")
```