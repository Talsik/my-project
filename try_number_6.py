import tkinter as tk
def thankyou():
    app = tk.Tk()
    app.title("thank you")
    app.geometry("170x70")
    tk.Label(app, text= "thank you for using my project").grid(row = 2, column=2)
    app.mainloop()
class Coins:
    def __init__(self, name, country, worth):
        self.name = name
        self.country = country
        self.worth = int(worth)
        
    def setchange(self):
        def some():
            return int(eval(input("enter amount:")))
        print(some() * self.worth / 100) 

    def setchange2(self):
        def some2():
            return int(eval(input("enter amount:")))
        print(some2() / self.worth * 100) 


class Mariocart8:
    def __init__(self, cup, track1, track2, track3, track4, favorite,image1):
        self.cup = cup
        self.track1 = track1
        self.track2 = track2
        self.track3 = track3
        self.track4 = track4
        self.favorite = favorite
        self.image1 = image1

    def intruduction(self):
        print("Hello, this is "+self.cup+" ,the first track is "+self.track1 +" ,the second track is "+self.track2+" ,the third track is "+self.track3+" and the fourth track is "+self.track4+"\nmy favorite track from this cup is "+self.favorite)
    
    def printtrack1(self):
        print("The first track of "+self.cup+" is "+self.track1)
    
    def printtrack2(self):
        print("The second track of "+self.cup+" is "+self.track2)
    
    def printtrack3(self):
        print("The third track of "+self.cup+" is "+self.track3)
    
    def printtrack4(self):
        print("The fourth track of "+self.cup+" is "+self.track4)
    
    def printfavorite(self):
        print("my favorite track of "+self.cup+" is "+self.favorite)
    
    def onlycup(self):
        print("This cup's name is "+self.cup)

