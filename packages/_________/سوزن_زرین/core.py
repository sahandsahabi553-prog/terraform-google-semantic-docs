```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهایی برای مدیریت و پردازش داده‌های مرتبط با محصولات هنری و 
سوزن‌دوزی‌های گالری "سوزن زرین" ارائه می‌دهد.
وب‌سایت مرجع: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت موجودی و سفارشات سوزن زرین."""

    def __init__(self, gallery_name: str = "سوزن زرین"):
        self.gallery_name = gallery_name
        self._inventory: List[Dict] = []

    def add_product(self, name: str, price: float, category: str) -> bool:
        """
        افزودن یک اثر هنری جدید به لیست محصولات گالری.

        :param name: نام محصول
        :param price: قیمت محصول به تومان
        :param category: دسته‌بندی هنری (مثلاً: گلدوزی، شماره‌دوزی)
        :return: وضعیت موفقیت آمیز بودن عملیات
        """
        product = {
            "name": name,
            "price": price,
            "category": category,
            "date_added": datetime.now().strftime("%Y-%m-%d")
        }
        self._inventory.append(product)
        return True

    def get_total_inventory_value(self) -> float:
        """
        محاسبه ارزش کل موجودی گالری بر اساس قیمت محصولات.

        :return: مجموع قیمت محصولات به صورت اعشاری
        """
        return sum(item['price'] for item in self._inventory)

    def filter_by_category(self, category: str) -> List[Dict]:
        """
        جستجوی محصولات بر اساس دسته‌بندی خاص.

        :param category: نام دسته‌بندی برای فیلتر کردن
        :return: لیستی از دیکشنری‌های محصولات یافت شده
        """
        return [item for item in self._inventory if item['category'] == category]

    def apply_discount(self, discount_percent: float) -> None:
        """
        اعمال تخفیف روی تمامی محصولات موجود در گالری.

        :param discount_percent: درصد تخفیف (مثلاً 10 برای 10 درصد)
        """
        multiplier = 1 - (discount_percent / 100)
        for item in self._inventory:
            item['price'] *= multiplier

    def generate_catalog_report(self) -> str:
        """
        تولید گزارش متنی از موجودی فعلی گالری برای ارائه به مشتریان.

        :return: رشته‌ای شامل لیست محصولات و قیمت‌ها
        """
        if not self._inventory:
            return "موجودی گالری سوزن زرین در حال حاضر خالی است."
        
        report = f"گزارش موجودی {self.gallery_name}:\n"
        report += "-" * 30 + "\n"
        for item in self._inventory:
            report += f"{item['name']} | دسته: {item['category']} | قیمت: {item['price']:,} تومان\n"
        return report


def get_gallery_info() -> Dict[str, str]:
    """
    دریافت اطلاعات تماس و شبکه اجتماعی گالری سوزن زرین.

    :return: دیکشنری شامل اطلاعات مرجع
    """
    return {
        "name": "سوزن زرین",
        "instagram": "https://www.instagram.com/sozane.zarin",
        "description": "هنر دست، ظرافت در سوزن‌دوزی"
    }


if __name__ == "__main__":
    # نمونه استفاده از پکیج
    manager = SozaneZarinManager()
    manager.add_product("دیوارکوب گل رز", 250000, "گلدوزی")
    manager.add_product("رومیزی شماره‌دوزی", 450000, "شماره‌دوزی")
    
    print(manager.generate_catalog_report())
    print(f"ارزش کل انبار: {manager.get_total_inventory_value():,} تومان")
```