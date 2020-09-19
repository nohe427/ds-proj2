# Active Directory Explanation
In the active directory search, I used recursion to iterate over each and every group that existed within that parent group and if the user was found before I reached a sub group, the function would exit early.
The runtime complexity is O(n) since the last found directory could contain the user
The space complexity is O(1) since we are not storing an intermediate variables along the way