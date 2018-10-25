import math
#shmuel padwa
#liam and alex gave me the problem 4^x+5^X=189
#obvious answer x=3
#they want a geenral solution, but closed form cant be found
#trancendental function
#so we out here trying to make a decent algorithm
a = input("give me the a in a^x+b^x=c")
b = input("give me the b in a^x+b^x=c")
c = input("give me the c in a^x+b^x=c")
# 7 8 and 9 just take the input
if a > b: #this if statement will find the higher of the inputs and get a starting point
  val = float(math.log(float(c),float(a)))
elif b > a:
  val = float(math.log(float(c),float(b)))
attempts = 0 
error = 100.0
while abs(error) > 0.05: #arbitrarily chosen, change to make more precise if you want.
  print("val is " +str(val)) #prints the value after each round
  attempts = attempts + 1 #increments the number of tries
  currtotal = (float(a))**val + (float(b))**val 
  percent = (100 * (currtotal-float(c))/float(c))
  if currtotal > float(c):
    print("On attempt "+ str(attempts)+ ", the value of the  function was "+ str(currtotal) + " while c is " + c +", so the algorithm was off by "+ str(percent) + "%")
    val = val * ((100 - percent/10)/100)
    error = percent
  elif currtotal < float(c):
    print("On attempt "+ str(attempts)+ ", the value of the  function was "+ str(currtotal) + " while c is " + c +", so the algorithm was too low by "+ str(abs(percent)) + "%")
    val = val * ((100 + abs(percent)/10)/100)
    error = percent
  elif currtotal == float(c):
    print("hooray!! the correct value of x is " + str(val))
  if attempts == 12: #feel free to change, just make sure not to brick your machine
    break

print ("So the answer is that x = " + str(val) + " within an error of " + str(abs(error)) + " percent" )
