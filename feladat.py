lista = ["á","g","h","z","t","s","o","m","k","ü","ö","ó","ú","ű","n","v","x","í","y","q","é","r"]
while True:
    ip = input("Adj meg egy ip címet: ")
    if ":" in ip:
        db = 0
        for i in range(0, len(ip)):
            if ip[i].lower() == ":":
                db += 1
        if db >= 2:
            check = 0
            for i in lista:
                if lista[i] in ip:
                     check += 1
            if check > 0:
                print("Ez se ipv4-es, se ipv6-os cím")
            elif db <= 7:
                db2 = 0
                for i in range(0, len(ip)):
                    if ip[i].lower() not in "ághztuopkmnlvűéőúóüöqwrzíyxs":
                        db2 += 1
                if db2 > 0:
                    print("Ez egy ipv6-os cím")  
                else:
                    print("Ez se ipv4-es, se ipv6-os cím")    
    elif "." in ip:
        db = 0
        for i in range(0, len(ip)):
            if ip[i].lower() == ".":
                db += 1
        if db == 3:
            db2 = 0
            for i in range(0,len(ip)):
                if ip[i].lower() in "1234567890":
                    db2 += 1
            if db2 >= 4:
                print("Ez egy ipv4-es cím") 
            else:
                print("Ez nem megfelelő ipv4-es cím")
    else:
        print("Ez se ipv4-es, se ipv6-os cím")