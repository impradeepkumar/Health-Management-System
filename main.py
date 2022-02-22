
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
         if k==1:
             c=int(input("Enter 1 for Excercise and 2 for food"))
             if(c==1):
                 value = input("type here \n")
                 with open("rohit_Ex.txt","a") as op:
                    op.write(str([str(gettime())]) +":"+ value +"\n")
                 print("suceesufully written")
             elif(c==2):
                 value = input("type here \n")
                 with open("rohit_food.txt","a") as op:
                     op.write(str([str(gettime())])+ ":" + value + "\n")
                 print("suceesufully written")
         elif(k==2):
             c=int(input("Enter 1 for Excercise and 2 for food"))
             if(c==1):
                 value = input("type here \n")
                 with open("neeraj_Ex.txt","a") as op:
                    op.write(str([str(gettime())]) +":"+ value +"\n")
                 print("suceesufully written")
             elif(c==2):
                 value = input("type here \n")
                 with open("neeraj_food.txt","a") as op:
                     op.write(str([str(gettime())])+ ":" + value + "\n")
                 print("suceesufully written")
         elif(k==3):
             c=int(input("Enter 1 for Excercise and 2 for food"))
             if(c==1):
                 value = input("type here \n")
                 with open("arun_Ex.txt","a") as op:
                    op.write(str([str(gettime())]) +":"+ value +"\n")
                 print("suceesufully written")
             elif(c==2):
                 value = input("type here \n")
                 with open("arun_food.txt","a") as op:
                     op.write(str([str(gettime())])+ ":" + value + "\n")
                 print("suceesufully written")

         else:
             print("Invalid Input")
def retrieve(k):
    if k==1:
        c = int(input("Enter 1 for Excercise and 2 for food"))
        if(c==1):
            with open("rohit_Ex.txt") as op:
                for i in op:
                    print(i, end="")
        if (c == 2):
            with open("rohit_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for Excercise and 2 for food"))
        if(c==1):
            with open("neeraj_Ex.txt") as op:
                for i in op:
                    print(i, end="")
        if (c == 2):
            with open("neeraj_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("Enter 1 for Excercise and 2 for food"))
        if(c==1):
            with open("arun_Ex.txt") as op:
                for i in op:
                    print(i, end="")
        if (c == 2):
            with open("arun_food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Invalid Input")
a= int(input("Press 1 for lock 2 for retrieve"))
if a==1:
    b=int(input("Press 1 for rohit 2 for neeraj 3 for yattu"))
    take(b)
else:
    b = int(input("Press 1 for rohit 2 for neeraj 3 for yattu"))
    retrieve(b)