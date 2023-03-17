nums = input()
res = ""
for i in range(len(nums)):
    if i == 0 and nums[i] == "9":
        res += nums[i]
    elif int(nums[i]) > 9 - int(nums[i]):
        res += str(9 - int(nums[i]))
    else:
        res += nums[i]
print(int(res))

