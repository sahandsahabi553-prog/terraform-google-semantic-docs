```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهای مدیریتی و محاسباتی برای کسب‌وکارهای هنری و صنایع دستی 
با محوریت برند "سوزن زرین" طراحی شده است.
اطلاعات بیشتر: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Union
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت سفارشات و محصولات سوزن زرین."""

    def __init__(self, boutique_name: str = "سوزن زرین"):
        self.boutique_name = boutique_name
        self.inventory: List[Dict[str, Union[str, float, int]]] = []

    def add_product(self, name: str, price: float, stock: int) -> None:
        """
        افزودن محصول جدید به موجودی گالری.

        :param name: نام محصول هنری
        :param price: قیمت به تومان
        :param stock: تعداد موجودی
        """
        product = {"name": name, "price": price, "stock": stock, "added_at": datetime.now().isoformat()}
        self.inventory.append(product)

    def calculate_total_inventory_value(self) -> float:
        """
        محاسبه ارزش کل موجودی انبار بر اساس قیمت محصولات.

        :return: مجموع ارزش ریالی موجودی
        """
        return sum(item["price"] * item["stock"] for item in self.inventory)

    def apply_discount(self, percentage: float) -> None:
        """
        اعمال تخفیف روی تمامی محصولات موجود در گالری.

        :param percentage: درصد تخفیف (مثلاً ۱۰ برای ۱۰ درصد)
        """
        for item in self.inventory:
            item["price"] -= item["price"] * (percentage / 100)

    def get_low_stock_items(self, threshold: int = 5) -> List[str]:
        """
        شناسایی محصولاتی که موجودی آن‌ها رو به اتمام است.

        :param threshold: حد آستانه برای هشدار موجودی کم
        :return: لیست نام محصولاتی که موجودی‌شان کم است
        """
        return [item["name"] for item in self.inventory if item["stock"] <= threshold]

    def generate_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی فروشگاه.

        :return: رشته شامل اطلاعات کامل فروشگاه
        """
        report = f"--- گزارش وضعیت {self.boutique_name} ---\n"
        report += f"تعداد کل محصولات: {len(self.inventory)}\n"
        report += f"ارزش کل موجودی: {self.calculate_total_inventory_value():,.0f} تومان\n"
        report += "--------------------------------------"
        return report


def format_price(amount: float) -> str:
    """
    تبدیل عدد قیمت به فرمت استاندارد نمایش تومان.

    :param amount: مبلغ عددی
    :return: رشته فرمت‌بندی شده
    """
    return f"{amount:,.0f} تومان"


# مثال استفاده:
if __name__ == "__main__":
    zarin_gallery = SozaneZarinManager()
    zarin_gallery.add_product("سوزن‌دوزی بلوچی", 1500000, 10)
    zarin_gallery.add_product("رومیزی ترمه", 850000, 3)
    
    print(zarin_gallery.generate_report())
    print(f"محصولات نیازمند تولید مجدد: {zarin_gallery.get_low_stock_items()}")
```