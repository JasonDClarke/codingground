import readKeys2
import dictionary
import editDictionary

def decompressFileSection(fileSection, mutableDictionary, keyToAdd):
    keyList = readKeys2.readKeys(fileSection)
    outputString ="";
    for i in range(len(keyList)-1):
        #add to dictionary
        #note: adding to output string after creating dictionary messes up when the dictionary resets
        mutableDictionary = editDictionary.editDictionary(mutableDictionary, keyList[i], keyList[i+1], keyToAdd)
        
        #print values to string 
        outputString += mutableDictionary[keyList[i]]
        keyToAdd += 1
        
        #when dictionary full, reset ditionary
        if (keyToAdd==4096): 
            mutableDictionary = dictionary.dictionary
            keyToAdd = firstKeyToAdd
    return [outputString, mutableDictionary, keyToAdd]