# This program will calculate how long it takes a picture from Curiosity
# To Reach Earth from Mars's Closest Distance


def main():
    print("Curiosity transmitts pictures to Earth in")
    DistanceMars = 34000000
    SpeedofTransmit = 186000
    Time = DistanceMars / SpeedofTransmit
    print("{} Seconds!".format(Time))


main()
