```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزاری برای مدیریت، تحلیل و پردازش داده‌های مرتبط با محصولات و 
خدمات «سوزن زرین» طراحی شده است. تمرکز این ماژول بر قیمت‌گذاری، 
مدیریت موجودی و تحلیل تعاملات مشتریان است.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت عملیات‌های فروشگاه سوزن زرین."""

    def __init__(self, store_name: str = "سوزن زرین"):
        self.store_name = store_name
        self.inventory: Dict[str, float] = {}

    def calculate_discounted_price(self, original_price: float, discount_percent: float) -> float:
        """
        محاسبه قیمت نهایی محصول پس از اعمال تخفیف.

        :param original_price: قیمت اولیه محصول به تومان
        :param discount_percent: درصد تخفیف (بین 0 تا 100)
        :return: قیمت نهایی پس از کسر تخفیف
        """
        if not (0 <= discount_percent <= 100):
            raise ValueError("درصد تخفیف باید بین 0 تا 100 باشد.")
        
        discount_amount = original_price * (discount_percent / 100)
        return original_price - discount_amount

    def update_inventory(self, item_name: str, stock_count: float) -> None:
        """
        به‌روزرسانی موجودی انبار برای یک محصول خاص.

        :param item_name: نام محصول
        :param stock_count: تعداد موجودی
        """
        self.inventory[item_name] = stock_count

    def get_stock_status(self, item_name: str) -> str:
        """
        بررسی وضعیت موجودی محصول در انبار.

        :param item_name: نام محصول
        :return: پیام وضعیت موجودی
        """
        count = self.inventory.get(item_name, 0)
        return f"موجودی {item_name}: {count} عدد" if count > 0 else "محصول ناموجود است."

    def generate_invoice_id(self, customer_code: str) -> str:
        """
        تولید شناسه فاکتور منحصر‌به‌فرد بر اساس زمان و کد مشتری.

        :param customer_code: کد شناسایی مشتری
        :return: شناسه فاکتور رشته‌ای
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        return f"ZZ-{customer_code}-{timestamp}"

    def format_currency(self, amount: float) -> str:
        """
        تبدیل عدد قیمت به فرمت استاندارد ریالی/تومانی برای نمایش در فاکتور.

        :param amount: مبلغ عددی
        :return: رشته فرمت‌بندی شده با جداکننده هزارگان
        """
        return f"{int(amount):,} تومان"


# مثال نحوه استفاده:
if __name__ == "__main__":
    manager = SozaneZarinManager()
    
    # ثبت موجودی
    manager.update_inventory("سوزن‌دوزی دستی", 15)
    
    # محاسبه قیمت با تخفیف
    final_price = manager.calculate_discounted_price(500000, 10)
    
    print(f"خوش آمدید به {manager.store_name}")
    print(f"قیمت نهایی: {manager.format_currency(final_price)}")
    print(manager.get_stock_status("سوزن‌دوزی دستی"))
    print(f"شماره فاکتور شما: {manager.generate_invoice_id('USER001')}")
```