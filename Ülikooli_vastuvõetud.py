#Isesesisev töö nr.3
# Vahur Kuuskmann - ITT20
# Ülesanne 3.1

aasta = input("Palun sisestage, millise aasta andmeid vajate 2011-2019:")
fail = open("rebased.txt", encoding="UTF-8")
arvud = fail.readlines()
print(arvud[int(aasta[3])-1])

fail.close()