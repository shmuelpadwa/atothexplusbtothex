import math
import random

attlist = []
xlist = []
tries = 50
while tries > 0:

  aprep = random.randint(0, 999999)
  adec = aprep / (1000000)
  aint = float(random.randint(0, 9))
  a = aint + adec
  bprep = random.randint(0, 999999)
  bdec = bprep / (1000000)
  bint = float(random.randint(0, 9))
  b = bint + bdec
  cprep = random.randint(0, 999999)
  cint = float(random.randint(0, 999999))
  cdec = cprep / (1000000)
  c = cint + cdec
  if a > b:
    val = float(math.log(float(c),float(a)))
  elif b > a:
    val = float(math.log(float(c),float(b)))
  attempts = 0 
  error = 100.0
  while abs(error) > 0.005: #arbitrarily chosen,
    attempts = attempts + 1 #increments the number of tries
    currtotal = (float(a))**val + (float(b))**val 
    percent = (100 * (currtotal-float(c))/float(c))
    if currtotal > float(c):
      val = val * ((100 - percent/10)/100)
      error = percent
    elif currtotal < float(c):
      val = val * ((100 + abs(percent)/10)/100)
      error = percent
    if attempts == 20: 
      break

  xlist.append(val)
  attlist.append(attempts)
  tries = tries - 1
print(xlist)
print(attlist)
print("average x was " + str((sum(xlist)/len(xlist))))
print("average number of attempts was " + str((sum(attlist)/len(attlist))))
