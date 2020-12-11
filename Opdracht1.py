from random import randint

sick_days = randint(0, 11)

calling_in_sick = False




while (sick_days > 0):

    
    actually_sick = randint(0,1)
    kinda_sick = randint(0,1)
    dont_feel_like_it = randint(0, 1)

    
    print(actually_sick, kinda_sick, dont_feel_like_it)
    print(sick_days)


    if actually_sick == 1 & sick_days > 0:
        calling_in_sick = True
        sick_days -= 1

    elif kinda_sick == 1 & dont_feel_like_it == 1 & sick_days > 0:
        calling_in_sick = True
        sick_days -= 1

    else:
        calling_in_sick = False
        print(f'Will I call in sick? {calling_in_sick}. Now I still have {sick_days} left.')
        continue


    print(f'Will I call in sick? {calling_in_sick}. Now I still have {sick_days} left.')



