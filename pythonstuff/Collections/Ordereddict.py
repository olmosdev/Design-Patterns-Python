from collections import OrderedDict

d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(''.join(d))
d.move_to_end('b', last=False)
print(''.join(d))
print()

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
d = LastUpdatedOrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)
d['a'] = 10
print(d)
print()

