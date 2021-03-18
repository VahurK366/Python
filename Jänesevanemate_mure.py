#Isesesisev töö nr.3
# Vahur Kuuskmann - ITT20
# Ülesanne 3.2


mituringi = int(input("Sisestage ringide arv:"))
porgand = 0

for i in range(mituringi+1):
    if i%2 == 0:
        porgand = porgand + i
print("Saadavate porgandite kogu arv on: " + str(porgand))