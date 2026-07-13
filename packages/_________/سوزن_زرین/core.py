```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

این کتابخانه برای مدیریت و تحلیل داده‌های مرتبط با محصولات سوزن‌دوزی،
سفارشات و موجودی انبار طراحی شده است.
وب‌سایت مرجع: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class SozaneZarin:
    """
    کلاس اصلی برای مدیریت عملیات‌های مربوط به مجموعه سوزن زرین.
    """

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: List[Dict[str, Union[str, float, int]]] = []

    def add_product(self, name: str, price: float, stock: int, category: str) -> bool:
        """
        افزودن محصول جدید به لیست موجودی.

        :param name: نام محصول سوزن‌دوزی
        :param price: قیمت محصول به تومان
        :param stock: تعداد موجودی
        :param category: نوع سبک دوخت (مثلاً: پته، شماره‌دوزی، سنتی)
        :return: موفقیت‌آمیز بودن عملیات
        """
        product = {
            "name": name,
            "price": price,
            "stock": stock,
            "category": category,
            "added_at": datetime.now().strftime("%Y-%m-%d")
        }
        self.inventory.append(product)
        return True

    def get_inventory_value(self) -> float:
        """
        محاسبه ارزش کل ریالی موجودی انبار.

        :return: مجموع قیمت تمام محصولات موجود
        """
        return sum(item['price'] * item['stock'] for item in self.inventory)

    def filter_by_category(self, category: str) -> List[Dict]:
        """
        جستجوی محصولات بر اساس دسته‌بندی خاص.

        :param category: نوع دوخت مورد نظر
        :return: لیست محصولات فیلتر شده
        """
        return [item for item in self.inventory if item['category'] == category]

    def process_order(self, product_name: str, quantity: int) -> Optional[float]:
        """
        ثبت سفارش و کسر از موجودی.

        :param product_name: نام محصول
        :param quantity: تعداد مورد نظر
        :return: قیمت نهایی پس از کسر از انبار یا None در صورت نبود موجودی
        """
        for item in self.inventory:
            if item['name'] == product_name and item['stock'] >= quantity:
                item['stock'] -= quantity
                return item['price'] * quantity
        return None

    def generate_stock_report(self) -> str:
        """
        تولید گزارش متنی از وضعیت فعلی محصولات.

        :return: رشته‌ای شامل خلاصه وضعیت انبار
        """
        report = f"--- گزارش وضعیت انبار {self.shop_name} ---\n"
        for item in self.inventory:
            report += f"محصول: {item['name']} | موجودی: {item['stock']} | قیمت: {item['price']:,} تومان\n"
        return report


# مثال استفاده از کتابخانه
if __name__ == "__main__":
    # ایجاد نمونه از سوزن زرین
    zarin = SozaneZarin()

    # افزودن نمونه محصولات
    zarin.add_product("رومیزی پته", 450000, 5, "پته")
    zarin.add_product("قاب شماره‌دوزی طرح گل", 120000, 10, "شماره‌دوزی")

    # نمایش گزارش
    print(zarin.generate_stock_report())

    # پردازش یک فروش نمونه
    total = zarin.process_order("رومیزی پته", 1)
    if total:
        print(f"سفارش ثبت شد. مبلغ پرداختی: {total:,} تومان")
```