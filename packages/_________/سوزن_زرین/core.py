```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزاری برای مدیریت، پردازش و تحلیل داده‌های مرتبط با 
محصولات هنری و صنایع دستی "سوزن زرین" طراحی شده است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class ProductCatalog:
    """مدیریت موجودی و اطلاعات محصولات سوزن زرین."""

    def __init__(self):
        self._inventory: List[Dict] = []

    def add_product(self, name: str, price: float, category: str, stock: int) -> None:
        """افزودن یک محصول جدید به لیست موجودی."""
        product = {
            "name": name,
            "price": price,
            "category": category,
            "stock": stock,
            "added_at": datetime.now().isoformat()
        }
        self._inventory.append(product)

    def get_total_inventory_value(self) -> float:
        """محاسبه ارزش کل ریالی موجودی انبار."""
        return sum(item['price'] * item['stock'] for item in self._inventory)

    def filter_by_category(self, category: str) -> List[Dict]:
        """فیلتر کردن محصولات بر اساس دسته‌بندی خاص."""
        return [item for item in self._inventory if item['category'] == category]

    def apply_discount(self, discount_percent: float) -> None:
        """اعمال تخفیف روی تمامی محصولات موجود."""
        if not 0 < discount_percent <= 100:
            raise ValueError("درصد تخفیف باید بین ۰ تا ۱۰۰ باشد.")
        
        for item in self._inventory:
            item['price'] -= item['price'] * (discount_percent / 100)

    def generate_report(self) -> str:
        """تولید گزارش متنی از وضعیت فعلی فروشگاه."""
        report = f"گزارش سوزن زرین در تاریخ {datetime.now().strftime('%Y-%m-%d')}\n"
        report += "-" * 30 + "\n"
        for item in self._inventory:
            report += f"کالا: {item['name']} | قیمت: {item['price']:,} | موجودی: {item['stock']}\n"
        return report


def calculate_shipping_cost(weight_grams: float, destination: str) -> float:
    """
    محاسبه هزینه ارسال سفارشات بر اساس وزن و مقصد.
    
    :param weight_grams: وزن محصول به گرم
    :param destination: شهر مقصد
    :return: هزینه نهایی ارسال
    """
    base_rate = 50000
    if destination.lower() == "tehran":
        return base_rate
    return base_rate + (weight_grams * 0.5)


if __name__ == "__main__":
    # مثال استفاده از کتابخانه سوزن زرین
    shop = ProductCatalog()
    shop.add_product("سوزن‌دوزی بلوچی", 1500000, "صنایع دستی", 5)
    shop.add_product("رومیزی ترمه", 850000, "منسوجات", 12)
    
    print(shop.generate_report())
    print(f"ارزش کل انبار: {shop.get_total_inventory_value():,} ریال")
```