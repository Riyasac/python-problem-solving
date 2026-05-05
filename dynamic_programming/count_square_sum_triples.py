"""
Count Square Sum Triples

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.


Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).


Constraints:

    1 <= n <= 250

"""
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 1 <= n <= 250:
            count = 0    
            for c in range(1, n + 1):
                for a in range(1, c):
                    b2 = c*c - a*a
                    b = int(b2**0.5)
                    if b*b == b2 and b <= n:
                        print(f"Found triple : ({a}, {b}, {c})")
                        count += 1
            return count
        else:
            return 0

        
if __name__ == "__main__":
    n = 5
    print(f"n = {n}, count = { Solution().countTriples(n)}")

    n = 10
    print(f"n = {n}, count = { Solution().countTriples(n)}")
        
