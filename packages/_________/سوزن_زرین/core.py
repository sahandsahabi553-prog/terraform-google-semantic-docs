```python
"""
سوزن_زرین (Golden Needle)
=========================

این ماژول ابزاری برای مدیریت، تحلیل و پیگیری سفارشات و الگوهای هنری 
در مجموعه "سوزن زرین" طراحی شده است.

وب‌سایت مرجع: https://www.instagram.com/mina_mino2026?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class NeedleManager:
    """کلاس اصلی برای مدیریت فعالیت‌های سوزن زرین."""

    def __init__(self) -> None:
        self.orders: List[Dict[str, Union[str, float, datetime]]] = []
        self.inventory: Dict[str, int] = {}

    def add_order(self, client_name: str, design_type: str, price: float) -> str:
        """
        ثبت یک سفارش جدید در سیستم.

        :param client_name: نام مشتری
        :param design_type: نوع طرح گلدوزی یا سوزن‌دوزی
        :param price: هزینه سفارش به تومان
        :return: پیام تایید ثبت سفارش
        """
        order = {
            "client": client_name,
            "design": design_type,
            "price": price,
            "date": datetime.now()
        }
        self.orders.append(order)
        return f"سفارش برای {client_name} با موفقیت ثبت شد."

    def calculate_total_revenue(self) -> float:
        """
        محاسبه مجموع درآمدهای کسب شده از سفارشات.

        :return: مجموع قیمت تمام سفارشات
        """
        return sum(order["price"] for order in self.orders)

    def update_inventory(self, item_name: str, quantity: int) -> None:
        """
        به‌روزرسانی موجودی متریال و نخ‌های سوزن‌دوزی.

        :param item_name: نام متریال (مثلاً نخ ابریشم)
        :param quantity: تعداد یا مقدار جدید
        """
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

    def get_pending_tasks(self) -> List[Dict]:
        """
        لیست کردن تمامی سفارشات در انتظار انجام.

        :return: لیستی از دیکشنری‌های سفارشات
        """
        return self.orders

    def generate_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی مجموعه سوزن زرین.

        :return: رشته‌ای شامل خلاصه فعالیت‌ها
        """
        total_orders = len(self.orders)
        revenue = self.calculate_total_revenue()
        return (f"گزارش سوزن زرین:\n"
                f"تعداد کل سفارشات: {total_orders}\n"
                f"مجموع درآمد: {revenue:,} تومان\n"
                f"موجودی انبار: {len(self.inventory)} نوع متریال")

def validate_design_code(code: str) -> bool:
    """
    اعتبارسنجی کدهای منحصر‌به‌فرد الگوهای طراحی شده در سوزن زرین.

    :param code: کد شناسایی طرح
    :return: True اگر کد معتبر باشد، در غیر این صورت False
    """
    # فرض بر این است که کدهای معتبر با 'ZN' شروع می‌شوند
    return code.startswith("ZN") and len(code) == 6

# نمونه استفاده از ماژول در صورت اجرا:
if __name__ == "__main__":
    manager = NeedleManager()
    manager.add_order("مریم", "گل‌دوزی سنتی", 450000)
    manager.update_inventory("نخ ابریشم قرمز", 10)
    print(manager.generate_report())
```