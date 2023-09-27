class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num):
        node = self.root
        xor_num = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            
            opposite_bit = 1 - bit
            if opposite_bit in node.children:
                xor_num |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return xor_num

def max_xor(nums):
    trie = Trie()
    max_xor_result = 0
    
    for num in nums:
        trie.insert(num)
        xor_result = trie.find_max_xor(num)
        max_xor_result = max(max_xor_result, xor_result)
    
    return max_xor_result


test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))

    result = max_xor(nums)
    print(result)
