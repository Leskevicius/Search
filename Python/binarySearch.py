#the list must be sorted! I'd add a sort algorithm but that would break the OOP!
#beauty of O(log(n))
class binarySearch(object):
    #returns the index of the element in the array.
    #returns -1 if not found
    def search(self, myList, element):
        n = len(myList)
        low = 0;
        high = n;
        while ( low <= high ):
            mid = low + ( high - low ) / 2
            #case 1 : we have found the element
            if element == myList[ mid ]:
                return mid
            #case 2 : we have searched the whole list and
            #it is not present
            elif mid >= n - 1 or mid <= 0:
                return -1
            #case 3 : the element we are looking for is bigger than the
            #element we are looking at currently
            elif element > myList[ mid ]:
                low = mid
            #case 4 : the element we are looking for is smaller than the
            #element we are looking at currently
            elif element < myList[ mid ]:
                high = mid
