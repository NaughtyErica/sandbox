from collections import defaultdict, namedtuple, OrderedDict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)


Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(
    id_num='1234',
    desc='Ford Engine',
    cost=1200.00,
    amount=10
)

print(auto_parts.id_num)


d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))

print(new_d)


for key in new_d:
    print(key, new_d[key])
print('-------------------------------')
for key in reversed(new_d):
    print(key, new_d[key])
