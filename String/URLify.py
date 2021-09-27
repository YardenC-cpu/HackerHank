def urlify(s):

    if len(s) <= 1:
        return s

    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == " ":
            s_list[i] = "%20"
        
    return ''.join(s_list)

s = 'Or and Yarden'
print(urlify(s))