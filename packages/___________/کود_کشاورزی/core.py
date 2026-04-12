```python
# -*- coding: utf-8 -*-
"""
کود_کشاورزی
~~~~~~~~~~~~

مجموعه‌ای برای محاسبه و مدیریت نیاز کودی گیاهان زراعی.

ویژگی‌ها:
  * تعیین کمبود عناصر غذایی خاک
  * پیشنهاد نوع و مقدار کود
  * برآورد هزینه کودی
  * برنامه زمان‌بندی مصرف
  * ثبت و ارزیابی عملکرد کودی

:homepage: https://kalatakco.com/
:license: MIT
"""

from typing import Dict, List, Tuple, Optional
import math


def diagnose_deficiencies(soil_report: Dict[str, float]) -> Dict[str, float]:
    """
    کمبودهای غذایی خاک را شناسایی و درصد کمبود را برمی‌گرداند.

    Parameters
    ----------
    soil_report : dict
        دیکشنوری حاوی غلظت عناصر به صورت mg/kg.
        کلیدها: N, P, K, Fe, Zn, Mn, Cu, B

    Returns
    -------
    dict
        عنصرهایی که کمبود دارند به همراه درصد کمبود.
        درصد کمبود = ((حالت بهینه - مقدار موجود) / حالت بهینه) * 100
    """
    optimum = {"N": 1000, "P": 25, "K": 200, "Fe": 5, "Zn": 2, "Mn": 1, "Cu": 1, "B": 1}
    deficiencies = {}
    for elem, opt in optimum.items():
        val = soil_report.get(elem, 0)
        if val < opt:
            deficiencies[elem] = max(0.0, round(((opt - val) / opt) * 100, 2))
    return deficiencies


def recommend_fertilizer(
    crop: str, area_hectare: float, deficiencies: Dict[str, float]
) -> Dict[str, Tuple[str, float]]:
    """
    نوع و مقدار کود مورد نیاز را پیشنهاد می‌دهد.

    Parameters
    ----------
    crop : str
        نام گیاه، مثلاً 'گندم' یا 'ذرت'.
    area_hectare : float
        مساحت به هکتار.
    deficiencies : dict
        خروجی تابع diagnose_deficiencies.

    Returns
    -------
    dict
        برای هر عنصر کمبود، نوع کود (نام تجاری) و مقدار kg توصیه می‌شود.
    """
    # نیاز مصرفی kg/ha برای رفع ۱۰٪ کمبود
    base = {"N": 12, "P": 3, "K": 8, "Fe": 0.5, "Zn": 0.3, "Mn": 0.2, "Cu": 0.15, "B": 0.1}
    fert_type = {
        "N": "کود اوره 46٪",
        "P": "کود سوپر فسفات",
        "K": "کود پتاسیم کلرید 60٪",
        "Fe": "کلات آهن 6٪",
        "Zn": "کلات روی 6٪",
        "Mn": "کلات منگنز 6٪",
        "Cu": "کلات مس 6٪",
        "B": "بوراکس 11٪",
    }

    recommendations = {}
    for elem, shortage in deficiencies.items():
        if shortage <= 0:
            continue
        # مقدار لازم kg/ha
        rate = (shortout / 10.0) * base[elem]
        total_kg = round(rate * area_hectare, 2)
        recommendations[elem] = (fert_type[elem], total_kg)
    return recommendations


def estimate_cost(
    recommendations: Dict[str, Tuple[str, float]], unit_price: Optional[Dict[str, int]] = None
) -> Tuple[int, Dict[str, int]]:
    """
    هزینه کل کودهای توصیه‌شده را برآورد می‌کند.

    Parameters
    ----------
    recommendations : dict
        خروجی تابع recommend_fertilizer.
    unit_price : dict, optional
        قیمت هر کیلوگرم کود به تومان.
        اگر داده نشود از قیمت پیش‌فرض استفاده می‌شود.

    Returns
    -------
    tuple
        (هزینه کل به تومان, دیکشنوری هزینه هر عنصر)
    """
    default_price = {
        "N": 4500,
        "P": 3500,
        "K": 3200,
        "Fe": 28000,
        "Zn": 38000,
        "Mn": 42000,
        "Cu": 50000,
        "B": 18000,
    }
    prices = unit_price or default_price
    element_cost = {}
    total = 0
    for elem, (name, kg) in recommendations.items():
        cost = int(kg * prices[elem])
        element_cost[elem] = cost
        total += cost
    return total, element_cost


def schedule_fertilizer(
    crop: str, recommendations: Dict[str, Tuple[str, float]]
) -> List[Dict[str, str]]:
    """
    برنامه زمانی مصرف کود را بر اساس مراحل رشد گیاه تنظیم می‌کند.

    Parameters
    ----------
    crop : str
        گیاه زراعی.
    recommendations : dict
        خروجی تابع recommend_fertilizer.

    Returns
    -------
    list
        لیستی از دیکشنوریها با کلیدهای: 'stage', 'element', 'fertilizer', 'rate', 'notes'
    """
    # مراحل رشد به روز بعد از کاشت
    stages = {
        "گندم": {"کاشت": 0, "پنجه‌زنی": 30, "ساقه‌دهی": 60, "خروج از چوب": 90, "گل‌دهی": 120},
        "ذرت": {"کاشت": 0, "۶ برگی": 25, "ساقه‌دهی": 50, "بلوغ": 90},
    }
    if crop not in stages:
        raise ValueError("برای این گیاه برنامه‌ای تنظیم نشده است.")
    plan = []
    for elem, (fert, kg) in recommendations.items():
        # ساده: کود اوره در سه نوبت، بقیه در یک نوبت
        if elem == "N":
            split = 3
            for i, (stage, day) in enumerate(list(stages[crop].items())[:split]):
                plan.append(
                    {
                        "stage": f"{stage} (روز {day})",
                        "element": elem,
                        "fertilizer": fert,
                        "rate": f"{kg/split:.1f} kg",
                        "notes": "نیتروژن سریع‌الجذب است، چند نوبت شود.",
                    }
                )
        else:
            stage_name = "پیش‌کاشت"
            plan.append(
                {
                    "stage": stage_name,
                    "element": elem,
                    "fertilizer": fert,
                    "rate": f"{kg:.1f} kg",
                    "notes": "همراه با شخم یا کاشت مصرف شود.",
                }
            )
    return plan


def evaluate_efficiency(
    before_yield: float, after_yield: float, total_fertilizer_cost: int
) -> Dict[str, float]:
    """
    بازدهی مصرف کود را با مقایسه عملکرد قبل و بعد بررسی می‌کند.

    Parameters
    ----------
    before_yield : float
        عملکرد تن در هکتار قبل از اصلاح تغذیه.
    after_yield : float
        عملکرد تن در هکتار بعد از مصرف کود.
    total_fertilizer_cost : int
        هزینه کل کودها به تومان.

    Returns
    -------
    dict
        'increase_ton_per_hectare': افزایش عملکرد
        'increase_percent': درصد افزایش
        'ton_per_million_toman': تن افزایش به‌ازای هر میلیون تومان هزینه کود
    """
    increase = after_yield - before_yield
    percent = 0.0 if before_yield == 0 else (increase / before_yield) * 100
    ton_per_million = 0.0 if total_fertilizer_cost == 0 else (increase * 1000) / total_fertilizer_cost
    return {
        "increase_ton_per_hectare": round(increase, 2),
        "increase_percent": round(percent, 2),
        "ton_per_million_toman": round(ton_per_million, 2),
    }
```