# Calculates babysitter pay


def main():
    start = float(input("At what hour did you start? Input in HH:MM. " ))
    Starttime = input("What this AM or PM?")
    end = float(input("At what hour did you end? Input in HH:MM. "))
    endtime = input("Was this AM or PM?")
    if Starttime.lower() == "am":
        print("You started at {} am.".format(start))
    elif Starttime.lower() == "pm":
        print("You started at {} pm.".format(start))
