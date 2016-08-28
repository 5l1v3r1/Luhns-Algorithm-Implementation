#!/bin/python

card_no=input("enter the card number")
card_no=str(card_no)
total_sum=0
alt=1 #this is to alternately add digit first time and then add digit*2 or digit*2 -1 for the next consecutive time 


for i in card_no:
    
    if(alt==1):
        if(int(i)*2>9):
            total_sum=(total_sum+(2*int(i))-9)
        if(int(i)*2<10):
            total_sum=total_sum+(2*int(i))
        alt=0
    else:
        total_sum+=int(i)
        alt=1
if(total_sum%10 == 0):
    print("valid card")
else:
    print("invalid card")
