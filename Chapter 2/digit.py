def digit(n):
    while(n != 0):
       d=n%10   # "%" ye mod hai jo ki percent bhi hai ye divide karne par remender deta hai. 
       print(d)
       n = n//10   # '/'  python me ye divide karke point value deta hai "//" perfect value deta hai aur quotient return karta hai .
    #print(n)   
n=int(input("Enter a num:")) 
digit(n)             
    
    

 
