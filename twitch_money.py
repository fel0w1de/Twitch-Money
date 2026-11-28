#1

import msvcrt
from datetime import datetime
import webbrowser
import sys

lang_choice = input("Select language / Выберите язык (1 - Русский, 2 - English, ru / en): ")

if lang_choice == "1" or lang_choice == "ru":
    lang = "ru"
elif lang_choice == "2" or lang_choice == "en":
    lang = "en"
else:
    lang = "mix"

release_date = datetime(2026, 11, 28)
days_passed = (datetime.now() - release_date).days
DEV_CODE = "k9X4mP2q"
RELEASES_URL = "https://github.com/fel0w1de/Twitch-Money/releases/tag/0.4.2"

if days_passed >= 30:
    while True:
        if lang == "ru":
            ans = input("\n[!] Поддержка этой версии прекращена (прошёл 1 месяц).\nВведите '1' чтобы открыть страницу обновлений: ")
        else:
            ans = input("\n[!] Support for this version has ended (1 month passed).\nEnter '1' to open the updates page: ")
            
        if ans == "1":
            print("Открываю браузер... / Opening browser...")
            webbrowser.open(RELEASES_URL)
            sys.exit()
        elif ans == DEV_CODE:
            break

elif days_passed >= 7:
    if lang == "ru":
        ans = input("\n[?] Прошла неделя с выхода версии. Хотите проверить обновления? (1 - Да, 2 - Нет): ")
    else:
        ans = input("\n[?] A week has passed since release. Do you want to check for updates? (1 - Yes, 2 - No): ")
        
    if ans == "1":
        print("Открываю браузер... / Opening browser...")
        webbrowser.open(RELEASES_URL)
        sys.exit()

#2

error_count = 0

if lang == "ru":
    msg_pts = "Введите количество поставленных баллов: "
    msg_limit = "Ошибка: слишком много баллов, так не бывает! Попробуйте снова."
    msg_exit = "Всё, надоело. Программа закрывается."
    msg_err_int = "Ошибка: введите целое число!"
    msg_mult = "Введите коэффициент ставки: "
    msg_err_float = "Ошибка: введите корректное число (коэффициент)!"
    msg_res_head = "--- Результаты ставки ---"
    msg_res_tot = "Вы получите всего:"
    msg_res_net = "Чистый выигрыш составит:"
    msg_pts_word = "баллов"
    msg_close = "\nНажмите любую кнопку, чтобы закрыть программу..."
elif lang == "en":
    msg_pts = "Enter the number of points awarded: "
    msg_limit = "Error: too many points, that's impossible! Try again."
    msg_exit = "That's it, I'm done. Closing the program."
    msg_err_int = "Error: please enter a whole number!"
    msg_mult = "Enter the betting odds: "
    msg_err_float = "Error: please enter a valid number (odds)!"
    msg_res_head = "--- Результаты ставки ---"
    msg_res_tot = "Вы получите всего:"
    msg_res_net = "Чистый выигрыш составит:"
    msg_pts_word = "баллов"
    msg_close = "\nPress any key to close the program..."
else:
    msg_pts = "Введите количество поставленных баллов: "
    msg_limit = "Error: too many points, that's impossible! Try again."
    msg_exit = "Всё, надоело. Closing the program."
    msg_err_int = "Ошибка: please enter a whole number!"
    msg_mult = "Введите коэффициент ставки: "
    msg_err_float = "Error: введите корректное число!"
    msg_res_head = "--- Betting results ---"
    msg_res_tot = "Вы получите всего:"
    msg_res_net = "The net gain will be:"
    msg_pts_word = "points"
    msg_close = "\nPress any key to close the program..."
#3

while True:
    try:
        points = int(input(msg_pts))
        
        if points > 10000:
            print(msg_limit)
            #error_count += 1
            #if error_count >= 3:
            #    print(msg_exit)
            #    sys.exit()
            continue

        break
    except ValueError:
        #error_count += 1
        #if error_count >= 3:
        #    print(msg_exit)
        #    sys.exit()
        print(msg_err_int)

while True:
    try:
        multiplier = float(input(msg_mult))#.replace(",", "."))
        
        break
    except ValueError:
        #error_count += 1
        #if error_count >= 3:
        #    print(msg_exit)
        #    sys.exit()
        print(msg_err_float)

#points = int(input("Введите количество поставленных баллов: "))
#multiplier = float(input("Введите коэффициент ставки: ").replace(",", "."))
#points = int(input("Enter the number of points awarded: "))
#multiplier = float(input("Enter the betting odds: ").replace(",", "."))

total_payout = round(points * multiplier)
net_profit = total_payout - points

current_time = datetime.now().strftime("[%d.%m.%Y %H:%M:%S]")
#4

#import random
#if random.choice([True, False]):
#    current_time = str(datetime.now())
#else:
#    now = datetime.now()
    #hour_12 = now.hour % 12
    #if hour_12 == 0:
    #    hour_12 = 12
    #min_clean = str(int(now.strftime("%M")))
    #sec_clean = str(int(now.strftime("%S")))
    #hour_clean = now.strftime("%H")
    #min_clean = now.strftime("%M")
    #sec_clean = now.strftime("%S")
    #current_time = f"{now.month}.{now.day}.{now.year} {hour_clean}:{min_clean}:{sec_clean}"
    #date_clean = now.strftime("%d.%m.%Y")
    #current_time = f"{date_clean} {hour_clean}:{min_clean}:{sec_clean}"

#0.5.0
#def save_bet_to_history(time_str, pts, mult, payout, profit):
#    try:

#5

print(f"\n{current_time} {msg_res_head}")
print(f"{msg_res_tot} {total_payout} {msg_pts_word}")
print(f"{msg_res_net} {net_profit} {msg_pts_word}")

print(msg_close)

try:
    msvcrt.getch()
except Exception:
    input()
