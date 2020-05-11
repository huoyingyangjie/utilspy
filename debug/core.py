# @Author: yangjiegogogo@gmail.com
import datetime
import traceback

DBGCTL_VAR_NAME = "__yangjiegogogo_debug__"


def DBGCTL(bool_val):
    globals()[DBGCTL_VAR_NAME] = bool_val


def __debug_print__(debug_type, fmt, *args):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print("[%s][%s]: %s" % (ts, debug_type, fmt % (args)))


def DBG(fmt, *args):
    if DBGCTL_VAR_NAME not in globals() or globals()[DBGCTL_VAR_NAME]:
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

