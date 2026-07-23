```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهایی برای مدیریت، قیمت‌گذاری و دسته‌بندی محصولات هنری 
و صنایع دستی مرتبط با برند «سوزن زرین» ارائه می‌دهد.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """مدیریت موجودی و قیمت‌گذاری محصولات سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: List[Dict] = []

    def add_product(self, name: str, price: float, category: str, stock: int) -> None:
        """
        افزودن محصول جدید به لیست محصولات سوزن زرین.

        :param name: نام محصول
        :param price: قیمت محصول به تومان
        :param category: دسته‌بندی (مثلاً: گلدوزی، شماره‌دوزی)
        :param stock: تعداد موجودی
        """
        product = {
            "name": name,
            "price": price,
            "category": category,
            "stock": stock,
            "added_at": datetime.now().strftime("%Y-%m-%d")
        }
        self.inventory.append(product)

    def get_total_inventory_value(self) -> float:
        """
        محاسبه ارزش کل موجودی انبار بر اساس قیمت و تعداد.

        :return: ارزش کل به صورت عدد اعشاری
        """
        return sum(item["price"] * item["stock"] for item in self.inventory)

    def filter_by_category(self, category: str) -> List[Dict]:
        """
        جستجوی محصولات بر اساس دسته‌بندی خاص.

        :param category: نام دسته‌بندی
        :return: لیستی از محصولات منطبق
        """
        return [item for item in self.inventory if item["category"] == category]

    def apply_discount(self, percentage: float) -> None:
        """
        اعمال تخفیف روی تمام محصولات موجود.

        :param percentage: درصد تخفیف (مثلاً 10 برای 10 درصد)
        """
        for item in self.inventory:
            item["price"] -= item["price"] * (percentage / 100)

    def generate_stock_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی انبار.

        :return: رشته‌ای شامل مشخصات محصولات
        """
        report = f"گزارش وضعیت انبار {self.shop_name}:\n"
        report += "-" * 30 + "\n"
        for item in self.inventory:
            report += f"محصول: {item['name']} | موجودی: {item['stock']} | قیمت: {item['price']:,} تومان\n"
        return report


def format_currency(amount: float) -> str:
    """
    فرمت‌دهی اعداد به صورت پول رایج ایران.

    :param amount: مبلغ عددی
    :return: رشته فرمت شده با جداکننده هزارگان
    """
    return f"{int(amount):,} تومان"


# مثال نحوه استفاده:
if __name__ == "__main__":
    manager = SozaneZarinManager()
    manager.add_product("قاب شماره‌دوزی طرح گل", 250000, "شماره‌دوزی", 10)
    manager.add_product("دیوارکوب سنتی", 450000, "گلدوزی", 5)
    
    print(manager.generate_stock_report())
    print(f"ارزش کل انبار: {format_currency(manager.get_total_inventory_value())}")
```