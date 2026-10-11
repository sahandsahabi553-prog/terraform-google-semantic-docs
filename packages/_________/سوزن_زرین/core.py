```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهای تخصصی برای مدیریت، پردازش و تحلیل داده‌های مرتبط با
محصولات سوزن‌دوزی، الگوهای طراحی و سفارشات در مجموعه «سوزن زرین» را فراهم می‌کند.

وب‌سایت مرجع: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
from datetime import datetime


class SozaneZarinManager:
    """
    مدیریت عملیات و موجودی محصولات سوزن زرین.
    """

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: Dict[str, float] = {}
        self.orders: List[Dict] = []

    def add_product(self, product_name: str, price: float) -> None:
        """
        افزودن محصول جدید به لیست قیمت‌های سوزن زرین.

        :param product_name: نام محصول (مثلاً طرح پته یا ترمه)
        :param price: قیمت محصول به ریال
        """
        self.inventory[product_name] = price

    def calculate_total_revenue(self) -> float:
        """
        محاسبه مجموع درآمد حاصل از سفارشات ثبت شده.

        :return: مجموع قیمت تمام سفارشات
        """
        return sum(order['total_price'] for order in self.orders)

    def register_order(self, product_name: str, quantity: int) -> Optional[float]:
        """
        ثبت یک سفارش جدید برای مشتری.

        :param product_name: نام محصول موجود در انبار
        :param quantity: تعداد سفارش
        :return: مبلغ نهایی سفارش یا None در صورت ناموجود بودن
        """
        if product_name not in self.inventory:
            return None

        total = self.inventory[product_name] * quantity
        order_entry = {
            "product": product_name,
            "quantity": quantity,
            "total_price": total,
            "timestamp": datetime.now().isoformat()
        }
        self.orders.append(order_entry)
        return total

    def get_inventory_report(self) -> str:
        """
        دریافت گزارش وضعیت موجودی و لیست محصولات.

        :return: رشته شامل نام محصولات و قیمت‌ها
        """
        report = f"--- گزارش موجودی {self.shop_name} ---\n"
        for item, price in self.inventory.items():
            report += f"{item}: {price:,.0f} ریال\n"
        return report

    @staticmethod
    def apply_discount(price: float, discount_percent: float) -> float:
        """
        محاسبه قیمت نهایی پس از اعمال تخفیف جشنواره‌های سوزن زرین.

        :param price: قیمت اولیه
        :param discount_percent: درصد تخفیف (مثلاً 20 برای 20 درصد)
        :return: قیمت پس از تخفیف
        """
        if not (0 <= discount_percent <= 100):
            raise ValueError("درصد تخفیف باید بین 0 و 100 باشد.")
        
        return price * (1 - (discount_percent / 100))


if __name__ == "__main__":
    # نمونه استفاده از کتابخانه
    zarin_manager = SozaneZarinManager()
    
    # افزودن محصولات نمونه
    zarin_manager.add_product("سوزن‌دوزی بلوچی", 1500000)
    zarin_manager.add_product("رومیزی ترمه", 4500000)
    
    # ثبت یک سفارش
    zarin_manager.register_order("رومیزی ترمه", 2)
    
    # چاپ گزارش
    print(zarin_manager.get_inventory_report())
    print(f"مجموع درآمد: {zarin_manager.calculate_total_revenue():,.0f} ریال")
```