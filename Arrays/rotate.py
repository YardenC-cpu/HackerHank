def rotate(pixels):
    for pixel in range(len(pixels)):
        swap_function(pixels[0],pixels[3])
        swap_function(pixels[1],pixels[2])

    return pixels

def swap_function(arr_1, arr_2):
    for i in range(len(arr_1)):
        temp = arr_1[i]
        arr_1[i] = arr_2[i]
        arr_2[i] = temp
    
list_1 = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
list_2 = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
list_3 = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
#arr = [list_1, list_2, list_3]
arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(arr))

#rotation of a pixels:
# temp = top[i]
# top[i] = left[i]
#left[i] = bottom[i]
#bottom[i] = right[i]
#right[i] = temp 