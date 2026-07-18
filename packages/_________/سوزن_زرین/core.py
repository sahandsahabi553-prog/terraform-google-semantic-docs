```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهایی برای مدیریت، ردیابی و پردازش سفارش‌های هنری و 
محصولات سوزن‌دوزی ارائه می‌دهد.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class OrderManager:
    """مدیریت سفارشات سوزن‌دوزی و محصولات سوزن زرین."""

    def __init__(self) -> None:
        self.orders: List[Dict] = []

    def register_order(self, customer_name: str, item_type: str, price: float) -> str:
        """
        ثبت یک سفارش جدید در سیستم سوزن زرین.

        :param customer_name: نام مشتری
        :param item_type: نوع محصول (مثلاً: رومیزی، تابلو، لباس)
        :param price: قیمت محصول به تومان
        :return: شناسه سفارش ایجاد شده
        """
        order_id = f"SZ-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        order = {
            "id": order_id,
            "customer": customer_name,
            "item": item_type,
            "price": price,
            "status": "Pending"
        }
        self.orders.append(order)
        return order_id

    def calculate_total_revenue(self) -> float:
        """
        محاسبه کل درآمد حاصل از سفارشات ثبت شده.

        :return: مجموع قیمت سفارشات
        """
        return sum(order["price"] for order in self.orders)

    def update_order_status(self, order_id: str, new_status: str) -> bool:
        """
        به‌روزرسانی وضعیت تولید یک سفارش خاص.

        :param order_id: شناسه سفارش
        :param new_status: وضعیت جدید (مثلاً: آماده، در حال دوخت، ارسال شد)
        :return: True در صورت موفقیت، False در صورت یافت نشدن سفارش
        """
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = new_status
                return True
        return False

    def get_pending_orders(self) -> List[Dict]:
        """
        دریافت لیستی از سفارشاتی که هنوز تکمیل نشده‌اند.

        :return: لیست دیکشنری‌های سفارشات در انتظار
        """
        return [order for order in self.orders if order["status"] != "Completed"]

    def generate_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی کسب‌وکار سوزن زرین.

        :return: رشته شامل جزئیات گزارش
        """
        report = f"--- گزارش وضعیت سوزن زرین ---\n"
        report += f"تعداد سفارشات کل: {len(self.orders)}\n"
        report += f"مجموع درآمد پیش‌بینی شده: {self.calculate_total_revenue():,.0f} تومان\n"
        return report


def get_official_instagram() -> str:
    """
    بازگرداندن لینک صفحه رسمی سوزن زرین.

    :return: آدرس اینستاگرام
    """
    return "https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ=="


if __name__ == "__main__":
    # مثال استفاده از ابزار
    manager = OrderManager()
    manager.register_order("مشتری نمونه", "رومیزی ترمه", 1500000)
    print(manager.generate_report())
    print(f"منبع: {get_official_instagram()}")
```