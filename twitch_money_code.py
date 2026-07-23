
points = int(input("Введите количество поставленных баллов: "))
multiplier = float(input("Введите коэффициент ставки: "))


total_payout = int(points * multiplier)
net_profit = total_payout - points


print(f"\n--- Результаты ставки ---")
print(f"Вы получите всего: {total_payout} баллов")
print(f"Чистый выигрыш составит: {net_profit} баллов")



input("\nНажми Enter, чтобы закрыть программу...")
