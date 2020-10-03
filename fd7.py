class FDAccount:
    def intrest(amt,nd):
     if(amt>0 and amt<10000000):
        if (nd > 6 and nd<14):
            rate = 4.50
        elif (nd > 14 and nd < 30):
            rate = 4.75
        elif (nd > 29 and nd < 46):
            rate = 5.50
        elif (nd > 45 and nd < 61):
            rate = 7
        elif (nd > 60 and nd < 185 ):
            rate = 7.50
        elif (nd > 184):
            rate = 8.75
        else:
            print('error')
     elif(amt>999999):
         if (nd > 6 and nd < 14):
             rate = 6.50
         elif (nd > 14 and nd < 30):
             rate = 6.75
         elif (nd > 29 and nd < 46):
             rate = 6.75
         elif (nd > 45 and nd < 61):
             rate = 8
         elif (nd > 60 and nd < 185):
             rate = 8.50
         elif (nd > 184):
             rate = 10
         else:
             print('error')
     else:
         print('error')
     check=int(input('enter your age'))
     if(check>59):
         intres=amt*rate/100
         return intres
     elif(check<60):
         intres=amt*rate/100
         return intres
     else:
         print('error')
