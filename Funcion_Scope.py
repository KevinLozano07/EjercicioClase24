a=10; #Global Variable a

def MyFunc1():
 a=20 #Local Variable
 print("1 :",a)

def MyFunc2():
 print("2 :",a)

MyFunc1() #Mostrara el local
MyFunc2() #Mostrara el global