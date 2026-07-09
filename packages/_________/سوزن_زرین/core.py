```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهایی برای مدیریت و پردازش داده‌های مرتبط با محصولات و 
خدمات «سوزن زرین» ارائه می‌دهد. این ماژول بر مدیریت موجودی، قیمت‌گذاری 
و تحلیل سفارشات هنری تمرکز دارد.

وب‌سایت: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات‌های سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: List[Dict[str, Union[str, float, int]]] = []

    def add_product(self, name: str, category: str, price: float, stock: int) -> None:
        """
        افزودن محصول جدید به لیست موجودی سوزن زرین.

        :param name: نام محصول (مثلاً: گلدوزی دست‌دوز)
        :param category: دسته‌بندی هنری
        :param price: قیمت به تومان
        :param stock: تعداد موجودی
        """
        product = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
            "added_at": datetime.now().strftime("%Y-%m-%d")
        }
        self.inventory.append(product)

    def calculate_total_inventory_value(self) -> float:
        """
        محاسبه ارزش کل موجودی انبار بر اساس قیمت‌ها.

        :return: مجموع ارزش ریالی موجودی
        """
        return sum(item["price"] * item["stock"] for item in self.inventory)

    def get_products_by_category(self, category: str) -> List[Dict]:
        """
        جستجوی محصولات بر اساس دسته‌بندی خاص.

        :param category: نام دسته‌بندی
        :return: لیست دیکشنری‌های محصولات یافت شده
        """
        return [item for item in self.inventory if item["category"] == category]

    def apply_discount(self, category: str, percentage: float) -> None:
        """
        اعمال تخفیف روی یک دسته خاص از محصولات سوزن زرین.

        :param category: دسته‌بندی مورد نظر
        :param percentage: درصد تخفیف (مثلاً 10 برای 10 درصد)
        """
        for item in self.inventory:
            if item["category"] == category:
                item["price"] -= item["price"] * (percentage / 100)

    def generate_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی فروشگاه.

        :return: رشته شامل جزئیات گزارش
        """
        report = f"--- گزارش وضعیت {self.shop_name} ---\n"
        report += f"تعداد کل محصولات: {len(self.inventory)}\n"
        report += f"ارزش کل موجودی: {self.calculate_total_inventory_value():,.0f} تومان\n"
        report += "--------------------------------------"
        return report


def format_currency(amount: float) -> str:
    """
    فرمت‌دهی اعداد به صورت استاندارد ریالی/تومانی ایران.

    :param amount: مبلغ عددی
    :return: رشته فرمت شده با جداکننده هزارگان
    """
    return f"{amount:,.0f} تومان"


# مثال استفاده:
if __name__ == "__main__":
    zarin_shop = SozaneZarinManager()
    zarin_shop.add_product("گلدوزی قاب‌دار", "تزئینی", 450000, 5)
    zarin_shop.add_product("سوزن‌دوزی سنتی", "پوشاک", 850000, 2)
    
    print(zarin_shop.generate_report())
```