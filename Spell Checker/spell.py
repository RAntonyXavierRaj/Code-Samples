# spell checker based on Peter Norvig's Algorithm
# I have modified it for my requiremets 
# I created a similar code in my previous work, I have recreated it in a short time to show a coding example.

import re
from collections import Counter

# finding number of word occurence in the training data
def words(text): return re.findall(r'\w+', text.lower())

#Finding total words
WORDS = Counter(words(open('NASDAQ.txt').read()))

# Finding probability
def P(word, N=sum(WORDS.values())): 
    prob = WORDS[word] / N
    return prob

# Spelling correction with highest probability
def correction(word): 
    x = candidates(word)
    return max(x, key=P)

# Generate all possible corretions in 3 levels
def candidates(word): 
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or edits3(word) or [word])

# Known words in the training data
def known(words): 
    most_used = set(w for w in words if w in WORDS)
    return most_used

# edits which are 1,2,3 edits away
def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def edits3(word): 
    "All edits that are two edits away from `word`."
    return (e3 for e1 in edits1(word) for e2 in edits1(e1) for e3 in edits1(e2))

print (correction(input("Enter a company name : ")))

