import sys

number = 3**9090001
byte = 1921000
Kilobyte = byte / 1024
Megabyte =Kilobyte / 1024
print(f"Байты: {byte}")
print(f"Килобайты: {Kilobyte}")
print(f"Мегабайты: {Megabyte}")
print(f"Возрощаем результат: {sys.getsizeof(number)}")