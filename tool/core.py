# @Author: yangjiegogogo@gmail.com


def count_set_bits(n):
    count = 0
    binstr = bin(n).replace('0b', '')
    for i in binstr:
        if i == "1":
            count += 1
    return count


def joinall(split_str, eles):
    str_eles = ""
    count = 0
    for ele in eles:
        str_eles += "%s" % ele
        count += 1
        if count != len(eles):
            str_eles += split_str
    return str_eles