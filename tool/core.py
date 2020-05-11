# @Author: yangjiegogogo@gmail.com


def count_set_bits(n):
    count = 0
    binstr = bin(n).replace('0b', '')
    for i in binstr:
        if i == "1":
            count += 1
    return count
