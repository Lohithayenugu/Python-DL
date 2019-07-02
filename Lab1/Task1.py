def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        res=[]
        dict = {}
        str = ""
        final_str = ""
        i = 0
        while i < len(s):
            if s[i] in dict:
                if len(str) > len(final_str):
                    final_str = str
                    res = [(final_str, len(final_str))]
                elif len(str) == len(final_str):
                    res.append((str, len(str)))
                i = dict[s[i]]
                dict.clear()
                str = ""
            else:
                dict[s[i]] = i
                str = str + s[i]

            i = i + 1
        if len(str) > len(final_str):
            final_str = str
            res=[(final_str,len(final_str))]
        elif len(str)== len(final_str):
            res.append((str,len(str)))
        return res
str=input("Enter the string")
print(lengthOfLongestSubstring(str))
