# loops 


am_i_alive = True
Age =0

#while loop
while am_i_alive:
    print("My age is ",Age)
    Age+=1
    if(Age == 20):
        am_i_alive =False

print("----------- End of while ----------------")

Age =0
#do-while loop
while True:
    print("My age is ",Age)
    Age+=1
    if(Age == 20):
        break

print("----------- End of do-while ----------------")