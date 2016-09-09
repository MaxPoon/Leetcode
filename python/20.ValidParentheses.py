class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isMatch(a,b):
            if (a=="(" and b==")") or  (a=="[" and b=="]") or  (a=="{" and b=="}"):
                return True
            else:
                return False
                
        openstack = []
        for i in range(len(s)):
            if(s[i] == "(" or s[i]=="[" or s[i]=="{"):
                openstack.append(s[i])
            elif not openstack:
                return False
            else:
                c = openstack.pop()
                if not isMatch(c,s[i]):
                    return False
        if openstack:
            return False
        else: 
            return True
