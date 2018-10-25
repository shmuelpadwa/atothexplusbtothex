import math
#shmuel padwa, python 3
#liam and alex gave me the problem 4^x+5^X=189
#obvious answer x=3
#they want a geenral solution, but closed form cant be found
#trancendental function
#so we out here trying to make a decent algorithm
a = input("give me the a in a^x+b^x+c^x=d")
b = input("give me the b in a^x+b^x+c^x=d")
c = input("give me the c in a^x+b^x+c^x=d")
d = input("give me the d in a^x+b^x+c^x=d")
# 7 8 and 9 just take the input
if a > b and a > c: #this if statement will find the higher of the inputs and get a starting point
  val = float(math.log(float(d),float(a)))
elif b > a and b > c:
  val = float(math.log(float(d),float(b)))
elif c > a and c > b:
  val = float(math.log(float(d),float(c)))
attempts = 0 
error = 100.0
while abs(error) > 0.0005: #arbitrarily chosen, change to make more precise if you want.
#the higher the value of c, and the greater the absolute difference between a and b, the closer to zero I would recommend this number
  print("val is " +str(val)) #prints the value after each round
  attempts = attempts + 1 #increments the number of tries
  currtotal = (float(a))**val + (float(b))**val + (float(c))**val 
  percent = (100 * (currtotal-float(d))/float(d))
  if currtotal > float(d):
    print("On attempt "+ str(attempts)+ ", the value of the  function was "+ str(currtotal) + " while d is " + d +", so the algorithm was off by "+ str(percent) + "%")
    val = val * ((100 - percent/10)/100)
    error = percent
  elif currtotal < float(d):
    print("On attempt "+ str(attempts)+ ", the value of the  function was "+ str(currtotal) + " while c is " + d +", so the algorithm was too low by "+ str(abs(percent)) + "%")
    val = val * ((100 + abs(percent)/10)/100)
    error = percent
  elif currtotal == float(d):
    print("hooray!! the correct value of x is " + str(val))
  if attempts == 20: #feel free to change, just make sure not to brick your machine
    break

print ("So the answer is that x = " + str(val) + " within an error of " + str(abs(error)) + " percent" )
