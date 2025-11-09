Godina = int(input("Unesite godinu: "))

if (Godina % 4 == 0 and Godina % 100 != 0) or (Godina % 400 == 0):
    print("Godina " + str(Godina) + ". je prijestupna")
else:
    print("Godina " + str(Godina) + ". nije prijestupna")