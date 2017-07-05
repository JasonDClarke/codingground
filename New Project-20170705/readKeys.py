def readKeys(fileName, halfBufferSize): #in bytes 
    keyList=[]
    with open(fileName, "rb") as f:
        bytess = f.read(halfBufferSize*3)
        i=0;
        for byte in bytess:
            if i%3==0:
                twelveBit = byte
            elif i%3==1:
                firstHalfByte = byte >> 4
                twelveBit = (twelveBit<<4) +firstHalfByte
                keyList.append(twelveBit)
                secondHalfByte = byte %16
                twelveBit = secondHalfByte
            elif i%3==2:
                twelveBit = (secondHalfByte<<8) +byte
                keyList.append(twelveBit)
            i+=1
    f.close()
    return keyList