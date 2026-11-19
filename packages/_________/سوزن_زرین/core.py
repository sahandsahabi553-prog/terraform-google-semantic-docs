```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهای تخصصی برای مدیریت، پردازش و تحلیل داده‌های مرتبط با
محصولات سوزن‌دوزی، الگوهای طراحی و موجودی کالاهای هنری فراهم می‌کند.

وب‌سایت رسمی: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

import math
from typing import List, Dict, Union


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات‌های سوزن‌زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name

    def calculate_embroidery_cost(self, fabric_price: float, thread_meterage: float, labor_hours: float) -> float:
        """
        محاسبه هزینه نهایی یک اثر هنری بر اساس مواد اولیه و دستمزد.

        :param fabric_price: قیمت پارچه پایه
        :param thread_meterage: متراژ نخ استفاده شده
        :param labor_hours: ساعات صرف شده برای دوخت
        :return: هزینه نهایی
        """
        thread_cost_per_meter = 1500  # نرخ پیش‌فرض نخ
        labor_rate_per_hour = 50000   # نرخ ساعتی دستمزد
        
        total = fabric_price + (thread_meterage * thread_cost_per_meter) + (labor_hours * labor_rate_per_hour)
        return float(total)

    def estimate_thread_needs(self, design_area_cm2: float, complexity_factor: float) -> float:
        """
        تخمین مقدار نخ مورد نیاز بر اساس مساحت طرح و پیچیدگی دوخت.

        :param design_area_cm2: مساحت طرح به سانتی‌متر مربع
        :param complexity_factor: ضریب پیچیدگی (بین ۱ تا ۵)
        :return: متراژ تقریبی نخ مورد نیاز
        """
        base_density = 2.5
        return round(design_area_cm2 * base_density * complexity_factor, 2)

    def validate_pattern_code(self, code: str) -> bool:
        """
        بررسی اعتبار کد محصول در سیستم بایگانی سوزن‌زرین.
        فرمت استاندارد: SZ-XXXX (مثال: SZ-1024)

        :param code: کد محصول
        :return: True اگر معتبر باشد
        """
        if not code.startswith("SZ-") or len(code) != 7:
            return False
        return code[3:].isdigit()

    def generate_inventory_report(self, items: Dict[str, int]) -> str:
        """
        تولید گزارش موجودی انبار برای اقلام هنری.

        :param items: دیکشنری شامل نام کالا و تعداد
        :return: متن گزارش
        """
        report = f"--- گزارش موجودی {self.shop_name} ---\n"
        for item, qty in items.items():
            status = "موجود" if qty > 0 else "ناموجود"
            report += f"{item}: {qty} عدد ({status})\n"
        return report

    def calculate_shipping_weight(self, items_weight: List[float], packaging_weight: float = 0.2) -> float:
        """
        محاسبه وزن نهایی بسته پستی جهت ارسال سفارشات.

        :param items_weight: لیستی از وزن اقلام سفارش
        :param packaging_weight: وزن بسته‌بندی (پیش‌فرض ۲۰۰ گرم)
        :return: وزن کل به کیلوگرم
        """
        return sum(items_weight) + packaging_weight


# مثال استفاده:
if __name__ == "__main__":
    manager = SozaneZarinManager()
    
    # تست تخمین نخ
    needed = manager.estimate_thread_needs(50.0, 3.5)
    print(f"نخ مورد نیاز: {needed} متر")
    
    # تست اعتبار سنجی
    print(f"اعتبار کد SZ-1234: {manager.validate_pattern_code('SZ-1234')}")
    
    # تست گزارش
    inventory = {"سوزن شماره ۵": 10, "نخ ابریشم": 0}
    print(manager.generate_inventory_report(inventory))
```