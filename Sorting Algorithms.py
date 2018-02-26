# O(1) space, O(n log(n))
def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        left = quick_sort([i for i in a[1:] if i <= a[0]])
        mid = [a[0]]
        right = quick_sort([i for i in a[1:] if i > a[0]])
        return left + mid + right


# in place quick sort
def qsort(array, start=0, end=None):
    if end is None:  # this just initializes end
        end = len(array) - 1
    if start > end:
        return
    pivot = array[start]  # pick pivot to be the first element
    i, j = start, end
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    qsort(array, start, j)
    qsort(array, i, end)
    return array


# O(n^2) running time
def insertion_sort(a):
    i = 1
    while i < len(a):
        j, x = i - 1, a[i]
        while j >= 0 and a[j] > x:
            a[j+1], a[j] = a[j], a[j+1]
            j -= 1
        i += 1
        a[j+1] = x
    return a


# O(1) space, O(n^2) running time
# can be modified to stop once sorted
def bubble_sort(a):
    for j in range(len(a)-1, 0, -1):
        for i in range(j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            else:
                break
    return a


# O(n^2) finds min on each pass, and performs n passes
def selection_sort(a):
    return [min(a[:len(a)-i]) for i in range(len(a))]


def test(f):
    t1 = list(range(100, 0, -1))
    t2 = list(range(50, 0, -1)) + list(range(100, 50, -1))
    a1 = list(range(1, 101))
    if f(t1) == a1 and f(t2) == a1:
        print("All tests passed\n")
    else:
        print("Something's not right!\n")


