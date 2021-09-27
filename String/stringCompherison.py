def stringCheck(a):

    a = list(a)
    count = 1 
    current_letter = a[0]
    arr = []
    print("the len of a is ", len(a))

    for i in range(1, len(a)):
        print("the i is ", i)

        if i == len(a) -1:
            print("it is the last element")
            if current_letter == a[i]:
                count += 1
                arr.append(current_letter)
                arr.append(count)
            else:
                arr.append(current_letter)
                arr.append(count)
                arr.append(a[i])
                arr.append(1)
        else:
            if current_letter == a[i]:
                count += 1
            if current_letter != a[i]:
                arr.append(current_letter)
                arr.append(count)
                current_letter = a[i]
                count = 1
       


    if len(arr) > len(a):
        return ''.join(str(i) for i in a)
    
    return ''.join(str(j) for j in arr)


a = 'aabcnnnca'
print(stringCheck(a))