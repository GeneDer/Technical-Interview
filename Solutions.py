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


############# For Question 2 #############
def longest_palindrome(a, left_idx, right_idx):
    # find the longest palindrome if centered at idx.
    # idx can be in between elements.
    # left_idx and right_idx are the left and the right element of idx
    l = left_idx
    r = right_idx
    while l >=0 and r < len(a):
        if a[l] == a[r]:
            l -= 1
            r += 1
        else:
            return l,r
    return l,r

def question2(a):
    # make sure a is a string
    if type(a) != str:
        return "Error: a not string!"
    
    # make sure a has at least 2 characters
    if len(a) < 2:
        return a

    # check all possible center of palindrome
    pal_left = 0
    pal_right = 1
    for i in xrange(len(a)-1):
        # check palindrome centered at i
        l,r = longest_palindrome(a, i, i)
        if r-l-1 > pal_right - pal_left:
            pal_right = r
            pal_left = l+1
            
        # check palindrome centered between i and i+1
        l,r = longest_palindrome(a, i, i+1)
        if r-l-1 > pal_right - pal_left:
            pal_right = r
            pal_left = l+1
    return a[pal_left:pal_right]

def test2():
    print "\nTesting 2"
    print "Edge case (not string):", "Pass" if "Error: a not string!" == question2(123) else "Fail"
    print "Edge case (empty string):", "Pass" if "" == question2("") else "Fail"
    print "Case (a = \"a\"):", "Pass" if "a" == question2("a") else "Fail" 
    print "Case (a = \"aa\"):", "Pass" if "aa" == question2("aa") else "Fail"
    print "Case (a = \"ab\"):", "Pass" if "a" == question2("ab") else "Fail"
    print "Case (a = \"aba\"):", "Pass" if "aba" == question2("aba") else "Fail" 
    print "Case (a = \"aaaaaba\"):", "Pass" if "aaaaa" == question2("aaaaaba") else "Fail" 
    print "Case (a = \"abcbaiojadoijaosdj\"):", "Pass" if "abcba" == question2("abcbaiojadoijaosdj") else "Fail" 


############# For Question3 #############
def question3(G):
    pass


############# For Question4 #############
def question4(T, r, n1, n2):
    pass


############# For Question5 #############
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def get_length(ll):
    # get the length of ll
    # also checking whether the linked list is circular
    # return -1 if the linked list is circular

    # length == 1
    if ll.next == None:
        return 1
    
    length_ll = 0
    current_node = ll
    current_node2 = ll.next
    while current_node != None and current_node != current_node2:
        current_node = current_node.next
        if current_node2 != None:
            current_node2 = current_node2.next
        if current_node2 != None:
            current_node2 = current_node2.next
        length_ll += 1

    if current_node == None:
        return length_ll
    else:
        return -1

def question5(ll, m):
    # make sure ll is a Node
    if type(ll) != Node:
        return "Error: ll not a Node!"

    # make sure m is an integer
    if type(m) != int:
        return "Error: m not an integer!"
    
    # get the length of ll
    length_ll = get_length(ll)

    # make sure ll is not circular
    if length_ll == -1:
        return "Error: circular linked list!"
        
    # make sure m is less than or equal to the length of ll
    if length_ll < m:
        return "Error: m greater than the length of ll!"
    
    # traverse to the last mth element
    current_node = ll
    for i in xrange(length_ll - m):
        current_node = current_node.next
        
    return current_node.data

def test5():
    n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2
    
    print "\nTesting 5"
    print "Edge case (ll not Node):", "Pass" if "Error: ll not a Node!" == question5(123, 111) else "Fail"
    print "Edge case (m > length of ll):", "Pass" if "Error: m greater than the length of ll!" == question5(n1, 6) else "Fail"
    print "Case (ll = n1 and m = 3):", "Pass" if 3 == question5(n1, 3) else "Fail" 
    n5.next = n1
    print "Case (circular linked list):", "Pass" if "Error: circular linked list!" == question5(n1, 3) else "Fail" 

#test1()
#test2()
#test3()
#test4()
test5()
