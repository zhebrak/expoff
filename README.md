# expoff

Production ready implementation of Exponential Fuckoff algorithm. Repeat your functions with exponentially diminishing timeout until you're done.


```python
from expoff import exponential_fuckoff

@exponential_fuckoff
def get_infinity():
    return 1 / 0

get_infinity()
```

> each call is made 2x sooner than previous!

```code
Repeating get_infinity #1
Repeating get_infinity #2
Repeating get_infinity #3
Repeating get_infinity #4
Repeating get_infinity #5
Repeating get_infinity #6
Repeating get_infinity #7
...
```
