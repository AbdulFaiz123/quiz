import csv
from collections import namedtuple
def __init__(self,name,symbol,exchange,price):
    self.name=name       
    self.exchange=exchange       
    self.price =price       
    self.symbol=symbol
def __str__(self):
    print("{self.name},{self.exchange},{self.price},{self.symbol}")  
count =0      
try:
    name =int(input("eneter the name:"))
    count = count+1
except ValueError:
    print(f"invalid {name}")
print("\n")
print("no of count is :{count}")
def show stock_by_price(price):
    st_lst