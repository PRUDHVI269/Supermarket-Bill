from datetime import datetime

name=input("Enter User Name : ")
 # LIST OF ITEMS
list1 ='''' 
RICE      Rs 20/kg
SUGAR     Rs 30/kg
SALT      Rs 20/kg
OIL       Rs 80/liter
PANEER    Rs 110/packet
MAGGI     Rs 12/packet
BOOST     Rs 5/packet
COLGATE   Rs 100/each
COOLDRINK Rs 50/liter
TEAPOWDER Rs 100/Packet
''' 
#decleration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
#item list = ilist
qlist=[]
#quantity list = qlist
plist=[]
#price list =plist

#ROUNDFIGURE

#rates for items
items = {'RICE':20,
         "SUGAR":30,"SALT":20,
         "OIL":80,"PANEER":110,"MAGGI":12,
         "BOOST":5,"COLGATE":100,"COOLDRINK":50,"TEAPOWDER":100}

option=int(input("To View The Items Press 1 :  "))
if option==1:
    print(list1)
else:
    print("YOU PRESSED WRONG NUMBER BUT WE CAN SHOP")
for i in range(len(items)):
    inp1=int(input("Press 1 To Buy (OR) Press 2 TO Exit :- "))
    if inp1==2:
        print("THANKS YOU VISIT AGAIN")
        break
    elif inp1==1:
        item=input("Enter Your Items:")
        quantity=int(input("Enter Quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalamount=gst+totalprice
            ####
        else:
            print("Sorry Item No Find")
    else:
        print("Entered Wrong Number")
    inp=input("Can I Bill The Items YES Or NO :")
    if inp == "YES":
        pass
        if finalamount !=0:
            print(33*"=","CHINNI SUPERMARKET",33*"=")
            print(36*" ","MUMMIDIVARAM")
            print("NAME:",name,30*" ","DATE: ",datetime.now())
            print(85*"-")
            print("SNO",10*" ","ITEMS",10*" ","QUANTITY",5*" ","PRICE")
            for i in range(len(pricelist)):
                print(i+1,12*" ",ilist[i],12*" ",qlist[i],12*" ",plist[i])
            print(85*"-")
            print(50*" ","TOTALAMOUNT : ","RS ",totalprice)
            print("GST AMOUNT : ",50*" ","RS ",gst)
            print(85*"-")
            print(50*" ","FINALAMOUNT : ","RS ",finalamount)
            print(85*"-")
            print(50*" ","THANKS FOR VISITING")
            print(85*"-")
