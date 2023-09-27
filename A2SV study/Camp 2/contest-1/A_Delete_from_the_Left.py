word = list(input().strip())
word2 = list(input().strip())
word.reverse()
word2.reverse()
word = ''.join(word)    
word2 = ''.join(word2)

i = 0
while i < len(word) and i < len(word2) and word[i] == word2[i]:
    i += 1

res = len(word) + len(word2) - 2 * i
print(res)
