#priorityqueue test

import priorityqueue

# test basic pop function
a = priorityqueue.PriorityQueue()
a.add('alpha', 1)
a.add('charlie', 3)
a.add('delta', 4)
assert a.pop() == 'alpha'
assert a.pop() == 'charlie'
assert a.pop() == 'delta'

# test basic update function
a.add('alpha', 1)
a.add('charlie', 3)
a.add('delta', 4)
a.add('alpha', 5)
assert a.pop() == 'charlie'
assert a.pop() == 'delta'
assert a.pop() == 'alpha'

# test for stable pop
a.add('alpha', 1)
a.add('charlie', 3)
a.add('delta', 4)
a.add('alpha2', 1)
assert a.pop() == 'alpha'
assert a.pop() == 'alpha2'
assert a.pop() == 'charlie'
assert a.pop() == 'delta'

# test contains function
a.add('alpha', 1)
a.add('charlie', 3)
a.add('delta', 4)
assert a.contains('alpha')
assert a.contains('charlie')
assert a.contains('delta')
assert not a.contains('bravo')

# test is_empty
assert not a.is_empty()
a.pop()
a.pop()
a.pop()
assert a.is_empty()

assert a.keys() == set()
a.add('alpha', 1)
assert a.keys() == {'alpha'}
a.add('charlie', 3)
assert a.keys() == {'alpha', 'charlie'}
a.add('delta', 4)
assert a.keys() == {'alpha', 'charlie', 'delta'}
assert a.keys() == {'alpha', 'delta', 'charlie'}


