

import msvcrt


points = int(input("Введите количество поставленных баллов: "))
multiplier = float(input("Введите коэффициент ставки: ").replace(",", "."))


total_payout = round(points * multiplier)
net_profit = total_payout - points


print(f"\n--- Результаты ставки ---")
print(f"Вы получите всего: {total_payout} баллов")
print(f"Чистый выигрыш составит: {net_profit} баллов")




print("\nНажмите любую кнопку, чтобы закрыть программу...")
msvcrt.getch()
