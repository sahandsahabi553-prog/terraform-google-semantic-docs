```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهای تخصصی برای مدیریت، پردازش و تحلیل داده‌های مرتبط با
محصولات سوزن‌دوزی، الگوهای طراحی و موجودی کالاهای هنری فراهم می‌کند.

وب‌سایت مرجع: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class SozaneZarinManager:
    """مدیریت مرکزی موجودی و خدمات سوزن‌زرین."""

    def __init__(self) -> None:
        self.inventory: List[Dict[str, Union[str, float, int]]] = []

    def add_product(self, name: str, category: str, price: float, stock: int) -> bool:
        """
        افزودن محصول جدید به لیست کالاهای سوزن‌زرین.

        Args:
            name: نام محصول
            category: دسته‌بندی (مثلاً: رومیزی، تابلو، لباس)
            price: قیمت به تومان
            stock: تعداد موجودی

        Returns:
            bool: وضعیت موفقیت آمیز بودن عملیات
        """
        product = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)
        return True

    def get_total_value(self) -> float:
        """
        محاسبه ارزش کل موجودی انبار بر اساس قیمت و تعداد.

        Returns:
            float: مجموع ارزش ریالی محصولات
        """
        return sum(item["price"] * item["stock"] for item in self.inventory)

    def search_by_category(self, category: str) -> List[Dict]:
        """
        جستجوی محصولات بر اساس دسته‌بندی خاص.

        Args:
            category: نام دسته‌بندی برای فیلتر کردن

        Returns:
            List[Dict]: لیست محصولات منطبق
        """
        return [item for item in self.inventory if item["category"] == category]

    def apply_discount(self, discount_percent: float) -> None:
        """
        اعمال تخفیف روی تمامی محصولات موجود.

        Args:
            discount_percent: درصد تخفیف (بین 0 تا 100)
        """
        if not 0 <= discount_percent <= 100:
            raise ValueError("درصد تخفیف باید بین 0 تا 100 باشد.")
        
        for item in self.inventory:
            item["price"] *= (1 - discount_percent / 100)

    def generate_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی فروشگاه.

        Returns:
            str: گزارش وضعیت محصولات
        """
        report = f"گزارش موجودی سوزن‌زرین - تاریخ: {datetime.now().strftime('%Y-%m-%d')}\n"
        report += "-" * 40 + "\n"
        for item in self.inventory:
            report += f"کالا: {item['name']} | موجودی: {item['stock']} | قیمت: {item['price']:,} تومان\n"
        return report


def format_currency(amount: float) -> str:
    """
    تبدیل عدد به فرمت پولی استاندارد ایران.

    Args:
        amount: مبلغ عددی

    Returns:
        str: مبلغ فرمت شده با جداکننده
    """
    return f"{int(amount):,} ریال"


if __name__ == "__main__":
    # نمونه استفاده از پکیج
    store = SozaneZarinManager()
    store.add_product("رومیزی ترمه", "رومیزی", 1500000, 5)
    store.add_product("تابلو طرح گل", "تابلو", 2500000, 2)
    
    print(store.generate_report())
    print(f"ارزش کل انبار: {format_currency(store.get_total_value())}")
```