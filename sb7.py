class SBAccount:
    def intrest(amt):
        check=input('ARE YOU A \'NRI\' Y/N : ')
        check=check.upper()
        if(check=='Y'):
            intr=amt*6/100
            return intr
        elif(check=='N'):
            intr=amt*4/100
            return intr
        else:
            print('oops pls provide input correctly')