users = ['Dave', 'Gray', 'Sam']
data = ['Dave', True]

empty = []

# print(users[-2])
# print(users.index('Sam'))
# print(users[0:2])
# print(users[1:])

users.append('Elsa')
# print(users)

users += ['daniel', 'Jason']
# print(users)

users.extend(data)
# print(users)

users.insert(0, 'Grace')
# print(users)

users[2:2] += ['Eddie', 'Alex']
# print(users)

users[1:3] = ['antony', 'JPJ']
# print(users)

users.remove('Dave')
users.pop()
# print(users)

del users[0]
# print(users)

# del data
data.clear()
# print(data)

users.sort()
# print(users)

users.sort(key=str.lower)
# print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# print(sorted(nums, reverse=True))
# print(nums)

numsCopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
# print()
# print(numsCopy)
# print(mynums)
# print(mycopy)

# Tuples
# mytuple = tuple('Sam')
# anotherTuple = ('Dave', 45, 'Anna', 'Fred', True)
# (one, *two, three) = anotherTuple
# print(one)
# print(two)
# print(three)

# Dictionaries

# band = {"vocals": "plant", "guitar": "Page"}
# band2 = dict(vocals= "plant", guitar= "Page")
# print(band.get('guitar'))
# print(band2['vocals'])
# print(band.keys())
# print()

# list of key value pairs a tuple
# print(anotherTuple)
# print(band.items())

# print('guitar' in band)
# band['guitar'] = 'drums'
# band.update({'name': 'mark'})
# print(band)

# print(band.pop('name'))
# print(band)

# band.update({'drums': 'Bonham'})
# band['id'] = '23jj2b3'
# print(band.popitem())
# print(band)

# del band['vocals']
# print(band)

# band2.clear()
# print(band2)

# copy dictionaries
# band2 = band # creates a reference, not a copy
# print('Bad copy')
# print(band2)

# band2 = band.copy() # a copy
# band3 = dict(band) # a copy
# print(band)
# print(band3.popitem())
# print(band3)
# band2.update({"tree": "wood"})
# print(band2)
# print(band)

# Nested dictionaries

member1 = {
  "name": "Plant",
  "instrument": "guitar"
}
member2 = {
  "name": "Page",
  "instrument": "vocals"
}
band = {
  "member1": member1,
  "member2": member2,
}
# print(band)
# print(band['member1']['name'])

# Sets
nums = {1, 2, 1, 3, 4, 5}
nums2 = set((1, 2, 1, 3, 4, False, 'Mark'))
# print(nums)
# print(nums2)
nums.add(8)
# print(nums)

nums.update(nums2)
# print()

one = {1, 2, 4, 5, 6, 3}
two = {5, 9, 0, 6, 7}

# merging two sets
newset = one.union(two)
# print(newset)

# keeping only duplicates
newset = one.intersection(two)
# print(newset)

# keeping all except duplicates
one.symmetric_difference_update(two)
# print(one)
one.intersection_update(two)
# print(one)

# loops
# [print ("x = {:d}".format(x * 2)) for x in range(10)]

val = 0
# while val < 10:
#   val += 1
#   if val == 5:
#     continue
#   print(val)
# else:
#   print('Finished')

names = ["Dave", "Mike", "John"]
# for name in names:
#   print(name)
# for x in "Mississipi":
#   print(x)

# for name in names:
#   if name == 'Mike':
#     continue
#   print(name)

# for x in range(4):
#   print(x)

# for x in range(2, 10, 3):
#   print(x)
# else:
#   print('Done')

actions = ['codes', 'eats', 'sleeps']

print('-----------------------')
for name in names:
  for action in actions:
    print(name + ' ' + action + '.')
  print('-----------------------')














































