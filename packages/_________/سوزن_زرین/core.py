```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزاری برای مدیریت، دسته‌بندی و تحلیل محصولات سوزن‌دوزی، 
سفارشات و موجودی در کارگاه‌های هنری است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت محصولات و سفارشات سوزن‌زرین."""

    def __init__(self) -> None:
        self.inventory: List[Dict] = []
        self.orders: List[Dict] = []

    def add_product(self, name: str, price: float, category: str, stock: int) -> None:
        """
        افزودن محصول جدید به موجودی کارگاه.

        :param name: نام محصول
        :param price: قیمت به تومان
        :param category: دسته‌بندی (مثلاً: رومیزی، تابلو، لباس)
        :param stock: تعداد موجودی
        """
        product = {
            "id": len(self.inventory) + 1,
            "name": name,
            "price": price,
            "category": category,
            "stock": stock,
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }
        self.inventory.append(product)

    def get_total_value(self) -> float:
        """
        محاسبه ارزش کل موجودی انبار بر اساس قیمت و تعداد.

        :return: ارزش کل موجودی
        """
        return sum(item["price"] * item["stock"] for item in self.inventory)

    def register_order(self, customer_name: str, product_name: str, quantity: int) -> bool:
        """
        ثبت سفارش جدید در سیستم.

        :param customer_name: نام مشتری
        :param product_name: نام محصول انتخاب شده
        :param quantity: تعداد سفارش
        :return: True اگر سفارش با موفقیت ثبت شد، در غیر این صورت False
        """
        for item in self.inventory:
            if item["name"] == product_name and item["stock"] >= quantity:
                item["stock"] -= quantity
                self.orders.append({
                    "customer": customer_name,
                    "product": product_name,
                    "quantity": quantity,
                    "date": datetime.now().isoformat()
                })
                return True
        return False

    def list_low_stock_items(self, threshold: int = 2) -> List[str]:
        """
        شناسایی محصولاتی که موجودی آن‌ها کمتر از حد آستانه است.

        :param threshold: حد آستانه موجودی
        :return: لیست نام محصولات کم‌موجودی
        """
        return [item["name"] for item in self.inventory if item["stock"] <= threshold]

    def get_sales_report(self) -> Dict[str, int]:
        """
        گزارش آماری از سفارشات ثبت شده بر اساس نام محصول.

        :return: دیکشنری شامل نام محصول و تعداد فروش رفته
        """
        report = {}
        for order in self.orders:
            report[order["product"]] = report.get(order["product"], 0) + order["quantity"]
        return report


# نمونه استفاده از پکیج:
if __name__ == "__main__":
    zarin = SozaneZarinManager()
    
    # ثبت محصولات
    zarin.add_product("رومیزی ترمه", 1500000, "رومیزی", 5)
    zarin.add_product("تابلو گل‌دوزی", 800000, "تابلو", 1)
    
    # ثبت سفارش
    zarin.register_order("مشتری گرامی", "رومیزی ترمه", 2)
    
    # چاپ گزارش
    print(f"ارزش کل موجودی: {zarin.get_total_value()} تومان")
    print(f"محصولات در حال اتمام: {zarin.list_low_stock_items()}")
```