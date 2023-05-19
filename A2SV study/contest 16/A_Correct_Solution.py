num = input()
gus = input()
nums = []

for i in num:
    nums.append(int(i))
nums.sort()

res = ""
temp = ""
for i in nums:
    if i == 0 and res == "":
        temp += str(i)
    else:
        res += str(i)
        res += temp
        temp = ""
if gus == num and num == "0":
    print("OK")
elif res == gus:
    print("OK")
else:
    print("WRONG_ANSWER")

