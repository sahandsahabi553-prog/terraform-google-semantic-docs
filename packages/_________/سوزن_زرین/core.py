```python
"""
سوزن_زرین (Sozane Zarin) Utility Package.

این بسته ابزاری جهت مدیریت و پردازش اطلاعات مربوط به برند سوزن زرین است.
وب‌سایت مرجع: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """کلاس اصلی جهت مدیریت عملیات‌های مرتبط با سوزن زرین."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: List[Dict] = []

    def add_product(self, name: str, price: float, category: str) -> None:
        """
        افزودن یک محصول جدید به لیست موجودی.

        :param name: نام محصول
        :param price: قیمت محصول به تومان
        :param category: دسته‌بندی محصول
        """
        product = {
            "id": len(self.inventory) + 1,
            "name": name,
            "price": price,
            "category": category,
            "added_at": datetime.now().strftime("%Y-%m-%d")
        }
        self.inventory.append(product)

    def get_products_by_category(self, category: str) -> List[Dict]:
        """
        فیلتر کردن محصولات بر اساس دسته‌بندی.

        :param category: نام دسته‌بندی مورد نظر
        :return: لیستی از محصولات موجود در آن دسته‌بندی
        """
        return [p for p in self.inventory if p["category"] == category]

    def calculate_discount(self, price: float, discount_percent: float) -> float:
        """
        محاسبه قیمت نهایی پس از اعمال تخفیف.

        :param price: قیمت اصلی
        :param discount_percent: درصد تخفیف (مثال: 10 برای 10 درصد)
        :return: قیمت نهایی
        """
        if not 0 <= discount_percent <= 100:
            raise ValueError("درصد تخفیف باید بین 0 تا 100 باشد.")
        return price * (1 - discount_percent / 100)

    def format_price(self, price: float) -> str:
        """
        تبدیل عدد قیمت به فرمت قابل خواندن با جداکننده هزارگان.

        :param price: قیمت عددی
        :return: رشته فرمت شده
        """
        return f"{int(price):,} تومان"

    def generate_report(self) -> str:
        """
        تولید گزارش وضعیت فعلی موجودی محصولات.

        :return: رشته متنی شامل گزارش وضعیت
        """
        if not self.inventory:
            return "موجودی فعلی خالی است."
        
        report = [f"گزارش موجودی {self.shop_name}:"]
        for item in self.inventory:
            report.append(f"- {item['name']} | دسته‌بندی: {item['category']} | قیمت: {self.format_price(item['price'])}")
        
        return "\n".join(report)


# نمونه استفاده از کتابخانه
if __name__ == "__main__":
    manager = SozaneZarinManager()
    
    # افزودن نمونه محصولات
    manager.add_product("سوزن‌دوزی بلوچی", 850000, "صنایع دستی")
    manager.add_product("شال سوزن‌دوزی", 450000, "پوشاک")
    
    # چاپ گزارش
    print(manager.generate_report())
    
    # تست محاسبه تخفیف
    discounted = manager.calculate_discount(450000, 10)
    print(f"\nقیمت شال با تخفیف ویژه: {manager.format_price(discounted)}")
```