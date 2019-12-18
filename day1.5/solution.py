# python 3


f = open('input.txt', 'r')
massArr = f.readlines()
f.close()


# fuel per load = loadweight / 3 - 2 
total = 0
for mass in massArr:
    fuelReq = int((int(mass) / 3) - 2)
    while True:
        total += fuelReq
        fuelReq = int((fuelReq / 3)) - 2

        if(fuelReq < 1): 
            break
        


print("Total: " + str(total))

