k=0
pol=""
flag=True
isikukoodid=[]
arvud=[]
while 1:
    k+=1
    print(k)
    ik=""
    while len(ik)!=11:
        try:
            ik=input("Введи личный код: ")
        except:
            ValueError
    print("11 символов")
    print("Проверяем первый символ")
    ik1=int(ik[0])
    if 1<=ik1<=6:
        if ik1%2==0:
            pol="Женский"
        else:
            pol="Мужской"
        ik23=int(ik[1]+ik[2])#год
        ik45=int(ik[3]+ik[4])#месяц #47610112243
        ik67=int(ik[5]+ik[6])#день
        print(ik23)
        print(ik45)
        print(ik67)
        kod=int(str(ik[7])+str(ik[8])+str(ik[9]))
        if 0<=ik23<=99 and 1<=ik45<=12 and 1<=ik67<=31:
            data=str(ik67)+"."+str(ik45)+"."+str(ik23)#11.10.76
            #11.10.76
            print(data)
            kontrol=int(ik[-1])
            n=1
            summa=0
            #4761011224,3
            ikk=str(int(ik)//10)
            print(ikk)
            for i in ikk: #1*4+2*7+3*6
                summa+=int(i)*n
                n+=1
                if n==10:
                    n=1

            kontroll=summa-(summa//11)*11#kontrol==kontroll?
            if kontrol==kontroll:
                print("Личный код верный, контрольный номер ок")
                isikukoodid.append(ik)
            else:
                print("Личный код неверный, контрольный номер не ок")
                arvud.append(ik)

            if 1<=kod<=10:
                reg="Kuressaare Haigla"
            elif 11<=kod<=19:
                reg="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
            elif 21<=kod<=220:
                reg="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
            elif 221<=kod<=270:
                reg="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
            elif 271<=kod<=370:
                reg="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
            elif 371<=kod<=420:
                reg="Narva Haigla"
            elif 421<=kod<=470:
                reg="Pärnu Haigla"
            elif 471<=kod<=490:
                reg="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
            elif 491<=kod<=520:
                reg="Järvamaa Haigla (Paide)"
            elif 521<=kod<=570:
                reg="Rakvere, Tapa haigla"
            elif 571<=kod<=600:
                reg="Valga Haigla"
            elif 601<=kod<=650:
                reg="Viljandi Haigla"
            elif 651<=kod<=700:
                reg="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
            print(pol, data)
            print(reg)

    else:
        arvud.append(ik)
    if k==5: break
    