# Readme
## Files
```
clickstream.py
```

## Environment
Python 3.x (No additional library / package used.)

## Steps
1. Set the desired click number in `clickstream.py`.
``` python=92
clicks = 8  # The number of clicks can be modified.
```
2. Run `clickstream.py` using python 3.x.
3. The iteration process takes time, so be patient and wait for the result. :)

## Further settings
- If you want to set the program for your own graph, just edit the codes located at `line 19` to `line 87`. 
``` python=19
# Start setting Nodes.
ordering = Node("ordering", True, [0])
refund = Node("refund", True, [0])
order = Node("order", False, [refund, ordering])
ordering.setConnected([order]) 
...
```