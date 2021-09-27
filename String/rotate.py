def rotate(pixels):

    for pixel in range(len(pixels)):
        swap(pixels[pixel][0],pixels[pixel][3])
        swap(pixels[pixel][1],pixels[pixel][2])

    return pixels

def swap(arr_1, arr_2):

    for i in range(len(arr_1)):
        temp = arr_1[i]
        arr_1[i] = arr_2[i]
        arr_2[i] = temp
    
list_1 = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
list_2 = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
list_3 = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
arr = [ list_1, list_2, list_3]
print(rotate(arr))

#rotation of a pixels:
# temp = top[i]
# top[i] = left[i]
#left[i] = bottom[i]
#bottom[i] = right[i]
#right[i] = temp 