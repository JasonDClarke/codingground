numChars=256
sizeDict=4096

strings =[]
for i in range (0, numChars):
  string = chr(i%128) #a hack fix
  strings.append(string)

for i in range (numChars, sizeDict):
  string = None
  strings.append(string)

dictionary = strings