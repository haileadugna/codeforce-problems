# Consider a simplified penalty phase at the end of a football match.

# A penalty phase consists of at most 10
#  kicks, the first team takes the first kick, the second team takes the second kick, then the first team takes the third kick, and so on. The team that scores more goals wins; if both teams score the same number of goals, the game results in a tie (note that it goes against the usual football rules). The penalty phase is stopped if one team has scored more goals than the other team could reach with all of its remaining kicks. For example, if after the 7
# -th kick the first team has scored 1
#  goal, and the second team has scored 3
#  goals, the penalty phase ends — the first team cannot reach 3
#  goals.

# You know which player will be taking each kick, so you have your predictions for each of the 10
#  kicks. These predictions are represented by a string s
#  consisting of 10
#  characters. Each character can either be 1, 0, or ?. This string represents your predictions in the following way:

# if si
#  is 1, then the i
# -th kick will definitely score a goal;
# if si
#  is 0, then the i
# -th kick definitely won't score a goal;
# if si
#  is ?, then the i
# -th kick could go either way.
# Based on your predictions, you have to calculate the minimum possible number of kicks there can be in the penalty phase (that means, the earliest moment when the penalty phase is stopped, considering all possible ways it could go). Note that the referee doesn't take into account any predictions when deciding to stop the penalty phase — you may know that some kick will/won't be scored, but the referee doesn't.

# Input
# The first line contains one integer t
#  (1≤t≤1000
# ) — the number of test cases.

# Each test case is represented by one line containing the string s
# , consisting of exactly 10
#  characters. Each character is either 1, 0, or ?.

# Output
# For each test case, print one integer — the minimum possible number of kicks in the penalty phase.

# Example
# inputCopy
# 4
# 1?0???1001
# 1111111111
# ??????????
# 0100000000
# outputCopy
# 7
# 10
# 6
# 9
# Note
# Consider the example test:

# In the first test case, consider the situation when the 1
# -st, 5
# -th and 7
# -th kicks score goals, and kicks 2
# , 3
# , 4
#  and 6
#  are unsuccessful. Then the current number of goals for the first team is 3
# , for the second team is 0
# , and the referee sees that the second team can score at most 2
#  goals in the remaining kicks. So the penalty phase can be stopped after the 7
# -th kick.

# In the second test case, the penalty phase won't be stopped until all 10
#  kicks are finished.

# In the third test case, if the first team doesn't score any of its three first kicks and the second team scores all of its three first kicks, then after the 6
# -th kick, the first team has scored 0
#  goals and the second team has scored 3
#  goals, and the referee sees that the first team can score at most 2
#  goals in the remaining kicks. So, the penalty phase can be stopped after the 6
# -th kick.

# In the fourth test case, even though you can predict the whole penalty phase, the referee understands that the phase should be ended only after the 9
# -th kick.


test = int(input())

for i in range(test):
    s = input()
    cnt1 = 0
    cnt2 = 0
    acnt1 = 0
    acnt2 = 0
    loss1 = 0
    loss2 = 0
 
    for i in range(10):
        if i%2 == 0:
            if s[i] == '1':
                cnt1 += 1
            elif s[i] == '?':
                acnt1 += 1
            else:
                loss1 += 1
 
        else:
            if s[i] == '1':
                cnt2 += 1
            elif s[i] == '?':
                acnt2 += 1
            else:
                loss2 += 1
 
        if cnt1 + acnt1 > 5 - (loss2 + acnt2) or cnt1 + acnt1 > 5 - acnt2:
            print(i+1)
            break
        if cnt2 + acnt2 > 5 - (loss1 + acnt1) or cnt2 + acnt2 > 5 - acnt1:
            print(i+1)
            break
    else:
        print(10) 