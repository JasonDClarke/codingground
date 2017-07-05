def editDictionary(dictionary, currentKey, nextKey, keyToAdd):
    #if know value of next key, write value of new key as current value plus first character of next value
    if (dictionary[nextKey] != None):
        dictionary[keyToAdd] = dictionary[currentKey] + dictionary[nextKey][0]
    #if don't know value of next key, write value of new key as current value plus first character of current value
    #if you don't know the next key, the key you were about to create must have been used. The first character of
    #the value of this key is the first character of the value of the current key
    else:
        dictionary[keyToAdd] = dictionary[currentKey] + dictionary[nextKey][0]
    return dictionary