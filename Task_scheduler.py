// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None


// Your code here along with comments explaining your approach:
In this problem we first calculate the frequency of the largest occuring element and how many times the freq has occured.Then we using the above two parameters we calculate partitions,emptyslots,pending tasks,Idle task.with the above calculated parameters we can calculate the least number of intervals to finish the given tasks.

# Time complexity --> o(n)
#space compelxity --> o(1)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n==0:
            return len(tasks)
        d=dict()
        for i in tasks:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        maxi=float("-inf")
        #creating a dictionary and calculating the max occuring freq and how many times they have occured.
        for key,value in d.items():
            if value>maxi:
                maxi=value
                count=1
            elif value==maxi:
                count=count+1
        
        maxfreq=maxi
        # print(maxfreq)
        partitions=maxfreq-1
        # print(partitions)
        emptyslots=partitions * (n-(count-1))
        # print(emptyslots)
        pendingtasks=len(tasks)-(maxfreq*count)
        # print(pendingtasks)
        idle=emptyslots-pendingtasks
        if idle<0:
            idle=0
        # print(idle)
        return len(tasks)+idle
                