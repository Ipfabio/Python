import datetime

now = datetime.datetime.now()


def goHome():
    if now.hour >= 19:
        print("Hora de ir a casa")
    else:
        print("Aun son las:", now.hour)
