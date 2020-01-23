"""
Problem:
Find the occurences of the words in a given string:
example:  s= "Hi, Peter! Hi Jon!",  words =  ["Peter", "Hi", "Mary"]
"""
# desired return  {Peter:[4], Hi: [0, 11]}

# return #1 {Peter:[4], Hi: [0, 11], Mary: []} ,  useless information for Mary input
# return #2 [True, True, False]    information loss,  where is the occurence, how many times?
# return #3 [1, 2, 0]    information loss,  where is/are the occurence(s)?
import collections
class InterviewQuestion:

    def __init__(self, s, words):
        self.s = s
        self.words = words

    def solution_by_looping_the_dictionary(self) -> dict:        
        # naive way to solve my_strstr, can do KMP, Rabin-Karp
        def my_strstr(haystack, needle):
            ans = []
            m, n = len(haystack), len(needle)
            for i in range(m - n + 1):
                if haystack[i:i+n] == needle:
                    ans.append(i)
            return ans

        s, words = self.s, self.words
        ret = collections.defaultdict(list)
        for word in set(words):
            indexes = my_strstr(s, word)
            if indexes:
                ret[word] = indexes
        return ret


    def solution_using_sliding_window_with_fixed_length_word(self) -> dict:

        # find the maxlenght of the word in the words
        s, words = self.s, self.words
        s_len = len(s)
        max_len = max(map(len, words))
        word_dict_group_by_len = collections.defaultdict(set)
        ret = collections.defaultdict(list)
        
        for word in set(words):
            word_dict_group_by_len[len(word)].add(word)

        for l in range(1, max_len+1):
            for idx in range(0, s_len - l):                
                w = s[idx:idx+l]
                if w in word_dict_group_by_len[l]:
                    ret[w].append(idx)
        return ret


test = InterviewQuestion("Hi, Peter! Hi Jon!",  ["Peter", "Hi", "Mary", "on"])

print(test.solution_by_looping_the_dictionary())
print(test.solution_using_sliding_window_with_fixed_length_word())
    
