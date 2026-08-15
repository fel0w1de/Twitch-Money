
points = int(input("Enter the number of points awarded: "))
multiplier = float(input("Enter the betting odds: ").replace(",", "."))



total_payout = int(points * multiplier)
net_profit = total_payout - points


print(f"\n--- Betting results ---")
print(f"You will receive in total: {total_payout} points")
print(f"The net gain will be: {net_profit} points")



input("\nPress Enter to close the program...")
