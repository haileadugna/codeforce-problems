from collections import Counter

test = int(input())

for _ in range(test):
    n = int(input())
    word = input()
    word = [x for x in word]
    wordDict = Counter(word)
    wordSet = set()
    maxSum = 0

    for ind in range(n - 1, -1, -1):
        letter = word[ind]
        wordDict[letter] -= 1
        if wordDict[letter] == 0:
            del wordDict[letter]

        wordSet.add(letter)
        curSum = len(wordDict) + len(wordSet)
        maxSum = max(curSum, maxSum)

    print(maxSum)