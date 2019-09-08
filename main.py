i=1
x = int(input("Enter the number:")) #generate prime number that we want to search
counter = 0
while True:
    c=0;
    for j in range (1, (i+1), 1): #iteration
        a = i%j
        if (a==0):
            c = c+1
    if (c==2): #first prime number is 2
        print (i)
        counter = counter + 1 #addition when get prime number
        if counter >= x:  
            break
    i=i+1
