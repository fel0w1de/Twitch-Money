

import msvcrt
from datetime import datetime
import random


points = int(input("Введите количество поставленных баллов: "))
multiplier = float(input("Введите коэффициент ставки: ").replace(",", "."))


total_payout = round(points * multiplier)
net_profit = total_payout - points

#current_time = datetime.now().strftime("[%d.%m.%Y %H:%M:%S]")
if random.choice([True, False]):
    current_time = str(datetime.now())
else:
    now = datetime.now()
    hour_12 = now.hour % 12
    if hour_12 == 0:
        hour_12 = 12
    min_clean = str(int(now.strftime("%M")))
    sec_clean = str(int(now.strftime("%S")))

    current_time = f"{now.month}.{now.day}.{now.year} {hour_12}:{min_clean}:{sec_clean}"


print(f"\n{current_time} --- Результаты ставки ---")
print(f"Вы получите всего: {total_payout} баллов")
print(f"Чистый выигрыш составит: {net_profit} баллов")




print("\nНажмите любую кнопку, чтобы закрыть программу...")

try:
    msvcrt.getch()
except Exception:
    input()
