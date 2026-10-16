```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه برای مدیریت و بهینه‌سازی فرآیندهای هنری، خیاطی و 
مدیریت موجودی کارگاه‌های هنری "سوزن زرین" طراحی شده است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
import math


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات و محاسبات کارگاه سوزن زرین."""

    def __init__(self, workshop_name: str = "سوزن زرین"):
        self.workshop_name = workshop_name
        self.inventory: Dict[str, float] = {}

    def calculate_fabric_requirement(self, length: float, width: float, margin: float = 0.1) -> float:
        """
        محاسبه متراژ پارچه مورد نیاز با در نظر گرفتن حاشیه اطمینان.

        :param length: طول طرح (متر)
        :param width: عرض طرح (متر)
        :param margin: درصد حاشیه اطمینان (پیش‌فرض ۱۰٪)
        :return: متراژ کل مورد نیاز
        """
        area = length * width
        return round(area * (1 + margin), 2)

    def estimate_thread_usage(self, complexity_score: int, hours: float) -> float:
        """
        تخمین میزان نخ مورد نیاز بر اساس پیچیدگی طرح و زمان صرف شده.

        :param complexity_score: امتیاز پیچیدگی از ۱ تا ۱۰
        :param hours: زمان صرف شده برای گلدوزی
        :return: مقدار تخمینی نخ به متر
        """
        base_rate = 5.5  # متر بر ساعت
        return round(base_rate * complexity_score * hours, 2)

    def update_inventory(self, item_name: str, quantity: float) -> None:
        """
        به‌روزرسانی موجودی انبار کارگاه.

        :param item_name: نام کالا (نخ، پارچه، سوزن و غیره)
        :param quantity: مقدار اضافه یا کم شده
        """
        self.inventory[item_name] = self.inventory.get(item_name, 0.0) + quantity

    def get_inventory_report(self) -> Dict[str, float]:
        """
        دریافت گزارش کامل موجودی فعلی.

        :return: دیکشنری شامل نام اقلام و مقادیر آن‌ها
        """
        return self.inventory

    def pricing_calculator(self, material_cost: float, labor_hours: float, hourly_rate: float) -> float:
        """
        محاسبه قیمت نهایی اثر هنری بر اساس هزینه مواد و دستمزد.

        :param material_cost: هزینه مواد اولیه
        :param labor_hours: تعداد ساعات کاری
        :param hourly_rate: نرخ دستمزد ساعتی
        :return: قیمت نهایی پیشنهادی
        """
        profit_margin = 0.2  # ۲۰ درصد حاشیه سود کارگاه
        total_cost = material_cost + (labor_hours * hourly_rate)
        return round(total_cost * (1 + profit_margin), 2)


# نمونه استفاده از کتابخانه
if __name__ == "__main__":
    # مقداردهی اولیه
    zarin_app = SozaneZarinManager()

    # مثال ۱: محاسبه پارچه برای یک سفارش خاص
    fabric_needed = zarin_app.calculate_fabric_requirement(1.5, 2.0)
    print(f"پارچه مورد نیاز: {fabric_needed} متر مربع")

    # مثال ۲: محاسبه قیمت نهایی
    final_price = zarin_app.pricing_calculator(500000, 10, 150000)
    print(f"قیمت نهایی اثر هنری: {final_price} ریال")

    # مثال ۳: مدیریت انبار
    zarin_app.update_inventory("نخ ابریشم", 50)
    zarin_app.update_inventory("سوزن شماره ۵", 10)
    print(f"موجودی فعلی: {zarin_app.get_inventory_report()}")
```