
class RDAccount:
    rate = 0.0
    a=0
    n=0
    def intrest(amt,nm):
        a=amt
        n=nm
        if(nm>0 and nm<7):
            rate=7.50
        elif(nm>6 and nm<10):
            rate=7.75
        elif(nm>9 and nm<13):
            rate=8.00
        elif (nm > 12 and nm < 16):
            rate = 8.25
        elif (nm > 15 and nm < 19):
            rate = 8.50
        elif (nm > 20):
            rate = 8.75
        else:
            print('error')

        check=int(input('PLEASE PROVIDE YOUR AGE:  '))
        if(check>59):
          rate=rate+0.5
          p1=a*(n*n+1)*rate
          intres=p1/(12*2*100)
          return intres
        elif(check<60):
            p1 = a * (n * n + 1) * rate
            intres = p1 / (12 * 2 * 100)
            return intres
        else:
            print('error')