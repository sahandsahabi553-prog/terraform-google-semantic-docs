```python
"""
سوزن_زرین (Sozane Zarin) Utility Package.

این بسته ابزارهای تخصصی برای مدیریت، تحلیل و سازمان‌دهی داده‌های 
مرتبط با هنرهای دستی و محصولات سوزن‌دوزی ارائه می‌دهد.
اطلاعات بیشتر: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Union
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت موجودی و سفارشات سوزن زرین."""

    def __init__(self):
        self.inventory: Dict[str, Dict[str, Union[str, float, int]]] = {}
        self.orders: List[Dict] = []

    def add_product(self, product_id: str, name: str, price: float, stock: int) -> None:
        """
        افزودن محصول جدید به لیست محصولات سوزن زرین.

        :param product_id: شناسه یکتای محصول
        :param name: نام محصول (مانند سوزن‌دوزی سنتی)
        :param price: قیمت محصول به تومان
        :param stock: تعداد موجودی
        """
        self.inventory[product_id] = {
            "name": name,
            "price": price,
            "stock": stock,
            "added_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

    def get_total_inventory_value(self) -> float:
        """
        محاسبه ارزش کل موجودی انبار بر اساس قیمت و تعداد.

        :return: ارزش کل به صورت عدد اعشاری
        """
        return sum(item["price"] * item["stock"] for item in self.inventory.values())

    def register_order(self, customer_name: str, product_id: str, quantity: int) -> bool:
        """
        ثبت سفارش مشتری جدید در سیستم.

        :param customer_name: نام مشتری
        :param product_id: شناسه محصول انتخابی
        :param quantity: تعداد سفارشی
        :return: در صورت موجود بودن کالا True و در غیر این صورت False
        """
        if product_id in self.inventory and self.inventory[product_id]["stock"] >= quantity:
            self.inventory[product_id]["stock"] -= quantity
            self.orders.append({
                "customer": customer_name,
                "product": self.inventory[product_id]["name"],
                "quantity": quantity,
                "date": datetime.now().isoformat()
            })
            return True
        return False

    def list_low_stock_items(self, threshold: int = 5) -> List[str]:
        """
        شناسایی محصولاتی که موجودی آن‌ها رو به اتمام است.

        :param threshold: حد آستانه برای هشدار موجودی
        :return: لیست نام محصولاتی که موجودی کمی دارند
        """
        return [
            details["name"] for details in self.inventory.values() 
            if details["stock"] < threshold
        ]

    def format_invoice(self, order_index: int) -> str:
        """
        ایجاد متن فاکتور برای یک سفارش خاص.

        :param order_index: ایندکس سفارش در لیست سفارشات
        :return: متن فرمت شده فاکتور
        """
        if 0 <= order_index < len(self.orders):
            order = self.orders[order_index]
            return (f"--- فاکتور سوزن زرین ---\n"
                    f"مشتری: {order['customer']}\n"
                    f"محصول: {order['product']}\n"
                    f"تعداد: {order['quantity']}\n"
                    f"تاریخ: {order['date']}")
        return "سفارش یافت نشد."

# مثال استفاده از پکیج:
if __name__ == "__main__":
    manager = SozaneZarinManager()
    manager.add_product("001", "سوزن‌دوزی طرح گل", 250000.0, 10)
    manager.register_order("مریم", "001", 2)
    
    print(f"ارزش کل موجودی: {manager.get_total_inventory_value()} تومان")
    print(f"فاکتور ثبت شده: \n{manager.format_invoice(0)}")
```