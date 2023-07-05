# Sinple and cool Calculator in Python
#Author : Muhammad Shariq Shafiq

arr= []
#Hiatory Function 
def history():
    print("History \n", arr)
    
    #Main Function 
while True:
    n = int(eval(input ("Enter Expression or (0 to terminate with history : ")))
    print("Answer = ", n)
    arr.append(n)
    if n == 0:
        history()
