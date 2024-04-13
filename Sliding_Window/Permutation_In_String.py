class Solution(object):
    def frequency_map(self,s1):
        dictt = {}
        for word in s1:
            dictt[word] = dictt.get(word, 0)+1
        return dictt

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        windowsize = len(s1)
        print(windowsize)
        
        for i in range(len(s2)-windowsize+1):
            if self.frequency_map(s1) == self.frequency_map(s2[i:i+windowsize]):
                return True
        return False


solutionn = Solution()
print(solutionn.checkInclusion("haka", "djlshdlkahabanlks"))
