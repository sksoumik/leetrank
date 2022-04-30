# https://www.hackerrank.com/challenges/python-tuples/

# Given an integer, , and  space-separated integers as input, create a tuple, ,
# of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.


def hash_tuple(t):
    return hash(t)


if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(t)
    print(hash_tuple(t))
