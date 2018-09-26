from turtle import *

speed(10)





for a in range(3,7):
    
    for b in range(a):
    
        forward(100)
        
        left(360/a)
        if a%2 == 0:
            color("red")
        else:
            color("blue")    
        

    

    
    

mainloop()