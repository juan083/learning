dict的遍历
====

```
dic = {'name': 'meng', 'from': 'guangxi', 'location': 'shenzhen'}
for k in dic:
    # name meng
    print(k, dic[k])

for k, v in dic.items():
    # name meng
    print(k, v)

for item in dic.items():
    # ('name', 'meng')
    print(item)

for v in dic.values():
    # meng
    print(v)

for k in dic.keys():
    # meng
    print(dic[k])
```
