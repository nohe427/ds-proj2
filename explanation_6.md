# Union and Intersection
For this problem, I chose to use a set to record whether or not I have seen an element before.  The set provides a runtime of O(1) for insertion, deletion, and lookup.

Union Runtime O(n)
For the union problem, I ran through each linked list element once, checked if it was in the set, and if it was not append it to the new linked list (which also has a runtime of O(n)) (and append it to the set). Space complexity is O(n) as we could have a list of two different numbers so this would return the length of both of those lists.

Intersection Runtime O(n)
For the intersection problem, I ran through the first linked list appending all elements to the set, and then I ran through the second linked list appending only elements that appeared in the set to the new linked list (and removing it from the set). Space complexity is O(log(n)) as we are only storing numbers that are duplicates in either list.  If both lists are identical, we are only storing n/2 where n is the two lists combined.
