from fd7 import FDAccount
from rd7 import RDAccount
from sb7 import SBAccount
class call():
 n = 1
 while (n != 0):
  print('---------------------------------')
  print('|\t please provide  input      | \n'
         '|\t 1. Intrest Claculator - SB |\n'
         '|\t 2. Intrest Claculator - RD |\n'
         '|\t 3. Intrest Claculator - FD |\n'
         '|\t 4. exit                    |')
  print('---------------------------------')
  choice = int(input('enter your choice\n'))
  if (choice ==1):
      dep=int(input('enter the amuont you are going to deposit in account: '))
      intrest=SBAccount.intrest(dep)
      print('interest gained is :  %d'%intrest)
#-------------------------------------------------------------------------------
  elif (choice == 2):
     dep=int(input('enter the  recurring deposit amount: '))
     NoM=int(input('enter the number of months : '))
     intrest = RDAccount.intrest(dep,NoM)
     print('interest gained is :  %d '%intrest)
  elif (choice == 3):
      dep = int(input('enter the  fixed deposit amount: '))
      NoD = int(input('enter the number of months : '))
      intrest = FDAccount.intrest(dep,NoD)
      print('interest gained is :  %d '%intrest)
  elif (choice == 4):
     n=0
  else :
    print('Sorry, that combination did\'nt worked')