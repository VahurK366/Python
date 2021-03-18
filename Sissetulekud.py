#Isesesisev töö nr.3
# Vahur Kuuskmann - ITT20
# Ülesanne 3.3

fail = open("konto.txt", "r")
sisu = fail.readlines()
for rida in sisu:
    if float(rida) > 0:
      print(rida,end="")