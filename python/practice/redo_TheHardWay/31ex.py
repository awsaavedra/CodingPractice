print "You enter a dark room with two doors. Do you go through door #1 or #2?"

door = raw_input("> ")

if door == "1":
  print "There's a giant bear eating a cake. What do you do?"
  print "1. Take the cake."
  print "2. Scream at the bear."
  
  bear = raw_input(" >")

  if bear == "1":
    print "The bear eats your face off. Good job!"
  elif bear == "2":
    print "The bear eats your legs off. Good job!"
  else:
    "Well doing %s  probably better. Bear runs away." % bear
elif door == "2":
  print "You stare into the endless abyss that's cthulu's retina."
  

else:
  print "over exercise, I know this bruh"
  
