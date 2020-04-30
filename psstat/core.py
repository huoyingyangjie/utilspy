# @Author: yangjiegogogo@gmail.com
import os


def __ps_info_in_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    if len(lines) < 2:
        raise Exception("illegal format")
    pid = lines[0].strip()
    ts = lines[1].strip()
    return pid, ts


def __ps_info_in_sys(pid):
    ts = os.popen("ps -p %s -o lstart=" % pid).read()
    return ts.strip()


def process_dump(path):
    pid, fts = __ps_info_in_file(path)
    sts = __ps_info_in_sys(pid)
    if fts == sts:
        return True
    return False


def process_load(path, pid):
    with open(path, "w") as f:
        f.write("%s\n" % pid)
        ts = os.popen("ps -p %s -o lstart=" % pid).read()
        f.write("%s" % ts)
