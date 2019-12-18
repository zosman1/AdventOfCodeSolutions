# python 3


f = open('input.txt', 'r')
massArr = f.readlines()
f.close()


# fuel per load = loadweight / 3 - 2 
total = 0
for mass in massArr:
    total += int((int(mass) / 3) - 2)

print("Total: " + str(total))

