import keyword

def contains_keyword(*sentences):
    value = None

    for sentence in sentences:
        if keyword.iskeyword(sentence):
            value = True
            break
        else:
            value = False
    return value
    
    

 
answer = contains_keyword('hello', 'goodbye')  # print out: False 
print(answer)

answer2 = contains_keyword('def', 'haha', 'lol', 'chickens are evil', 42)  # print out: True 
print(answer2)

answer3 = contains_keyword('four', 'for', 'if')  # print out: True 
print(answer3)

answer4 = contains_keyword('blabla', 'doggo', 'crab', 'anchor')  # print out: False 
print(answer4)

answer5 = contains_keyword('grizzly', 'ignore', 'return', 'False')  # print out: True
print(answer5)
