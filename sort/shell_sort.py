
def shell_sort(arr):
    h = int(len(arr) / 2)

    while h > 0:
        print('h:', h)
        for start in range(h):
            print('start:', start)

            cnt = 0
            while len(arr) > start + (cnt + 1) * h:
                cur = cnt * h + start
                nex = (cnt + 1) * h + start
                temp = arr[cur]
                if arr[nex] < temp:
                    arr[cur] = arr[nex]
                    arr[nex] = temp
                cnt += 1
        h = int(h / 2)

    return arr

