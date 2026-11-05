```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه برای مدیریت و تحلیل داده‌های مرتبط با محصولات سوزن‌دوزی، 
سفارشات و مدیریت موجودی هنری طراحی شده است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات و داده‌های سوزن‌زرین."""

    def __init__(self) -> None:
        self.inventory: Dict[str, Dict[str, Union[int, float]]] = {}
        self.orders: List[Dict] = []

    def add_product(self, name: str, price: float, quantity: int) -> None:
        """
        افزودن محصول جدید به موجودی سوزن‌زرین.

        :param name: نام طرح یا محصول
        :param price: قیمت محصول به تومان
        :param quantity: تعداد موجودی
        """
        self.inventory[name] = {"price": price, "quantity": quantity}

    def register_order(self, customer_name: str, items: List[str]) -> Optional[str]:
        """
        ثبت سفارش جدید برای مشتری.

        :param customer_name: نام مشتری
        :param items: لیست نام محصولات خریداری شده
        :return: شناسه سفارش یا پیام خطا
        """
        total_price = 0.0
        for item in items:
            if item in self.inventory and self.inventory[item]["quantity"] > 0:
                total_price += self.inventory[item]["price"]
                self.inventory[item]["quantity"] -= 1
            else:
                return f"خطا: محصول {item} ناموجود است."

        order_id = f"ZZ-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.orders.append({
            "id": order_id,
            "customer": customer_name,
            "items": items,
            "total": total_price,
            "date": datetime.now().isoformat()
        })
        return order_id

    def get_inventory_report(self) -> str:
        """
        دریافت گزارش وضعیت موجودی محصولات.

        :return: رشته شامل جزئیات موجودی
        """
        report = ["گزارش موجودی سوزن‌زرین:"]
        for name, info in self.inventory.items():
            report.append(f"- {name}: {info['quantity']} عدد | قیمت: {info['price']} تومان")
        return "\n".join(report)

    def calculate_total_revenue(self) -> float:
        """
        محاسبه مجموع درآمد حاصل از سفارشات ثبت شده.

        :return: مجموع درآمد
        """
        return sum(order["total"] for order in self.orders)

    def get_customer_history(self, customer_name: str) -> List[Dict]:
        """
        دریافت تاریخچه خرید یک مشتری خاص.

        :param customer_name: نام مشتری
        :return: لیست سفارشات مشتری
        """
        return [order for order in self.orders if order["customer"] == customer_name]


# مثال استفاده از پکیج
if __name__ == "__main__":
    zarin = SozaneZarinManager()
    
    # افزودن محصولات نمونه
    zarin.add_product("سوزن‌دوزی سنتی طرح گل", 450000.0, 10)
    zarin.add_product("رومیزی شماره‌دوزی", 850000.0, 5)
    
    # ثبت یک سفارش
    order_id = zarin.register_order("مریم محمدی", ["سوزن‌دوزی سنتی طرح گل"])
    
    print(f"سفارش با موفقیت ثبت شد: {order_id}")
    print(zarin.get_inventory_report())
    print(f"مجموع درآمد: {zarin.calculate_total_revenue()} تومان")
```