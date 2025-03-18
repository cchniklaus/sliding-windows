# sliding windows
based on function numpy.lib.stride_tricks.as_strided, we create a simple and efficient class, Slide_wins, Performing a 2D sliding window operation on a 2D array.

## User Manual

```Python
Row, Col = 11, 9
x = np.arange(Row * Col).reshape(Row,Col)
print(x)

win_size = (5,3)
win_step = (3,2)

sw = Slide_wins(x,win_size,win_step)
print(sw.run())
```



