numChars=128
sizeDict=4096
twelveBits =[]
for i in range (0,sizeDict):
  twelveBit = i
  twelveBits.append(twelveBit)
  
strings =[]
for i in range (0, numChars):
  string = chr(i)
  strings.append(string)

for i in range (numChars, sizeDict):
  string = None
  strings.append(string)

dictionary = dict(zip(twelveBits, strings))