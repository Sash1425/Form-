Design tik tak toe game

Actors :
    -play (users)
    -Admin
    
Use Case Diagram i.e. who interact with the system and how will interact 

Admin:
    -Accept new invitation 
    -Taking feedback 
    - Analysing feedback 
    
users:
    - Registration and Login 
    - Selecting options to from[-1,1]
    - participate in game  
    - Moves
    
Entity 
Classes 
    - Person 
    - user 
    - Admin 
    - board 
    - Score & winner declration 
    
-------------------------------------------------------------------------------------

from abs import ABC 
from enum import Enum 
import threading 


class Max_player(Enum):
    No._of_player=2 
    
class Max_time(Enum):
    time=30 
    
class dimension(Enum):
    raw,column=3,3 
    
class Person(ABC):
    def __init__(self,name,email,username,password):
        self.name= name 
        self.email=email
        self.username=username
        self.password=password
    
    def login(self):
        pass 
    
    def Registration(self):
        pass 
    
    def reset(self):
        pass 
    

class Admin(Person):
    def __init__(self):
        super().__init__()
    

class player1(Person):
    def __init__(self):
        super().__init__()


class player2(Person):
    def __init__(self):
    

class board():
    
    @instancemethod 
    def __init__(self):
        self.matrix=[[]]
    
    @instancemethod
    def fill_defaul_val(self):
        self.matrix=[0 for i in range(3)] for j in range(3)]
        return self.matrix 
    

class move():
    instance=None 
    
    @instancemethod
    def __init__(self,x,y,player,Board):
        self.x=x 
        self.y=y  
        self.player=player 
        self.Board=Board

    @instancemethod
    def update_move(self):
        lock=threading.Lock()
        
        lock.acquire()
        if player==1:
            Board[self.x][self.y]=1 
        else:
            Board[self.x][self.y]=0 
        lock.release()
    
    @instancemethod
    def get_updated_board(self):
        return self.Board

    
class Score():
    
    def__init__(self,Board):
        self.Board=Board


    def calculate_raw(self):
        result_raw=-1 
        for i in range(3):
            temp=0 
            for j in range(3):
                temp+=self.Board[i][j]
                
            if temp==0:
                result_raw=temp
            if temp==3:
                result_raw=1 
        return result_raw 


    def calculate_col(self):
        result_col=-1 
        for i in range(3):
            temp=0 
            for j in range(3):
                temp+=self.Board[j][i]
                
            if temp==0:
                result_col=temp
            if temp==3:
                result_col=1 
        return result_col 
    
    def calculate_diagonal(self):
        result_diagonal=-1
        temp1=0
        for i in range(3):
            temp1+=self.Board[i][i]
            
        temp=0
        for i in range(3):
            temp+=self.Board[i][2-i]
            
        if temp==0 or temp1==0:
            result_raw=temp
        if temp==3 or temp1==3:
            result_raw=1 
        return result_raw


class Decide_winner():
    def__init__(self):
        
    @classmethod
    def Decide_winner(cls):
        obj = Score()
        raw=obj.calculate_raw()
        col=obj.calculate_col()
        digonal=obj.calculate_diagonal()
        
        if raw!=-1:
            return "Winner is"+str(raw)
        elif col!=-1: 
            return "Winner is"+str(col)
        elif digonal!=-1:
            return "Winner is"+str(digonal)
            
        return "yet to decide or draw"



    