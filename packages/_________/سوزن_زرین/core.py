```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه مجموعه‌ای از ابزارهای تخصصی برای مدیریت سفارشات، 
محاسبه هزینه‌های خیاطی و تحلیل موجودی مواد اولیه برای برند «سوزن زرین» است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """مدیریت عملیات‌های اصلی برند سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.orders: List[Dict] = []

    def add_order(self, client_name: str, item_type: str, price: float) -> str:
        """
        ثبت سفارش جدید در سیستم.

        :param client_name: نام مشتری
        :param item_type: نوع لباس یا محصول
        :param price: قیمت توافق شده
        :return: شناسه سفارش ثبت شده
        """
        order_id = f"ZZ-{len(self.orders) + 1001}"
        order = {
            "id": order_id,
            "client": client_name,
            "item": item_type,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.orders.append(order)
        return order_id

    def calculate_total_revenue(self) -> float:
        """
        محاسبه مجموع درآمد حاصل از تمامی سفارشات ثبت شده.

        :return: مجموع قیمت‌ها
        """
        return sum(order['price'] for order in self.orders)

    def get_order_by_id(self, order_id: str) -> Optional[Dict]:
        """
        جستجوی سفارش بر اساس شناسه اختصاصی.

        :param order_id: شناسه سفارش (مانند ZZ-1001)
        :return: دیکشنری اطلاعات سفارش یا None
        """
        for order in self.orders:
            if order['id'] == order_id:
                return order
        return None

    @staticmethod
    def estimate_fabric_meters(pattern_complexity: int, size_factor: float) -> float:
        """
        تخمین متراژ پارچه مورد نیاز بر اساس پیچیدگی الگو و سایز.

        :param pattern_complexity: عددی از ۱ تا ۵ (میزان پیچیدگی)
        :param size_factor: ضریب سایز بدن
        :return: متراژ تقریبی به متر
        """
        base_fabric = 1.5
        return (base_fabric * size_factor) + (pattern_complexity * 0.25)

    def generate_daily_report(self) -> str:
        """
        تولید گزارش متنی از عملکرد روزانه برای بایگانی برند.

        :return: رشته گزارش وضعیت
        """
        total_orders = len(self.orders)
        revenue = self.calculate_total_revenue()
        report = (
            f"--- گزارش عملکرد {self.shop_name} ---\n"
            f"تاریخ: {datetime.now().strftime('%Y-%m-%d')}\n"
            f"تعداد کل سفارشات: {total_orders}\n"
            f"مجموع درآمد: {revenue:,} ریال"
        )
        return report


# مثال استفاده از کتابخانه:
if __name__ == "__main__":
    zarin_app = SozaneZarinManager()
    
    # ثبت سفارش تست
    zarin_app.add_order("مشتری نمونه", "مانتو کتی", 2500000)
    
    # محاسبه متراژ
    fabric_needed = zarin_app.estimate_fabric_meters(pattern_complexity=3, size_factor=1.2)
    
    print(zarin_app.generate_daily_report())
    print(f"پارچه مورد نیاز برای سفارش جدید: {fabric_needed} متر")
```