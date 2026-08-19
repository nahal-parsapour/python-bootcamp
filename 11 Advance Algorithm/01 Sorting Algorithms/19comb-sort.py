def comb_sort(arr, shrink=1.3):
    n = len(arr)
    gap = n
    swapped = True
    comparisons = 0

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        swapped = False
        for i in range(0, n - gap):
            comparisons += 1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr, comparisons

test = [5, 3, 8, 4, 2]
for factor in [1.3, 1.5, 1.7]:
    arr = test.copy()
    sorted_arr, comps = comb_sort(arr, shrink=factor)
    print(f"shrink={factor} → sorted={sorted_arr}, comparisons={comps}")