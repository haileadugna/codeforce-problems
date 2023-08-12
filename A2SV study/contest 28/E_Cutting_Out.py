from collections import Counter

    


n, k = map(int, input().split())
s = list(map(int, input().split()))
freq_counter = Counter()
window_counter = Counter()

max_copies = 0
t = []

for i in range(n):
    
    window_counter[s[i]] += 1
    freq_counter[s[i]] += 1

    
    if len(window_counter) > k:
        elem_to_remove = s[i - k]
        window_counter[elem_to_remove] -= 1
        if window_counter[elem_to_remove] == 0:
            del window_counter[elem_to_remove]

    
    if len(window_counter) == k:
        curr_copies = min(window_counter.values())
        if curr_copies > max_copies:
            max_copies = curr_copies
            t = list(window_counter.keys())


print(*t)
