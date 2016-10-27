import six
import time


def exponential_fuckoff(*dargs, **dkwargs):
    retry_kwargs = {
        'timeout': 10,
        'coeff': 2,
        'verbose': True
    }

    if len(dargs) == 1 and callable(dargs[0]):
        with_args = False
    else:
        with_args = True
        retry_kwargs.update(dkwargs)

    def decorator(func):

        @six.wraps(func)
        def wrapped(*args, **kwargs):
            retry = Retry(func, **retry_kwargs)
            return retry.run(*args, **kwargs)

        return wrapped

    if not with_args:
        return decorator(dargs[0])

    return decorator


class WrapCallable:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class RecursiveMethod:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while isinstance(result, WrapCallable):
            result = result()
        return result

    def call(self, *args, **kwargs):
        return WrapCallable(lambda: self.func(*args, **kwargs))


class Retry:
    def __init__(self, func, **kwargs):
        self.func = func
        self.trials = 0

        for attr, value in kwargs.items():
            setattr(self, attr, value)

        self.run = RecursiveMethod(self.run)

    def run(self, *args, **kwargs):
        try:
            if self.verbose and self.trials > 0:
                print('Repeating {} #{}'.format(self.func.__name__, self.trials))

            self.trials += 1
            return self.func(*args, **kwargs)

        except Exception:
            time.sleep(self.timeout)
            self.timeout /= self.coeff or 1

            return self.run.call(*args, **kwargs)
