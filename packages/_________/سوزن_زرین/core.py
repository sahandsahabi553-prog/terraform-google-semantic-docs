```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه برای مدیریت و تحلیل داده‌های مرتبط با محصولات سوزن‌دوزی،
سفارشات، و موجودی گالری «سوزن زرین» طراحی شده است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات گالری سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: List[Dict[str, Union[str, float, int]]] = []

    def add_product(self, name: str, price: float, category: str, stock: int) -> bool:
        """
        افزودن یک محصول جدید به موجودی گالری.

        :param name: نام محصول سوزن‌دوزی
        :param price: قیمت به تومان
        :param category: دسته‌بندی محصول (مثلاً رومیزی، تابلو، لباس)
        :param stock: تعداد موجودی
        :return: موفقیت‌آمیز بودن عملیات
        """
        product = {
            "name": name,
            "price": price,
            "category": category,
            "stock": stock,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)
        return True

    def calculate_total_inventory_value(self) -> float:
        """
        محاسبه ارزش کل ریالی موجودی انبار گالری.

        :return: مجموع قیمت تمام محصولات موجود در انبار
        """
        return sum(item["price"] * item["stock"] for item in self.inventory)

    def get_products_by_category(self, category: str) -> List[Dict]:
        """
        جستجوی محصولات بر اساس دسته‌بندی خاص.

        :param category: نام دسته‌بندی برای فیلتر
        :return: لیستی از محصولات منطبق
        """
        return [item for item in self.inventory if item["category"] == category]

    def process_order(self, product_name: str, quantity: int) -> bool:
        """
        ثبت سفارش و کسر از موجودی انبار.

        :param product_name: نام محصول مورد نظر
        :param quantity: تعداد سفارش
        :return: وضعیت ثبت سفارش (True اگر موفق باشد)
        """
        for item in self.inventory:
            if item["name"] == product_name and item["stock"] >= quantity:
                item["stock"] -= quantity
                return True
        return False

    def generate_stock_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی انبار برای مدیریت گالری.

        :return: متن گزارش وضعیت موجودی
        """
        report = f"--- گزارش وضعیت انبار {self.shop_name} ---\n"
        for item in self.inventory:
            report += f"کالا: {item['name']} | موجودی: {item['stock']} | قیمت: {item['price']:,} تومان\n"
        return report


# نمونه استفاده از کتابخانه
if __name__ == "__main__":
    zarin = SozaneZarinManager()
    
    # افزودن نمونه محصولات
    zarin.add_product("رومیزی ترمه دوزی", 1500000, "رومیزی", 5)
    zarin.add_product("قاب سوزن‌دوزی سنتی", 850000, "تابلو", 2)
    
    # چاپ گزارش
    print(zarin.generate_stock_report())
    
    # محاسبه ارزش کل
    total = zarin.calculate_total_inventory_value()
    print(f"ارزش کل موجودی گالری: {total:,} تومان")
```