import pprint

def marge_sort(arr):
    return rec_split(arr)

def rec_split(arr):
    print('rec start')
    pprint.pprint(arr)
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr

    else:
        br = int(len(arr) / 2)
        pprint.pprint(arr[:br])
        pprint.pprint(arr[br:])
        return marge_arr(rec_split(arr[:br]), rec_split(arr[br:]))

def marge_arr(arr1, arr2):
    print('marge start')
    pprint.pprint(arr1)
    pprint.pprint(arr2)

    ret = list()
    len1 = len(arr1)
    len2 = len(arr2)

    i = j = 0
    arr1_val = arr1[i]
    arr2_val = arr2[j]

    while len(ret) < len1 + len2:
        print('arr1:', i, ':', arr1[i])
        print('arr2:', j, ':', arr2[j])

        if arr1_val < arr2_val:
            ret.append(arr1_val)
            if i < len1 - 1:
                i += 1
                arr1_val = arr1[i]
            else:
                arr1_val = float('inf')

        elif arr1_val >= arr2_val:
            ret.append(arr2_val)
            if j < len2 - 1:
                j += 1
                arr2_val = arr2[j]
            else:
                arr2_val = float('inf')
        print('condition:', len(ret) , ':',  len1, ':',  len2)

    return ret
