# This program will calculate how much money you earned as a babysitter


def main():

    shour = float(input("Enter the starting hours "))
    smin = float(input("Enter the starting minutes "))
    ehour = float(input("Enter the ending hours "))
    emin = float(input("Enter the ending minutes: "))
    cperiodh = ehour-shour
    cperiodm = emin - smin
    cperiodm1 = cperiodm / 60
    fperiod = cperiodh + cperiodm1
    if ehour < 9:
        charge = fperiod * 2.50
        print("Your payable ammount is {}".format(charge))
    elif ehour >= 9:
        shour1 = (9-(shour + (smin / 60)))
        ehour1 = ((ehour + (emin / 60)-9))
        fcharge1 = (shour1 * 2.50) + (ehour1 * 1.75)
        print("Your payable amount is {}".format(fcharge1))


main()