def main():
    dollar = Coins("dollar", "United States", 100)
    shekel = Coins("shekel", "Israel", 365)
    pound = Coins("pound", "The United Kingdom",80 )
    euro = Coins("euro","The EU",93)
    ruble = Coins("ruble", "Russia", 8160)
    yen = Coins("yen","Japan",13959)
    rupee = Coins("rupee", "India", 8250)
    peso=Coins ("peso","The Philipines", 5596)
    rand =Coins("rand","South Africa",1907)
    dinar= Coins("dinar","Kuwait",31)
    rial= Coins("rial","Iran",4230000)
    zloty= Coins("zloty","Poland",418)
    yuan = Coins("yuan","china",712) 
    real= Coins("real","Brazil",491)
    krone= Coins("krone","Norway",1101)
    krona= Coins("krona","Sweden",1085)
    riyal= Coins("riyal","Saudi Arabia",375)
    won= Coins("won","South Korea", 130250)
    rupiah= Coins("rupiah","Indonisia",1484200)
    # the list of the mario kart cups
    mushroom = Mariocart8("the mushroom cup", "mario kart stadium","water park", "sweet sweet canyon","thwomp ruins","thwomp ruins","C:\\Users\\tals1\\python\\final project\\thwomp_ruins.jpg")
    flower = Mariocart8("the flower cup", "mario circuit","toad harbor", "twisted mansion","shy gut falls","toad harbor","C:\\Users\\tals1\\python\\final project\\toad_harbor.jpg")
    star = Mariocart8("the star cup", "sunshine airport","dolphin shoals", "electrodrome","mount wario","mount wario","C:\\Users\\tals1\\python\\final project\\mount_wario.jpg")
    special = Mariocart8("the special cup", "cloudtop cruise","bone dry dunes", "bowser's castle","rainbow road","cloudtop crusise","C:\\Users\\tals1\\python\\final project\\cloudtop_cruise.jpg")
    shell = Mariocart8("the shell cup", "moo moo meadows","GBA mario circuit", "cheep cheep beach","toad's turnpike","GBA mario circuit","C:\\Users\\tals1\\python\\final project\\mario_circuit.jpg")
    banana = Mariocart8("the banana cup", "dry dry desert","donut plains", "royal raceway","DK jungle","royal raceway","C:\\Users\\tals1\\python\\final project\\royal_raceway.jpg")
    leaf = Mariocart8("the leaf cup", "wario stadium","sherbert land", "melody motorway (music park)","yoshi valley","yoshi valley","C:\\Users\\tals1\\python\\final project\\yoshi_valley.jpg")
    lightning = Mariocart8("the lightning cup", "tick tock clock","piranha plant slide", "grumble volcano","N64 rainbow road","tick tock clock","C:\\Users\\tals1\\python\\final project\\tick_tock_clock.jpg")
    egg = Mariocart8("the egg cup", "yoshi's circuit","excitebike arena", "dragon driftway","mute city","yoshi's circuit","C:\\Users\\tals1\\python\\final project\\yoshis_circuit.jpg")
    triforce = Mariocart8("the triforce cup", "wario's gold mine","SNES rainbow road", "ice ice outpost","hyrule circuit","wario's gold mine","C:\\Users\\tals1\\python\\final project\\warios_gold_maine.jpg")
    bell = Mariocart8("the bell cup", "koopa city","ribbon road", "super bell subway","big blue","big blue","C:\\Users\\tals1\\python\\final project\\big_blue.jpg")
    crossing = Mariocart8("the crossing cup", "baby park","cheese land", "wild woods","animal crossing","wild woods","C:\\Users\\tals1\\python\\final project\\wild_woods.jpg")

    list_of_coins = [dollar, shekel, pound, euro,ruble,yen,rupee,peso,rand,dinar,rial,zloty,yuan,real,krona,krone,riyal,won,rupiah]
    list_of_cups = [mushroom,flower,star,special,shell,banana,lightning,leaf,egg,triforce,bell,crossing]

    print("Hello there, and welcome to my project. This project is capeable of doing two thing: money convertions and telling you about MK8(mario kart 8).")
    qna = input("If you wish to choose converting currencys, plese type money. If you want to learn about MK8, please type mario kart 8 \nThe currencys may not be currect in real time, they are currect for wednesday 7\6.")
    if qna == "money":
        print("You got to the money convertion part! Here, you have three options to choose from - converting money to or from dollars, \nOr printing all of the countrys and their currencys that I chose to include in this project")
        red = input("Do you wish to convert from dollar to your currency(type in f), to dollar(type in t), or print all of the countrys(type in all)?")
        if red == "f":
            blue = input("What currency would you like to use?")
            try:
                for coin in list_of_coins:
                    if blue == coin.name:
                        Coins.setchange(coin)
            except:
                print("There was an error, please try again")
        elif red == "t":
            blue = input("What currency would tou like to use?")
            try:
                for coin in list_of_coins:
                    if blue == coin.name:
                        Coins.setchange2(coin)
            except:
                print("There was an error in the process, please try again")
        elif red == "all":
            app = tk.Tk()
            jjjj = 3
            app.title("a list of all the currencys")
            app.geometry("360x540")
            for coin in list_of_coins:
                tk.Label(app,text= "this currency's name is "+coin.name+" and it is from "+coin.country).grid(row=jjjj,column=2,ipadx=3,ipady=3,columnspan=2)
                jjjj +=3
            print("check the window that has opened")
            app.mainloop()
        thankyou()
    elif qna == "mario kart 8":
        red = input("What cup would you want to use?\nYou can type in a cup name (in the form 'the ____ cup', with no capital letters), or print out all of the cups' names by typing in 'cup'")
        if red == "cup":
            for cup in list_of_cups:
                Mariocart8.onlycup(cup)
        else:
            try:
                for cup in list_of_cups:
                    if red == cup.cup:
                        decision = input("Do you want to see all of the information about this cup, or only about one track? your options are to see about track_one,track_two,track_three, track_four or my_favorite (my favorite track in this cup).\nif you would like all the information, please type all")
                        if decision == "all":
                            Mariocart8.intruduction(cup)
                        elif decision == "track_one":
                            Mariocart8.printtrack1(cup)
                        elif decision == "track_two":
                            Mariocart8.printtrack2(cup)
                        elif decision == "track_three":
                            Mariocart8.printtrack3(cup)
                        elif decision == "track_four":
                            Mariocart8.printtrack4(cup)
                        elif decision == "my_favorite":
                            Mariocart8.printfavorite(cup)
                thankyou()
                        
            except:
                print("An error has occured")
    elif qna == "thank you":
        thankyou()
if __name__ == "__main__":
    main()
