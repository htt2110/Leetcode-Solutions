'''
Given a string s, find the length of the longest substring
 without repeating characters.
'''
def lengthOfLongestSubstring(s: str) -> int:
        st = list(s)
        subStr = ''
        lens = []
        for s in st:
            if s not in subStr:
                subStr += s
                    
            else: 
                ind = subStr.index(s)
                subStr = subStr[ind+1:] + s
            
            lens.append(len(subStr))
            
    
        return max(lens, default=0)