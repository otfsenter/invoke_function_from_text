import utils
import utils2
from context import Context


def init():
    c = Context()
    utils.register(c)
    utils2.register(c)
    return c
