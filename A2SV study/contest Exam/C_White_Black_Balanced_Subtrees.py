def main():
    t = int(input())  # Number of test cases
    
    for _ in range(t):
        n = int(input())  # Number of vertices in the tree
        parents = list(map(int, input().split()))  # Parent vertices
        colors = input()  # Color string
        
        # Create an array to store the count of black and white vertices
        counts = [0, 0]
        
        # Initialize the dictionary with a zero difference
        balanced_subtrees = {0: 1}
        
        ans = 0
        
        for i in range(n - 1, -1, -1):
            color = 0 if colors[i] == 'B' else 1
            counts[color] += 1
            
            diff = counts[0] - counts[1]
            ans += balanced_subtrees.get(diff, 0)
            
            # Update the dictionary with the current difference
            balanced_subtrees[diff] = balanced_subtrees.get(diff, 0) + 1
            
        print(ans)

main()
