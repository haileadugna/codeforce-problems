# A bracket sequence is called regular if it is possible to obtain correct arithmetic expression by inserting characters «+» and «1» into this sequence. For example, sequences «(())()», «()» and «(()(()))» are regular, while «)(», «(()» and «(()))(» are not.

# One day Johnny got bracket sequence. He decided to remove some of the brackets from it in order to obtain a regular bracket sequence. What is the maximum length of a regular bracket sequence which can be obtained?

# Input
# Input consists of a single line with non-empty string of «(» and «)» characters. Its length does not exceed 106.

# Output
# Output the maximum possible length of a regular bracket sequence.

# Examples
# inputCopy
# (()))(
# outputCopy
# 4
# inputCopy
# ((()())
# outputCopy
# 6

# Solution code

s = input()
n = len(s)
a = 0
b = 0
for i in range(n):
    if s[i] == '(':
        a += 1
    else:
        if a > 0:
            a -= 1
            b += 2
print(b)


