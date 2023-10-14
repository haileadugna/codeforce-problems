n = int(input())
arr = list(map(int, input().split()))

arr.sort()

res = 0
for num in arr:
    if num > res + 1:
        break
    else:
        res += num



print(res + 1)




'''
def smallest_unmatched_titan_strength(n, artifacts):
    # Sort the artifacts in ascending order
    artifacts.sort()
    
    # Initialize a variable to keep track of the maximum reachable strength
    max_reachable_strength = 0
    
    # Iterate through the artifacts and update max_reachable_strength
    for artifact in artifacts:
        if artifact > max_reachable_strength + 1:
            # If there is a gap in reachable strengths, return max_reachable_strength + 1
            return max_reachable_strength + 1
        max_reachable_strength += artifact
    
    # If you can reach all strengths up to max_reachable_strength, return max_reachable_strength + 1
    return max_reachable_strength + 1

# Input
n = int(input())
artifacts = list(map(int, input().split()))

# Calculate and print the result
result = smallest_unmatched_titan_strength(n, artifacts)
print(result)
'''

