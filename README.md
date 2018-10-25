# atothexplusbtothex
two variables . py will solve a^x+b^x=c for positive, even if not integer, a, b, and c.

three variable . py will do the same for a^x+b^x+c^x=d

In either case, more accurate within fewer attempts the higher the value of the final variable.

two var random . py randomizes a and b between 0.000001 and 9.999999 and c between 0.000001 and 999999.999999

data creata . py allows you to keep track of the x values and number of attempts needed to reach. Do what you want with the data.

I tested the data creata in 50 tries a piece. I noticed that in about 1 of every 100 tries, x was incredible high, like 10 to the 30 level high. Turns out, this isn't about 1 in 100 tries, but exactly! Why? When the non-decimal part of both a and b was zero, this would occur. I have since fixed this issue.

11:52 PM-added a standard deviation calculator for attempts and x values. I'm going to bed.
