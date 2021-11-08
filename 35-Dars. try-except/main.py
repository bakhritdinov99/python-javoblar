#15:47

while True:
    x = input("Butun va noldan farqli son kiriting: ")
    try:
        x = int(x)
        y = 50/x
    except ZeroDivisionError:
        print("Kiritilgan sonni 0 ga bo'lish mumkin emas, qayta kiriting.")
    except ValueError:
        print("Kirtilgan son butun son emas, qayta kiriting")
    else:
        break