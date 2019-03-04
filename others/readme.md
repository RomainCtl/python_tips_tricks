# How to

## ProgressBarIterator

[pbi.py](./pbi.py)

> Console progress bar iterator

Object that create progress bar with iteration of iterable object.

ProgressBarIterator accept list and dict types.

#### Example
```python
items = list(range(2,50))
# items = {"p"+str(i): items[i] for i in range(len(items))}
items = ProgressBarIterator(items)

for i in items:
    sleep(0.1)
```
