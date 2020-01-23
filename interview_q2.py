"""
Problem:
Find the occurences of the words in a given string:
example:  s= "Hi, Peter! Hi Jon!",  words = {Peter, Hi, Mary};
"""
# desired return  {Peter:[4], Hi: [0, 11]}

# return #1 {Peter:[4], Hi: [0, 11], Mary: []} ,  useless information for Mary input
# return #2 [True, True, False]    information loss,  where is the occurence, how many times?
# return #3 [1, 2, 0]    information loss,  where is/are the occurence(s)?


def solution_by_looping_the_dictionary(s: String, words: List[String]) -> dict:

    # naive way to solve my_strstr, can do KMP, Rabin-Karp
    def my_strstr(haystack, needle):
        ans = []
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                ans.append(i)
        return ans

    ret = {}
    for word in set(words):
        indexes = my_strstr(s, words):
        if indexes:
            ret[word] = indexes
    return ret
