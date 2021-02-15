Design Amazon - Online Shopping System

Actor
    -User
    -Admin
    -Guest 
    -System 
    
Use case Diagram i.e. Who will interact and how will interact 

Admin 
    - restered/login
    - keep watch on products 
    
User 
    -add new products 
    -search for products by their name or category
    -add/remove/modify product items in their shopping cart
    -check out and buy items in the shopping cart
    -

Guest
    -Search products 
    -Registered 
    
System 
    - send notifications 
    
Class 
    -User
    -payment 
    -product 
    -System 
    -shoping cart 
    -canceal order 
    -Tract order 
    
__________________________________________________________________________________________________________



from abc import ABC 
from enum import Enum 
import threading 

class Address():
    def ___init__(self,house,town,city,state,country):
        self.house=house
        self.town=town 
        self.city=city 
        self.state=state
        self.country=country
        
class order_status(Enum):
    unshiped,shiped,complete,pending=1,2,3,4,5 

class account_status(Enum):
    Blocked,Registered,unblock=1,2,3
    
class payment_status(Enum):
    unpaid,decline,paid,accepted=1,2,3,4
    

class person(ABC):
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        
    def login(self):
        pass 
    
class Admin(person):
    "' Abstract base class"' 

    def __init__(self):
        super().__init__()
    
    @staticmethod   
    def Check_review():
        pass 
    
    @staticmethod
    def Check_products():
        pass 

class Guest():
    def __init__(self):
        self.purpose="Visitors"
    
    @staticmethod
    def serach_products():
        pass 
    
    @staticmethod
    def create_account(name,email,password):
        pass 


class User(person):
    def __init__(self):
        super().__init__()
        
    def add_product():
        obj=products()
        pass
    
    @staticmethod
    def remove():
        pass 
    
    @staticmethod
    def modify(product):
        pass 
    
    @staticmethod
    def change_address():
        pass 
    
    @staticmethod
    def cancel_order():
        passs 
    
    
class shoping_cart():
    @staticmethod
    def buy(buy):
        __lock=threading.Lock()
        __lock.aquire()
        ------
        ------
        __lock.release()
        pass 
    
    @staticmethod
    def add_cart(product):
        pass 
    
    def remove_items():
        pass 
    
    
class search_products():
    @staticmethod
    def search_by_name(name):
        item=product_name.get(category,0)
        if item:
            return item 
        else:
            return "not available"

    
    def serach_by_category(category):
        item=product_category.get(category,0)
        if item:
            return item 
        else:
            return "not available"
    

class products():
    product_name={}
    product_category={category:{products}}
    
    @classmethod
    def add_product_name():
        product_name
        pass 
    
    def add_product_category():
        product_category
        pass 
    
    @classmethod
    def remove_product():
        pass 
    
    
class Payment():
    __lock=threading.Lock()
    
    def pay_by_card():
        __lock.aquire()
        ------
        ------
        __lock.release()
        
        pass 
    
    def pay_online():
        pass 
    
    
class Track():
    @staticmethod
    def track_order():
        pass 
    
    
class System():
    def get_change():
        pass 
    
    def send_notification():
        passs 