def insert_sort(arr):
    for location in range(1, len(arr) ):

        temp = arr[location]

        for position in range(location - 1, -1, -1):

            if arr[position] > temp:
                arr[position + 1] = arr[position]
                arr[position] = temp
            else:
                arr[position + 1] = temp
                break

    return arr
