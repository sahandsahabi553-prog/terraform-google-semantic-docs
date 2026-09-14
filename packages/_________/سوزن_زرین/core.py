```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه برای مدیریت، تحلیل و پردازش داده‌های مرتبط با محصولات 
و خدمات "سوزن زرین" طراحی شده است. 

وب‌سایت مرجع: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت سفارشات و محصولات سوزن زرین."""

    def __init__(self, store_name: str = "سوزن زرین"):
        self.store_name = store_name
        self.inventory: List[Dict[str, Union[str, float]]] = []

    def add_product(self, name: str, price: float, category: str) -> None:
        """
        افزودن محصول جدید به لیست موجودی.

        :param name: نام محصول
        :param price: قیمت محصول به تومان
        :param category: دسته‌بندی محصول (مثلاً گلدوزی، خیاطی و غیره)
        """
        product = {
            "name": name,
            "price": price,
            "category": category,
            "date_added": datetime.now().strftime("%Y-%m-%d")
        }
        self.inventory.append(product)

    def get_total_inventory_value(self) -> float:
        """
        محاسبه ارزش کل موجودی انبار.

        :return: مجموع قیمت تمام محصولات
        """
        return sum(item["price"] for item in self.inventory)

    def filter_by_category(self, category: str) -> List[Dict]:
        """
        فیلتر کردن محصولات بر اساس دسته‌بندی خاص.

        :param category: نام دسته‌بندی مورد نظر
        :return: لیست محصولات موجود در دسته‌بندی
        """
        return [item for item in self.inventory if item["category"] == category]

    def apply_discount(self, discount_percent: float) -> None:
        """
        اعمال تخفیف روی تمامی محصولات موجود.

        :param discount_percent: درصد تخفیف (مثلاً ۱۰ برای ۱۰ درصد)
        """
        for item in self.inventory:
            current_price = float(item["price"])
            item["price"] = current_price * (1 - (discount_percent / 100))

    def generate_catalog_summary(self) -> str:
        """
        تولید خلاصه وضعیت کاتالوگ برای نمایش در گزارش‌ها.

        :return: رشته شامل تعداد کل محصولات و نام برند
        """
        count = len(self.inventory)
        return f"فروشگاه {self.store_name} در حال حاضر {count} محصول فعال دارد."


# مثال استفاده از کتابخانه
if __name__ == "__main__":
    # راه‌اندازی سیستم
    zarin_sys = SozaneZarinManager()

    # ثبت نمونه محصولات
    zarin_sys.add_product("سوزن دوزی سنتی", 150000.0, "گلدوزی")
    zarin_sys.add_product("نخ ابریشم اصل", 45000.0, "ملزومات")
    zarin_sys.add_product("پارچه ترمه", 320000.0, "پارچه")

    # نمایش اطلاعات
    print(zarin_sys.generate_catalog_summary())
    print(f"ارزش کل موجودی: {zarin_sys.get_total_inventory_value():,.0f} تومان")

    # اعمال تخفیف فصلی
    zarin_sys.apply_discount(10)
    print("تخفیف ۱۰ درصدی با موفقیت اعمال شد.")
```