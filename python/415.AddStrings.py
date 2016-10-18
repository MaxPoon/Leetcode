class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s = ""
        c = 0
        while len(num1) or len(num2) or c:
            n1 = ord(num1[-1])-48 if len(num1) else 0
            n2 = ord(num2[-1])-48 if len(num2) else 0
            n=n1+n2+c
            c = int(n>=10)
            n=n%10
            s = str(n)+s
            num1=num1[:-1]
            num2=num2[:-1]
        return s
