def hello():
    print('Hello world')
# hello()


def multiple_items(*args):
    print(args)

# multiple_items(1, True, 'Dave', 56, False)

# kwargs = keyword arguments


def mult_named_items(**kwargs):
    print(kwargs)

# mult_named_items(vocals="mark",name="adam")

# Recursion


def add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)

# result = add_one(0)
# print("Final: "+ str(result))


value = True
# while value:
#   print('Come')
#   value = 0

# scopes

name = "Dave"
count = 1


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name: str):
        nonlocal color
        color = 'red'
        print(color)
        print(name)

    greeting('Dave')

# another()

# closure


def parent_funtion(person, coins=1):
    # coins = count

    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left")
        else:
            print("\n" + person + " has no more coin")

    return play_game


tommy = parent_funtion('Tommy', 2)
jenny = parent_funtion('Jenny', 3)

# tommy()
# tommy()

# jenny()
# jenny()
# jenny()
count = 3
person = "Ade"
message = "\n%s has %d coins left." % (person, count)
# print(message)
# print(f"\n{person} has {count} coins left")
# print("\n{} has {:d} coins left".format(person, count))

num = 10
# print(f"2.25 x {num} is {2.25 * num:.2f}")

# lambda


def res(x): return x * x
# print(res(10))


def another(x, y): return x ** y
# print(another(42, 57))


def addOne(num):
    return lambda num2: num2 + num


addMore = addOne(10)
# print(addMore(20))
lambda num: num * num

numbers = [23, 15, 48, 82, 21, 40]
squared_nums = map(lambda num: num * num, numbers)
print(f"Result: {list(squared_nums)}")

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(f"Filtered: {list(odd_nums)}")

from functools import reduce
# sum is still a better function to use
added_nums = reduce(lambda acc, curr : acc + curr, numbers, 25)
print(f"Addition: {added_nums}")
print(f"Addition: {sum(numbers, 22)}")

names = ['Dave', 'Makurdi', 'Jacob', 'Sam smith']
complexAddition = reduce(lambda acc, curr : acc + len(curr), names, 0)
print(f"Names_Length: {complexAddition}")
























