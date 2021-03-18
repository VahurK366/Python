#Isesesisev töö nr.3
# Vahur Kuuskmann - ITT20
# Ülesanne 3.4


def laul():
    fail = input("Palun sisestage faili nimi: ")
    valik = open(fail, "r", encoding="UTF-8")
    a = 0
    for i in valik:
        a = a+1
        print(str(a)+".",i,end="")
        
    kas_valik = int(input("\nVali lugu: "))
    valik.seek(0)
    a = 0
    for i in valik:
        a =a+1
        if kas_valik == a:
            print(str(a)+".",i,end="")
            
laul()