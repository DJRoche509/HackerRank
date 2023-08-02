'''
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is 
the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.


Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]


Constraints:
1 <= s.length <= 104
s[i] and c are lowercase English letters.
It is guaranteed that c occurs at least once in s.
'''

def shortest_distance(s, c):
  answer = [0] * len(s)
    prev = float('-inf')
    # Scan from left to right
    for i in range (len(s)):
        if s[i] == c:
            prev = i
        answer[i] = i - prev
        
    #Scan from right to left 
    prev = float('inf')
    for i in range (len(s)-1, -1, -1):
        if s[i] == c:
            prev = i
        answer[i] = min(answer[i], prev -i)
    return answer
    
print(shortest_distance('loveleetcode','e'))
print(shortest_distance('aaab', 'b))
print(shortest_distance('aaabcfbv','b'))  # Expected output: [3,2,1,0,1,1,0,1]

                        
'''
Time complexity of this implementation is O(n), where n is the length of the input string s. This is because we perform two separate
scans of the string, each of which takes O(n) time.
The space complexity of this implementation is also O(n), because we allocate an additional array of length n to store the distances 
from the leftmost occurrence of c.
'''
