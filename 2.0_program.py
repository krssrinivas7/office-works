sum = 10
def calculate() :
    global sum
    sum = sum + 20
    currentSum = 200
    totalSum = sum + currentSum
    print (totalSum)
calculate();
print(sum)