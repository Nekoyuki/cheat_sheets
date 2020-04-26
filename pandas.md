### loc

```python
In [92]: import pandas as pd

In [93]: df = pd.DataFrame()

In [94]: df.loc[0,0] = 'Hage'

In [95]: df.loc[0,1] = 'Hige'

In [96]: df
Out[96]: 
      0     1
0  Hage  Hige
```

### to_csv

``python
In [97]: df.to_csv()
Out[97]: ',0,1\r\n0,Hage,Hige\r\n'

In [98]: print(df.to_csv())
,0,1
0,Hage,Hige
```

