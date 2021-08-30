list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]

list1 = ['a', 'b', 'q', 'f']
list2 = [1, 2, 3]
list1.extend(list2)
list1
['a', 'b', 'q', 'f', 1, 2, 3]

list1 = ['a', 'b', 'q', 'f', 1, 2, 3]
list1.insert(1, 'hi')
list1
['a', 'hi', 'b', 'q', 'f', 1, 2, 3]

list1 = ['a', 'hi', 'b', 'q', 'f', 1, 2, 3]
list1.sort()
list1
[1, 2, 3, 'a', 'b', 'f', 'hi', 'q']
list1.reverse()
list1
['q', 'hi', 'f', 'b', 'a', 3, 2, 1]