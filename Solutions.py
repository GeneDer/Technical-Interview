# Gene Der Su wrote for Udacity technical interview

############# For Question 1 #############
def compare(set1, set2):
    # check if set1 and set2 are equal
    for i in set1:
        if i in set2:
            if set1[i] == set2[i]:
                set2.pop(i)
            else:
                return False
        else:
            return False
    if len(set2) == 0:
        return True
    else:
        return False

def question1(s, t):
    # assuming substring need to be consecutive

    # make sure s is a string
    if type(s) != str:
        return "Error: s not string!"

    # make sure t is a string
    if type(t) != str:
        return "Error: t not string!"

    # make sure there are s has at least as much characters as t
    if len(s) == 0 or len(s) < len(t):
        return False

    # if t is empty, the answer should alwasy be True
    if len(t) == 0:
        return True

    # store all character counts of t
    char_counts_t = {}
    for i in t:
        if i in char_counts_t:
            char_counts_t[i] += 1
        else:
            char_counts_t[i] = 1

    # store character counts of first len(t) charactersof s
    char_counts_s = {}
    for i in xrange(len(t)):
        if s[i] in char_counts_s:
            char_counts_s[s[i]] += 1
        else:
            char_counts_s[s[i]] = 1
    
    # compare if they are anagrams
    if compare(char_counts_t, char_counts_s.copy()):
        return True

    # compare the rest of sets
    for i in xrange(len(t), len(s)):

        # add new character in the set
        if s[i] in char_counts_s:
            char_counts_s[s[i]] += 1
        else:
            char_counts_s[s[i]] = 1

        # remove old character in the set
        j = i - len(t)
        char_counts_s[s[j]] -= 1
        if char_counts_s[s[j]] == 0:
            char_counts_s.pop(s[j])

        
        # compare if they are anagrams
        if compare(char_counts_t, char_counts_s.copy()):
            return True

    # no matching anagram of t in consecutive substring of s
    return False

def test1():
    print "Testing 1"
    print "Example test case (udacity, ad):", "Pass" if True == question1("udacity", "ad") else "Fail"
    print "Edge case (not string):", "Pass" if "Error: s not string!" == question1(123, 1.23) else "Fail"
    print "Edge case (t longer than s):", "Pass" if False == question1("ad", "udacity") else "Fail"
    print "Case (s equal to t):", "Pass" if True == question1("abcd", "abcd") else "Fail"
    print "Case (very long string):", "Pass" if True == question1("zxcvbnm,.asdfghjkertyuqwertyuifghnbvcfghnyfurf6e4dsxerzqwewaestyfgihbkjhgcthgbklhit75ydxtyhgfvighkjnolkvtyyc545768i8yhonjvctexdfujhvtetrydfjvc",
                                                                  "fa.sd") else "Fail"
    print "Case (repeated substrings):", "Pass" if True == question1("abcdabcdabcdabcdabcdabcdeabcd", "abce") else "Fail"
    print "Case (none consecutive matching substrings):", "Pass" if False == question1("abeeeeeeecd", "abcd") else "Fail"

test1()


############# For Question 2 #############
def question2(a):
    pass
