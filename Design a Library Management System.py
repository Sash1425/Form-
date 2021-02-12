Actors 
- Admin 
- User 
- System

System Requirements:
	- add book, delete book
	- Search book by book name, id, date
	- locate book 
	- Keep records 
	- collect fines 
	- send notifications 
	
	-reserve book 
	
class:
	-person
	-book 
	-user
	-library 
	-system
	-admin
	
-----------------------------------------------------------------------------------------------------

from abc import ABC
from enum import Enum
import threading

class book_limit(enum):
	max_book=5

class day_limit(enums):
	day_limit=10

class person(ABC):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		
	def reset(self):
		pass 
	
	
	
class admin(person):
	def __init__(self,name,email,password):
		super().__init__(name,email,password)
		
	def reset(self):
		pass
	
	def add_book():
		pass 
	
	def delete_book():
		pass 
	
	def search_book():
		pass 
	
	def locate_book():
		pass 
	
	def record():
		pass 
	
	def collect_fine():
		pass 
	
	
	
class user(person):
	
	def __init__(self):
		super().__init__(name,email,password)


	def register(self):
		pass 
	
	
	def login(self):
		pass 
	
	def search_name():
		pass
	
	def search_title():
		pass
	
	def search_subject():
		pass
	
	def serach_date():
		pass 
	
	def revserse(self):
		pass 
	
	def request_book():
		pass 
	
	
class book():
	def __init__():
		
	def strore_book():
		pass 
	
	def required_book():
		pass 
	
	def top_books():
		pass 
	
	def categprise():
		pass 
	

class system():
	def __init__(self):
		
	def read_barcode():
		pass 
	
	def check_record():
		pass 
	
	
	def check_due_list():
		pass 
	
	
	def notification():
		pass 