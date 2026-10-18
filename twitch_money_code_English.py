

import msvcrt
from datetime import datetime
import random


points = int(input("Enter the number of points awarded: "))
multiplier = float(input("Enter the betting odds: ").replace(",", "."))



total_payout = round(points * multiplier)
net_profit = total_payout - points

# current_time = datetime.now().strftime("[%d.%m.%Y %H:%M:%S]")
if random.choice([True, False]):
    current_time = str(datetime.now())
else:
    now = datetime.now()
    hour_12 = now.hour % 12
    if hour_12 == 0:
        hour_12 = 12

    #min_clean = str(int(now.strftime("%M")))
    #sec_clean = str(int(now.strftime("%S")))

    min_clean = now.strftime("%M")
    sec_clean = now.strftime("%S")

    current_time = f"{now.month}.{now.day}.{now.year} {hour_12}:{min_clean}:{sec_clean}"


print(f"\n{current_time} --- Betting results ---")
print(f"You will receive in total: {total_payout} points")
print(f"The net gain will be: {net_profit} points")



print("\nPress any key to close the program...")

try:
    msvcrt.getch()
except Exception:
    input()
