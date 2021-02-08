#Iseseisev töö nr.2
#Vahur Kuuskmann - ITT20


#2.5 Õunad
import random
from random import randrange

poisid = int(input("Mitu pöialpoissi tahab õunu?"))
def randnums():
   numbers = [] 
   for count in range(poisid):
        number = random.randint(1,2)
        numbers.append(number)
        print(number)
   lumi = sum(numbers)
   üle = 14 - lumi
   print("Lumevalgekesel jäi",üle)
randnums()

