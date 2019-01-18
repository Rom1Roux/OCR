carteJ1 = input()
carteJ2 = input()
count2 = 0
stop = True

if len(carteJ1) > len(carteJ2):
    count = len(carteJ2)
else:
    count = len(carteJ1)
        
for loop in range (count - 1):
    if carteJ1[loop] > carteJ2[loop] and stop == True:
        print("2")
        print(count2)
        stop = False
    if carteJ1[loop] < carteJ2[loop] and stop == True:
        print("1")
        print(count2)
        stop = False
    if carteJ1[loop] == carteJ2[loop] and stop == True:
        count2 = count2 + 1