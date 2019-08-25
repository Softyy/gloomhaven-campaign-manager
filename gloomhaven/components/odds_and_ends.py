def first_arg_is_greatest(*args):
    if len(args) < 2:
        raise Exception(f'2+ args are expected, {len(args)} were given')
    return (all(x < args[0] for x in args[1:]))
