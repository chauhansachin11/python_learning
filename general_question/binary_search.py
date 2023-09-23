def searchBinary(arr, l, h, k):
    if(l<=h):
        mid = l + (h-l)//2
        if(arr[mid] == k):
            return(mid)
        elif(arr[mid] > k):
            return(searchBinary(arr,l,mid-1,k))
        else:
            return(searchBinary(arr,mid+1,h,k))
    else:
        return(-1)


class Solution:
    
	def binarysearch(self, arr, n, k):
		# code here
		res = searchBinary(arr,0,n-1, k)
		return res


ob = Solution()
arr = [1, 2, 3, 4, 5]
print(ob.binarysearch(arr, 5, 10))