# @Author: yangjiegogogo@gmail.com
import datetime
import traceback


def DBGCTL(bool_val):
    globals()['__yangjiegogogo_debug__'] = bool_val


def __debug_print__(debug_type, fmt, *args):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print("[%s][%s]: %s" % (ts, debug_type, fmt % (args)))


def DBG(fmt, *args):
    if  globals()['__yangjiegogogo_debug__']:
        __debug_print__("DBG", fmt, *args)


def INF(fmt, *args):
    __debug_print__("INF", fmt, *args)


def ERR(fmt, *args):
    __debug_print__("ERR", fmt, *args)


def DIE(fmt, *args):
    __debug_print__("DIE", fmt, *args)
    for line in traceback.format_stack():
        print(line.strip())
    exit(1)

