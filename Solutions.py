# Gene Der Su wrote for Udacity technical interview

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
    
    # store counts of characters
    char_counts = {}

    # add all counts of characters in t
    for i in t:
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1

    # manually go throuh first len(t) characters
    for i in xrange(len(t)):
        if s[i] not in char_counts:
            char_counts[s[i]] = -1
        else:
            char_counts[s[i]] -= 1
            if char_counts[s[i]] == 0:
                char_counts.pop(s[i])
                
        if len(char_counts) == 0:
            return True
        print char_counts
    
    # loop through the rest of sets
    for i in xrange(len(t), len(s)):
        if s[i] not in char_counts:
            char_counts[s[i]] = -1
        else:
            char_counts[s[i]] -= 1
            if char_counts[s[i]] == 0:
                char_counts.pop(s[i])

        j = i - len(t)
        if s[j] not in char_counts:
            char_counts[s[i]] = -1
        else:
            char_counts[s[j]] += 1
            if char_counts[s[j]] == 0:
                char_counts.pop(s[j])
        if len(char_counts) == 0:
            return True
        print char_counts, s[i], s[j]

    # no matching anagram of t in consecutive substring of s
    return False

def test1():
    print "Testing 1"
    print "Example test case (udacity, ad):", "Pass" if True == question1("udacity", "ad") else "Fail"
    print "Edge case (not string):", "Pass" if "Error: s not string!" == question1(123, 1.23) else "Fail"
    print "Edge case (t longer than s):", "Pass" if False == question1("ad", "udacity") else "Fail"
    print "Case (s == t):", "Pass" if True == question1("abcd", "abcd") else "Fail"
    print "Case (very long string):", "Pass" if True == question1("zxcvbnm,.asdfghjkertyuqwertyuifghnbvcfghnyfurf6e4dsxerzqwewaestyfgihbkjhgcthgbklhit75ydxtyhgfvighkjnolkvtyyc545768i8yhonjvctexdfujhvtetrydfjvc",
                                                                  "fa.sd") else "Fail"
    print "Case (repeated substrings):", "Pass" if True == question1("abcdabcdabcdabcdabcdabcdeabcd", "abce") else "Fail"
    print "Case (none consecutive matching substrings):", "Pass" if False == question1("abeeeeeeecd", "abcd") else "Fail"




print question1("abcdeabcd", "abce")


#test1()
