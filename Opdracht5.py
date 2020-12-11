
def list_manipulation(list, command, location, value=None):

    if command == "remove":
        if location == "end":
            end = list[-1]
            list.remove(list[-1])
            return end
        if location == 'beginning':
            begin = list[0]
            list.remove(list[0])
            return begin
    if command == 'add':
        if location == 'end':
            list.append(value)
            return list
        if location == 'beginning':
            list.insert(0,value)
            return list



lit = list_manipulation([1, 2, 3], 'remove', 'end')  # print out: 3
print(lit)

litt = list_manipulation([1, 2, 3], 'remove', 'beginning')  # print out: 1
print(litt)

littt= list_manipulation([1, 2, 3], 'add', 'beginning', 20)  # print out: [20, 1, 2, 3]
print(littt)

litttt= list_manipulation([1, 2, 3], 'add', 'end', 30)  # print out: [1, 2, 3, 30] 
print(litttt)

