def nthElementFromRight(self, head, n):
 # phase I
    aheadPtr = head
    while n > 0:
        aheadPtr = aheadPtr.next
        n -= 1

    # phase II
    behindPtr = head
    while behindPtr:
        behindPtr = behindPtr.next
        aheadPtr = aheadPtr.next
    return behindPtr