import math
import random

aprep = random.randint(0, 999999)
adec = aprep / (1000000)
aint = float(random.randint(1, 9))
a = aint + adec
print ("a is " + str(a))
bprep = random.randint(0, 999999)
bdec = bprep / (1000000)
bint = float(random.randint(1, 9))
b = bint + bdec
print ("b is " + str(b))
cprep = random.randint(0, 999999)
cint = float(random.randint(0, 999999))
cdec = cprep / (1000000)
c = cint + cdec
print ("c is " + str(c))
if a > b: #this if statement will find the higher of the inputs and get a starting point
  val = float(math.log(float(c),float(a)))
elif b > a:
  val = float(math.log(float(c),float(b)))
attempts = 0 
error = 100.0
while abs(error) > 0.0005: #arbitrarily chosen, change to make more precise if you want.
#the higher the value of c, and the greater the absolute difference between a and b, the closer to zero I would recommend this number
  print("val is " +str(val)) #prints the value after each round
  attempts = attempts + 1 #increments the number of tries
  currtotal = (float(a))**val + (float(b))**val 
  percent = (100 * (currtotal-float(c))/float(c))
  if currtotal > float(c):
    print("On attempt "+ str(attempts)+ ", the value of the  function was "+ str(currtotal) + " while c is " + str(c) +", so the algorithm was off by "+ str(percent) + "%")
    val = val * ((100 - percent/10)/100)
    error = percent
  elif currtotal < float(c):
    print("On attempt "+ str(attempts)+ ", the value of the  function was "+ str(currtotal) + " while c is " + str(c) +", so the algorithm was too low by "+ str(abs(percent)) + "%")
    val = val * ((100 + abs(percent)/10)/100)
    error = percent
  elif currtotal == float(c):
    print("hooray!! the correct value of x is " + str(val))
  if attempts == 12: #feel free to change, just make sure not to brick your machine
    break

print ("So the answer is that x = " + str(val) + " within an error of " + str(abs(error)) + " percent" )

