```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزاری برای مدیریت، تحلیل و پردازش سفارشات، محصولات و 
اطلاعات مرتبط با برند "سوزن زرین" است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات‌های فروشگاه سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: List[Dict] = []
        self.orders: List[Dict] = []

    def add_product(self, name: str, price: float, category: str) -> None:
        """
        افزودن محصول جدید به موجودی سوزن زرین.
        
        :param name: نام محصول (مثلا: گلدوزی دستی)
        :param price: قیمت محصول به تومان
        :param category: دسته‌بندی محصول
        """
        product = {
            "name": name,
            "price": price,
            "category": category,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)

    def calculate_total_revenue(self) -> float:
        """
        محاسبه کل درآمد حاصل از سفارشات ثبت شده.
        
        :return: مجموع مبالغ سفارشات به صورت عدد اعشاری
        """
        return sum(order['price'] for order in self.orders)

    def register_order(self, customer_name: str, product_name: str, price: float) -> str:
        """
        ثبت یک سفارش جدید برای مشتری.
        
        :param customer_name: نام مشتری
        :param product_name: نام محصول خریداری شده
        :param price: قیمت نهایی
        :return: کد پیگیری سفارش
        """
        order_id = f"ZZ-{len(self.orders) + 1001}"
        order = {
            "order_id": order_id,
            "customer": customer_name,
            "product": product_name,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.orders.append(order)
        return order_id

    def get_inventory_report(self) -> List[str]:
        """
        دریافت گزارش متنی از محصولات موجود.
        
        :return: لیستی از نام محصولات موجود
        """
        return [item['name'] for item in self.inventory]

    def find_product_by_category(self, category: str) -> List[Dict]:
        """
        جستجوی محصولات بر اساس دسته‌بندی خاص.
        
        :param category: دسته‌بندی مورد نظر
        :return: لیست دیکشنری‌های محصولات مطابق با دسته‌بندی
        """
        return [item for item in self.inventory if item['category'] == category]


# مثال استفاده از کتابخانه
if __name__ == "__main__":
    # راه‌اندازی سیستم
    zarin_shop = SozaneZarinManager()

    # افزودن محصولات نمونه
    zarin_shop.add_product("سوزن‌دوزی بلوچی", 450000.0, "صنایع دستی")
    zarin_shop.add_product("کیف گلدوزی شده", 280000.0, "اکسسوری")

    # ثبت سفارش
    order_id = zarin_shop.register_order("مریم", "سوزن‌دوزی بلوچی", 450000.0)
    
    print(f"سفارش با موفقیت ثبت شد. کد پیگیری: {order_id}")
    print(f"موجودی فعلی: {zarin_shop.get_inventory_report()}")
    print(f"مجموع درآمد: {zarin_shop.calculate_total_revenue()} تومان")
```