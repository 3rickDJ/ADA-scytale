import time 
def wordBreak(dictionary, str, lookup, result):
    n = len(str)

    if n ==0:
        return True

    if lookup[n] == -1:
        lookup[n] = 0
        for i in range(1, n +1):
            prefix = str[:i]
            if (prefix in dictionary and wordBreak(dictionary, str[i:], lookup, result)):
                lookup[n] = 1
                result.insert(0, prefix)
                return True

    return lookup[n] == 1

if __name__ == '__main__':
    start = time.time()
    dictionary = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "me", "you", "we", "to", "with", "please", "help", "write", "read", "think", "apples", "bananas", "melons", "mangoes", "mushrooms", "strawberries", "can", "give", "and", "not", "do", "want", "build", "together", "houses"] 

    # sample scytale ciphertext 
    input = "dbtheouoevyigleolepnudtmmwhheaaoegnnurigtsavoteneeosdss"
    
    now = 0
    for i in range(1, len(input) -1):
        str= ""
