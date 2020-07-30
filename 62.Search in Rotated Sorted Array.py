class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A)==0:
            return -1
        if len(A)==1 and A[0]==target:
            return 0
        if len(A)==2:
            if A[0]==target:
                return 0
            elif A[1]==target:
                return 1
            else:
                return -1
        start=0
        end=len(A)-1
        while start+1<end:
            mid=start+(end-start)//2
            if A[mid]==target:
                return mid
            elif A[mid]>target:
                if (A[mid]-A[-1])*(target-A[-1])>0:
                    end=mid
                else:
                    start=mid
            else:
                if (A[mid]-A[-1])*(target-A[-1])<0:
                    end=mid
                else:
                    start=mid
        if A[start]==target:
            return start
        elif A[end]==target:
            return end
        else:
            return -1
