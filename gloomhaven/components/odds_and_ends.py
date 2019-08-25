def first_arg_is_greatest(*args):
    return (all(x < args[0] for x in args[1:]))
