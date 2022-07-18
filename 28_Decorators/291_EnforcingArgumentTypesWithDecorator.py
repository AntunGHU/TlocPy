def enforce(*types):
    def decorator(fn):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))  # feel free to have more
            return fn(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


repeat_msg("hellou", "3")


@enforce(float, float)
def devide(a, b):
    print(a/b)


devide("1", 2)
devide("1", "2")
devide(2, 1)
