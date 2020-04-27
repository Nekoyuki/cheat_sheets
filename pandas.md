### おためしデータフレーム作成

```python
In [273]: data='''
     ...: - 1 2 3 4 5
     ...: 1 a b c d e
     ...: 2 f g h i j
     ...: 3 k l m n o
     ...: '''

In [274]: df = pd.read_table(io.StringIO(data), sep=' ', index_col=0, header=0)

In [275]: df
Out[275]:
   1  2  3  4  5
-
1  a  b  c  d  e
2  f  g  h  i  j
3  k  l  m  n  o

In [276]: df.index
Out[276]: Int64Index([1, 2, 3], dtype='int64', name='-')

In [277]: df.columns
Out[277]: Index(['1', '2', '3', '4', '5'], dtype='object')
```

### loc
```df```が空の場合できる

```python
In [94]: df.loc[0,0] = 'Hage'

In [95]: df.loc[0,1] = 'Hige'

In [96]: df
Out[96]:
      0     1
0  Hage  Hige
```

### 行番号、列番号で抽出
```python
In [182]: df.iloc[:, [0,1]]
Out[182]:
   1  2
0  a  b
1  f  g
2  k  l

In [183]: df.iloc[[0,1],:]
Out[183]:
   1  2  3  4  5
0  a  b  c  d  e
1  f  g  h  i  j

In [184]: df.iloc[1,3]
Out[184]: 'i'
```

### 条件にあった行列
```python
In [128]: df.drop(1)    # 行のドロップ
Out[128]:
   1  2  3  4  5
0  a  b  c  d  e
2  k  l  m  n  o

In [129]: df.drop([1])  # 行のドロップ
Out[129]:
   1  2  3  4  5
0  a  b  c  d  e
2  k  l  m  n  o

In [130]: df.drop(['1'], axis=1)    # 列のドロップ
Out[130]:
   2  3  4  5
0  b  c  d  e
1  g  h  i  j
2  l  m  n  o

In [131]: df[(df['1'] == 'f') & (df['3'] == 'h')]   # 条件にあった行列抽出
Out[131]:
   1  2  3  4  5
1  f  g  h  i  j

In [132]: df[['1', '3']].apply(lambda x: True if x[0] == 'f' and x[1] == 'h' else False, axis=1)
Out[132]:
0    False
1     True
2    False
dtype: bool

In [133]: j = df[['1', '3']].apply(lambda x: True if x[0] == 'f' and x[1] == 'h' else False, axis=1)

In [134]: df[j]
Out[134]:
   1  2  3  4  5
1  f  g  h  i  j
```

### to_csv

```python
In [97]: df.to_csv()
Out[97]: ',0,1\r\n0,Hage,Hige\r\n'

In [98]: print(df.to_csv())
,0,1
0,Hage,Hige
```

