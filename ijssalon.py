aantalbollen = 0
horn = 0
bakjes = 0
slagroom = 0
sprikels = 0
caramel = 0
slagprijs = 0.50
sprinprijs = 0.30
caraprijs = 0.60
liter = 0
def vraag():
    vraag = input('wilt u nog meer bestellen? ')
    if vraag == 'y' or vraag == 'yes' or vraag == 'Y':
        return loop()
    elif vraag == 'n' or vraag == 'no' or vraag == 'N':
        print('bedankt voor je bestelling! ')
        print('tot ziens')
    elif vraag != vraag != 'y' or vraag != 'yes' or vraag != 'Y' or vraag != 'n' or vraag != 'no' or vraag != 'N':
        sorry()
        loop()

def welkom():
    print('Welkom bij Papi Gelato!')
    print('je mag alle smaken kiezen zolang dat het vanile, aardbei, chocolade en munt is')

def sorry():
    print('Sorry dat is geen optie die we aanbieden ')
def ZakVraag():
    vraag2 = input('wilt u nog meer bestellen? ')
    if vraag2 == 'y' or vraag2 == 'yes' or vraag2 == 'Y':
        return zakofpart()
    elif vraag2 == 'n' or vraag2 == 'no' or vraag2 == 'N':
        print('bedankt voor je bestelling! ')
        print('tot ziens')
    elif vraag2 != vraag2 != 'y' or vraag2 != 'yes' or vraag2 != 'Y' or vraag2 != 'n' or vraag2 != 'no' or vraag2 != 'N':
        sorry()
        ZakVraag()
def zakelijksmaken():
    global liter
    liternummer = 0
    for x in range(int(liter)):
        liternummer += 1
        smaak = input('liter nummer: {}: A) Chocolade B) Aardbei C) vanile, type(A or B or c or D): '.format(liternummer))
        if smaak == 'a' or smaak == 'A':
            smaak = 'chocolade'
        elif smaak == 'b' or smaak == 'B':
            smaak = 'aardbei'
        elif smaak == 'c' or smaak == 'C':
            smaak = 'vanile'

        else:
            sorry()
            zakelijksmaken()
def zakelijkfactuur():
    literprijs = 9.80
    total = (literprijs*int(liter))
    btw = (total/100) * 6
    print('----------["Papi Gelato"]----------')
    print('Liter         {} x {} = {:.2f}'.format(int(liter), literprijs,total))
    print('                         ------')
    print('Totaal(inclusief BTW) = {:.2f}'.format(total))
    print('BTW 6%                = {:.2f}'.format(btw))
    ZakVraag()
def zakelijk():
    global liter
    welkom()
    liter = input('hoeveel liters wilt u? ')
    zakelijksmaken()
    ZakVraag()
    zakelijkfactuur()
def factuur():
    total = ((aantalbollen*0.95)+(bakjes*0.75)+(horn*1.25)+(slagroom*slagprijs + sprikels * sprinprijs + caramel*caraprijs))
    print('----------["Papi Gelato"]----------')
    print('Bolletjes     {} x 1.10  = {:.2f}'.format(aantalbollen,(aantalbollen*0.95)))
    print('Horrentje     {} x 1.25  = {:.2f}'.format(horn,(horn*1.25)))
    print('Bakje         {} x 0.75  = {:.2f}'.format(bakjes,(bakjes*0.75)))
    print('Toppings                = {:.2f}'.format(slagroom*slagprijs + sprikels * sprinprijs + caramel*caraprijs))
    print('                         ------')
    print('Totaal                  = {:.2f}'.format(total))
    vraag()
       
def loop():
    bestellingen = int(input('hoeveel beestellingen wilt u maken ?'))
    for i in range(bestellingen):
        bolletjes()

def bolletjes():
    global aantalbollen
    global horn
    global bakjes
    global slagprijs 
    global caraprijs
    global sprinprijs
    welkom()
    aantal = str(input('hoeveel bolletjes wilt u? '))
    aantalbollen += int(aantal)
    def topping():
        global slagroom 
        global caramel
        global sprikels
        top = input('wil je toppings op je ijsje?(Y/N): ')
        if top == 'y' or top == 'Y' or top == 'yes' or top == 'Yes' or top == 'j' or top == 'J' or top == 'Ja' or top == 'ja':
            topingvraag = input('wat voor topping wil je? kies een van de volgende: A)Slagroom B)Sprinkels C)Caramel saus: ')
            if topingvraag == 'A' or topingvraag == 'a':
                topingvraag == 'Slagroom'
                slagroom += 1
            elif topingvraag == 'B' or topingvraag == 'b':
                topingvraag == 'Sprinkels'
                sprikels += 1
            elif topingvraag == 'C' or topingvraag == 'c':
                topingvraag == 'Caramel'
                caramel += 1
        elif top == 'n' or top == 'N' or top =='Nee' or top == 'nee':
            pass
        else: 
            sorry()
            topping()
    def smaken():
        nummer = 0
        for x in range(int(aantal)):
            nummer+=1
            smaak = input('wat voor smaak wilt u voor bolletje nummer {}: A) Chocolade B) Aardbei C) vanile  type(A or B or c): '.format(nummer))
            if smaak == 'a' or smaak == 'A':
                smaak = 'chocolade'
            elif smaak == 'b' or smaak == 'B':
                smaak = 'aardbei'
            elif smaak == 'c' or smaak == 'C':
                smaak = 'vanile'
            else:
                sorry()
                smaken()
    
    smaken() 
    topping()     
    if aantal.isdigit():
        aantal = int(aantal)
        if aantal <= 3:
            keuze = input('wilt u deze {} bolletjes in A) een Bakje of b) een Hoorntje? '.format(aantal))
            bak = 'bak'
            hoornjte = 'hoorntje'
            if keuze == 'a' or keuze == 'A':
                caraprijs = 0.90
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal, bak))
                print('hier is uw {} in een {}'.format(aantal, bak))

                bakjes += 1
            elif keuze == 'b' or keuze == 'B':
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal, hoornjte))
                print('hier is uw {} bolletjes in een {}'.format(aantal, hoornjte))
                horn += 1   
            else:
                sorry()
                smaken()
        if 4 <= aantal <= 8:
            print('dan krijgt u van mij een bakje met {} bolletjes'.format(aantal))
        elif aantal >= 9:
            print('sorry, zulke grote bakken hebben we niet')
    elif not aantal.isdigit():
        sorry()
        bolletjes()
def zakofpart():
    zakelij = input('wilt u zakelijk of particulier kopen? kies A) voor Zakelijk  en B)voor Particulier: ')
    if zakelij == 'A' or zakelij == 'a': 
        zakelijk()
    elif zakelij == 'B' or zakelij == 'b':
        loop()
        factuur()
    else : 
        sorry()
        zakofpart()
welkom()
zakofpart()