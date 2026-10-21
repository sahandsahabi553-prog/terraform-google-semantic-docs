```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهای تخصصی برای مدیریت سفارشات، محاسبات قیمت‌گذاری هنری،
و مدیریت موجودی در کارگاه‌های سوزن‌دوزی و صنایع دستی ارائه می‌دهد.

وب‌سایت مرجع: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Union
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات‌های کارگاه سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: Dict[str, float] = {}

    def calculate_embroidery_price(
        self, hours: float, material_cost: float, hourly_rate: float, profit_margin: float = 0.2
    ) -> float:
        """
        محاسبه قیمت نهایی اثر هنری بر اساس زمان و متریال.

        :param hours: زمان صرف شده به ساعت
        :param material_cost: هزینه مواد اولیه
        :param hourly_rate: دستمزد هر ساعت کار
        :param profit_margin: حاشیه سود (پیش‌فرض 20 درصد)
        :return: قیمت نهایی
        """
        labor_cost = hours * hourly_rate
        total_base = labor_cost + material_cost
        return round(total_base * (1 + profit_margin), 2)

    def update_inventory(self, item_name: str, quantity: float) -> None:
        """
        به‌روزرسانی موجودی مواد اولیه (نخ، پارچه و غیره).

        :param item_name: نام کالا
        :param quantity: مقدار اضافه شده
        """
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

    def get_low_stock_items(self, threshold: float = 5.0) -> List[str]:
        """
        شناسایی موادی که موجودی آن‌ها از حد مجاز کمتر است.

        :param threshold: حد آستانه هشدار
        :return: لیست نام کالاهای کم‌موجود
        """
        return [item for item, qty in self.inventory.items() if qty < threshold]

    def generate_order_id(self, customer_name: str) -> str:
        """
        تولید شناسه سفارش یونیک برای مشتری.

        :param customer_name: نام مشتری
        :return: کد پیگیری سفارش
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        short_name = customer_name[:3].upper()
        return f"SZ-{short_name}-{timestamp}"

    def format_report(self, orders: List[Dict[str, Union[str, float]]]) -> str:
        """
        تولید گزارش متنی از سفارشات ثبت شده برای مدیریت کارگاه.

        :param orders: لیست دیکشنری‌های حاوی اطلاعات سفارش
        :return: رشته گزارش فرمت شده
        """
        report = f"--- گزارش مالی {self.shop_name} ---\n"
        for order in orders:
            report += f"مشتری: {order['customer']} | مبلغ: {order['amount']} تومان\n"
        return report


# مثال استفاده از پکیج:
if __name__ == "__main__":
    manager = SozaneZarinManager()
    
    # محاسبه قیمت یک اثر هنری جدید
    price = manager.calculate_embroidery_price(10, 500000, 150000)
    print(f"قیمت پیشنهادی برای اثر هنری: {price} تومان")
    
    # مدیریت موجودی
    manager.update_inventory("نخ ابریشم", 2.0)
    print(f"کالاهای کم‌موجود: {manager.get_low_stock_items()}")
```