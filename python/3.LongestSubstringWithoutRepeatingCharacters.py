class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1, p2 = 0,0
        h = {}
        l, l_max = 0,0
        while p2<len(s):
            if s[p2] not in h or h[s[p2]]==-1:
                h[s[p2]]=p2
                l+=1
                p2+=1
            else:
                l_max = max(l,l_max)
                p = h[s[p2]]+1
                while p1<p:
                    h[s[p1]]=-1
                    p1+=1
                h[s[p2]] = p2
                l=p2-p1+1
                p2+=1
        return max(l_max,l)