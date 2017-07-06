import readKeys
import dictionary
import editDictionary

def decompressFileSection(c, fileSection):
    keyList = readKeys.readKeys(fileSection)
    outputString ="";
    for i in range(len(keyList)-1):
        #add to dictionary
        #note: adding to output string after creating dictionary messes up when the dictionary resets
        c["dictionary"] = editDictionary.editDictionary(c, keyList[i], keyList[i+1])
        
        #print values to string 
        c["outputString"] += c["dictionary"][keyList[i]]
        
        firstKeyToAdd =256;
        c["keyToAdd"] = updateKeyToAdd(c, firstKeyToAdd)
            
    return {"outputString" : c["outputString"],
        "keyToAdd" : c["keyToAdd"],
        "dictionary": c["dictionary"],
        "lastValue": keyList[len(keyList)-1] }
    
def updateKeyToAdd(c, firstKeyToAdd):   
    c["keyToAdd"] += 1
    if (c["keyToAdd"]==4096): 
        c["dictionary"] = dictionary.dictionary
        c["keyToAdd"] = firstKeyToAdd
    return c["keyToAdd"]