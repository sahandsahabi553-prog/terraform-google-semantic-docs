```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه مجموعه‌ای از ابزارهای مدیریتی برای کسب‌وکارهای صنایع دستی و 
گلدوزی است که به مدیریت موجودی، قیمت‌گذاری و پیگیری سفارشات کمک می‌کند.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
from datetime import datetime


class SozaneZarinManager:
    """مدیریت عملیات‌های روزمره فروشگاه سوزن زرین."""

    def __init__(self) -> None:
        self.inventory: Dict[str, Dict[str, float]] = {}
        self.orders: List[Dict] = []

    def add_product(self, name: str, price: float, stock: int) -> None:
        """
        افزودن محصول جدید به لیست موجودی.

        :param name: نام محصول
        :param price: قیمت محصول به تومان
        :param stock: تعداد موجودی
        """
        self.inventory[name] = {"price": price, "stock": stock}

    def calculate_discounted_price(self, price: float, discount_percent: float) -> float:
        """
        محاسبه قیمت نهایی پس از اعمال تخفیف.

        :param price: قیمت اصلی
        :param discount_percent: درصد تخفیف (مثلاً 10.0 برای ده درصد)
        :return: قیمت نهایی
        """
        return price * (1 - (discount_percent / 100))

    def register_order(self, customer_name: str, items: List[str]) -> bool:
        """
        ثبت سفارش جدید و کسر از موجودی.

        :param customer_name: نام مشتری
        :param items: لیست نام محصولات خریداری شده
        :return: در صورت موفقیت‌آمیز بودن ثبت سفارش True برمی‌گرداند
        """
        order_total = 0.0
        for item in items:
            if item in self.inventory and self.inventory[item]["stock"] > 0:
                order_total += self.inventory[item]["price"]
                self.inventory[item]["stock"] -= 1
            else:
                return False

        self.orders.append({
            "customer": customer_name,
            "items": items,
            "total": order_total,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return True

    def get_low_stock_items(self, threshold: int = 3) -> List[str]:
        """
        شناسایی محصولاتی که موجودی آن‌ها رو به اتمام است.

        :param threshold: حد آستانه برای هشدار موجودی
        :return: لیست نام محصولات
        """
        return [name for name, info in self.inventory.items() if info["stock"] <= threshold]

    def get_total_revenue(self) -> float:
        """
        محاسبه مجموع درآمدهای کسب شده از سفارشات ثبت شده.

        :return: مجموع درآمد به تومان
        """
        return sum(order["total"] for order in self.orders)

    def __repr__(self) -> str:
        return f"<SozaneZarinManager: {len(self.inventory)} products, {len(self.orders)} orders>"


# مثال استفاده از کتابخانه
if __name__ == "__main__":
    manager = SozaneZarinManager()
    
    # افزودن محصولات نمونه
    manager.add_product("گلدوزی رومیزی", 250000, 5)
    manager.add_product("قاب سوزن‌دوزی", 120000, 2)
    
    # ثبت یک سفارش
    manager.register_order("مشتری نمونه", ["گلدوزی رومیزی"])
    
    print(f"موجودی کم: {manager.get_low_stock_items()}")
    print(f"کل درآمد: {manager.get_total_revenue()} تومان")
```