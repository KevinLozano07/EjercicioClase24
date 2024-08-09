a=10 #Variable global

def MyFunc1():  #Funcion externa
 a=20 #Variable local
 print("1 :",a)

def MyFunc2():
 
 print("2 :",a)

 def SubFun1(st): #Funcion interna
     print("Local Function with ", st)

 SubFun1("Local Call") 

MyFunc1()
MyFunc2()