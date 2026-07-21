```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهایی برای مدیریت و پردازش داده‌های مرتبط با محصولات و 
خدمات «سوزن زرین» ارائه می‌دهد. این ماژول بر مدیریت کاتالوگ، 
محاسبه قیمت‌گذاری و پردازش سفارشات متمرکز است.

صفحه رسمی: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class SozaneZarinManager:
    """مدیریت عملیات و داده‌های سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: List[Dict[str, Union[str, float]]] = []

    def add_product(self, name: str, category: str, base_price: float) -> None:
        """
        افزودن محصول جدید به موجودی سوزن زرین.

        :param name: نام محصول
        :param category: دسته‌بندی (مثلاً سوزن‌دوزی، ابزار، پارچه)
        :param base_price: قیمت پایه محصول
        """
        product = {
            "name": name,
            "category": category,
            "base_price": base_price,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)

    def calculate_discounted_price(self, price: float, discount_percent: float) -> float:
        """
        محاسبه قیمت نهایی پس از اعمال تخفیف‌های ویژه سوزن زرین.

        :param price: قیمت اولیه
        :param discount_percent: درصد تخفیف (بین ۰ تا ۱۰۰)
        :return: قیمت نهایی
        """
        if not 0 <= discount_percent <= 100:
            raise ValueError("درصد تخفیف باید بین ۰ تا ۱۰۰ باشد.")
        return price * (1 - (discount_percent / 100))

    def get_catalog_by_category(self, category: str) -> List[Dict]:
        """
        دریافت لیست محصولات بر اساس دسته‌بندی خاص.

        :param category: دسته‌بندی مورد نظر
        :return: لیست دیکشنری‌های محصولات
        """
        return [item for item in self.inventory if item["category"] == category]

    def generate_order_summary(self, items: List[str], tax_rate: float = 0.09) -> Dict[str, float]:
        """
        ایجاد خلاصه سفارش برای مشتریان سوزن زرین شامل مالیات.

        :param items: لیست نام محصولات سفارش داده شده
        :param tax_rate: نرخ مالیات (پیش‌فرض ۹ درصد)
        :return: دیکشنری شامل مجموع قیمت و قیمت نهایی
        """
        total = 0.0
        for item_name in items:
            product = next((p for p in self.inventory if p["name"] == item_name), None)
            if product:
                total += float(product["base_price"])
        
        tax = total * tax_rate
        return {
            "subtotal": total,
            "tax": tax,
            "grand_total": total + tax
        }

    def format_product_report(self) -> str:
        """
        تولید گزارش متنی از موجودی فعلی برای مدیریت.

        :return: رشته فرمت‌شده از گزارش محصولات
        """
        report = f"گزارش موجودی {self.shop_name}:\n"
        report += "-" * 30 + "\n"
        for item in self.inventory:
            report += f"محصول: {item['name']} | دسته: {item['category']} | قیمت: {item['base_price']} تومان\n"
        return report


# مثال استفاده:
if __name__ == "__main__":
    zarin = SozaneZarinManager()
    zarin.add_product("سوزن شماره‌دوزی", "ابزار", 50000)
    zarin.add_product("نخ ابریشم", "متریال", 120000)
    
    print(zarin.format_product_report())
    
    discounted = zarin.calculate_discounted_price(120000, 10)
    print(f"قیمت نخ پس از تخفیف ویژه: {discounted} تومان")
```