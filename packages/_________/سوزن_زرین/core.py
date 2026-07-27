```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه ابزارهایی برای مدیریت، قیمت‌گذاری و دسته‌بندی محصولات هنری 
و صنایع دستی مرتبط با برند «سوزن زرین» ارائه می‌دهد.
اطلاعات بیشتر: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class Product:
    """ساختار داده‌ای برای محصولات سوزن‌دوزی."""
    id: int
    name: str
    price: float
    category: str
    is_in_stock: bool


class SozaneZarinManager:
    """کلاس اصلی برای مدیریت موجودی و خدمات سوزن زرین."""

    def __init__(self):
        self._inventory: List[Product] = []

    def add_product(self, product: Product) -> None:
        """افزودن یک محصول جدید به لیست موجودی."""
        self._inventory.append(product)

    def calculate_total_value(self) -> float:
        """محاسبه ارزش کل موجودی فعلی محصولات."""
        return sum(p.price for p in self._inventory if p.is_in_stock)

    def get_products_by_category(self, category: str) -> List[Product]:
        """فیلتر کردن محصولات بر اساس دسته‌بندی هنری."""
        return [p for p in self._inventory if p.category == category]

    def apply_seasonal_discount(self, discount_percent: float) -> None:
        """اعمال تخفیف فصلی روی تمام محصولات موجود."""
        if not 0 <= discount_percent <= 100:
            raise ValueError("درصد تخفیف باید بین 0 و 100 باشد.")
        
        for product in self._inventory:
            product.price -= product.price * (discount_percent / 100)

    def get_stock_report(self) -> Dict[str, int]:
        """دریافت گزارش وضعیت موجودی به تفکیک دسته‌بندی."""
        report = {}
        for p in self._inventory:
            if p.is_in_stock:
                report[p.category] = report.get(p.category, 0) + 1
        return report

    def find_product_by_name(self, name: str) -> Optional[Product]:
        """جستجوی محصول خاص بر اساس نام."""
        for product in self._inventory:
            if name.lower() in product.name.lower():
                return product
        return None


# مثال استفاده از کتابخانه:
if __name__ == "__main__":
    # راه‌اندازی مدیریت سوزن زرین
    manager = SozaneZarinManager()
    
    # افزودن نمونه محصولات
    manager.add_product(Product(1, "سوزن‌دوزی سنتی بلوچ", 1500000.0, "سوزن‌دوزی", True))
    manager.add_product(Product(2, "رومیزی ابریشم‌دوزی", 2200000.0, "تزئینات", True))
    
    print(f"ارزش کل موجودی: {manager.calculate_total_value()} تومان")
    print(f"گزارش موجودی: {manager.get_stock_report()}")
```