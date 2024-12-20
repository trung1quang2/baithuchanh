print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')

def bubblesort(nlist):
    """Hàm sắp xếp nổi bọt"""
    n = len(nlist)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True

        if not swapped:
            break

    return nlist
