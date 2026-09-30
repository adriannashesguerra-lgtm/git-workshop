def calc_units_fee(unit):
    return unit * 100

def fin_fee (f_fee):
    misc_fee = 2500
    ot_fee = 1000
    disc = 0.10
    tot_fee = f_fee + misc_fee + ot_fee
    return tot_fee - (f_fee * disc)

def main():
    unit = int(input("Enter the number of units enrolled: "))
    int_fee = calc_units_fee(unit)
    final = fin_fee(int_fee)
    print ("Total fee to pay is:", int_fee)
    print ("Actual Tuition fee is:", final)

main()