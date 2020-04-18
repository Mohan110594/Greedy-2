// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None


// Your code here along with comments explaining your approach
In this problem we take a new array and intialise to 1 for every index and check with the left neighbours first.
Then we traverse from the end to check with the right neighbours to check if the current element is greater then the neighbouring element or not.we are making sure that the current element is greater than the neighbouring elements.


# Time complexity --> o(n)
# space complexity --> o(n)
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if ratings==None or len(ratings)==0:
            return 0
        #we start by intializing 1 for each children as each children should have atleast one candy
        out=[1 for i in range(len(ratings))]
        #we start by traversing and we look the left neighbours to see if there is any neighbouring rating greater than the current rating
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                out[i]=out[i-1]+1
        print(out)
        #Then we traverse on the output array from the end to the start to check for any right neighbours.if yes then take the max of current value or the neighbour value+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                out[i]=max(out[i],out[i+1]+1)
        # print(out)
        return sum(out)
        