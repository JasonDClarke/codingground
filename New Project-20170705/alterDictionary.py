import dictionary
import readKeys
keyList = (readKeys.readKeys("compressedfile1.z", 20 ))
mutableDictionary = dictionary.dictionary

firstKeyToAdd = 256;
keyToAdd = firstKeyToAdd
for index, key in keyList:
    mutableDictionary[keyToAdd] = mutableDictionary[key] + mutableDictionary[keyList[index+1]]
    keyToAdd += 1
    