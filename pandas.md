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

[seaborn-data](https://github.com/mwaskom/seaborn-data) のデータを使う場合

```python
In [35]: import seaborn as sns

In [36]: sns.load_dataset('iris')
```

### loc ラベルで指定する。
空の```df```に値を代入できる。

```python
In [299]: df = pd.DataFrame()

In [300]: df.loc[0,0] = 'h'

In [301]: df
Out[301]:
   0
0  h
```

### iloc 行番号、列番号で抽出
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
In [131]: df[(df['1'] == 'f') & (df['3'] == 'h')]   # 条件にあった行抽出
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

locを使用して、アクセス、一番応用が効く
```python
In [85]: df
Out[85]:
   1  2  3  4  5
-
1  a  b  c  d  e
2  a  g  c  i  f
3  a  l  m  n  e
4  b  b  c  d  e

In [166]: df.loc[(df['1'] == 'a') & (df['2'] == 'g'), :]    # 行選択
Out[166]:
   1  2  3  4  5
-
2  a  g  c  i  f

In [167]: df.loc[(df['1'] == 'a') & (df['2'] == 'g'), '3':'5']  # 行選択＋列選択
Out[167]:
   3  4  5
-
2  c  i  f

In [86]: df.loc[(df['1'] == 'a') & (df['2'] == 'g'), '3']   # セル選択
Out[86]:
-
2    c
Name: 3, dtype: object

In [93]: df.loc[(df['1'] == 'a') & (df['2'] == 'g'), '3'].values[0]     # 値アクセス
Out[93]: 'c'

In [98]: df.loc[(df['1'] == 'a') & (df['2'] == 'g'), '3'] = '8'     # 値書き込み

In [99]: df
Out[99]:
   1  2  3  4  5
-
1  a  b  c  d  e
2  a  g  8  i  f
3  a  l  m  n  e
4  b  b  c  d  e

In [169]: df.loc[~(df['1'] == 'a'), :]  # 否定
Out[169]:
   1  2  3  4  5
-
4  b  b  c  d  e

In [170]: df.loc[(df['1'] == 'a') | (df['2'] == 'g'), :]    # OR
Out[170]:
   1  2  3  4  5
-
1  a  b  c  d  e
2  a  g  c  i  f
3  a  l  m  n  e
```

```python
In [171]: df.where(df == 'a', np.nan)    # whereを使った例, 対象となった以外はnp.nan
Out[171]:
     1    2    3    4    5
-
1    a  NaN  NaN  NaN  NaN
2    a  NaN  NaN  NaN  NaN
3    a  NaN  NaN  NaN  NaN
4  NaN  NaN  NaN  NaN  NaN
```

### ドロップ
```python
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
```

### セル内の値の結合

```python
In [324]: df[['1','2']]
Out[324]:
   1  2
-
1  a  b
2  f  g
3  k  l

In [325]: df[['1','2']].apply(lambda x: '{}_{}'.format(x[0], x[1]), axis=1)
Out[325]:
-
1    a_b
2    f_g
3    k_l
dtype: object
```

### セル内の値の分割

```python
In [335]: df
Out[335]:
          1
-
1  <a>a</a>
2  <a>f</a>

In [337]: df['1'].str.split('/')
Out[337]:
-
1    [<a>a<, a>]
2    [<a>f<, a>]
Name: 1, dtype: object

In [339]: df['1'].str.extract('(<a>)(.)(</a>)', expand=True)
Out[339]:
     0  1     2
-
1  <a>  a  </a>
2  <a>  f  </a>

In [339]:

In [340]: df['1'].str.extract('<a>(.)</a>', expand=True)
Out[340]:
   0
-
1  a
2  f
```

### 正規表現で置換
```python
In [147]: df = pd.DataFrame(['abc', 'def'])

In [148]: df
Out[148]:
     0
0  abc
1  def

In [149]: df.replace(r'a.*', r'ggg', regex=True)
Out[149]:
     0
0  ggg
1  def

In [150]: df.applymap(lambda x: re.sub(r'a.*', r'ggg', x))
Out[150]:
     0
0  ggg
1  def
```


### カラム、ロウをループする
```python
In [32]: df
Out[32]:
   a  b
0  1  2
1  3  4
2  5  6

In [33]: for c, d in df.iteritems():
    ...:     print(c, d.max())
    ...:
a 5
b 6

In [34]: for r, d in df.iterrows():
    ...:     print(r, d.max())
    ...:
0 2
1 4
2 6
```

### グルーピング
```python
df.groupby('pin').mean()
```

特定の値を個数をカウントする
```python
In [9]: df = sns.load_dataset('iris')

In [10]: df.groupby('species').apply(lambda x: x == 0.2)
Out[10]:
     sepal_length  sepal_width  petal_length  petal_width  species
0           False        False         False         True    False
1           False        False         False         True    False
2           False        False         False         True    False
3           False        False         False         True    False
4           False        False         False         True    False
..            ...          ...           ...          ...      ...
145         False        False         False        False    False
146         False        False         False        False    False
147         False        False         False        False    False
148         False        False         False        False    False
149         False        False         False        False    False

[150 rows x 5 columns]

In [11]: df.groupby('species').apply(lambda x: x == 0.2).sum()
Out[11]:
sepal_length     0
sepal_width      0
petal_length     0
petal_width     29
species          0
dtype: int64
```


### シリーズを合体して１つにする ```melt```
```python
In [35]: df.melt()
Out[35]:
  variable  value
0        a      1
1        a      3
2        a      5
3        b      2
4        b      4
5        b      6
```

### ピボットテーブル ```pivot_table```
```melt```の逆

```python
In [42]: tips = sns.load_dataset('tips')

In [45]: tips
Out[45]:
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]

In [46]: tips.pivot_table(columns='day', values='total_bill', index='size')
Out[46]:
day        Thur        Fri        Sat        Sun
size
1     10.070000   8.580000   5.160000        NaN
2     15.156875  16.321875  16.837170  17.560000
3     19.160000  15.980000  25.509444  22.184000
4     29.950000  40.170000  29.876154  26.688333
5     41.190000        NaN  28.150000  27.000000
6     30.383333        NaN        NaN  48.170000
```

### ソート、インデックスを振り直し
```python
df.sort_values('hage', inplace=True)        # ソート
df.reset_index(drop=True)                   # インデックス振り直し
df.columns = sorted(df.columns.to_list())   # カラム名ソート
```

### カラムの並び替え
```python
In [8]: df = pd.DataFrame(data=[[1,2,3,4,5]], columns=[8,7,3,2,0])

In [9]: df
Out[9]:
   8  7  3  2  0
0  1  2  3  4  5

In [12]: df[sorted(df.columns)]
Out[12]:
   0  2  3  7  8
0  5  4  3  2  1
```

### to_csv

```python
In [97]: df.to_csv()
Out[97]: ',0,1\r\n0,Hage,Hige\r\n'

In [98]: print(df.to_csv())
,0,1
0,Hage,Hige
```

### to_string
```python
pd.options.display.max_colwidth = 500   # これを唱えないと行末が...になっちゃう
df.to_string('hage.csv', index=False)
```

### データフレーム中で最小値を探す
```python
In [135]: i = [0, 0, 99999]
     ...: for c, d in df.drop('species', axis=1).items():
     ...:     for r, s in d.items():
     ...:         i = [r, c, s] if i[2] > s else i
     ...: print(i)
[9, 'petal_width', 0.1]
```

### データフレームのリスト例
```python
def aaa(i):
    df = pd.DataFrame)
    df.read_csv(i)
    return df

df_lst = []
for i in args:
    df = aaa(i)
    df_lst.append(df)

se_acc = pd.Series()
for j in df_lst:
    for k j.index.to_list():
        se = j.loc[k, :]
        se_acc = pd.concat([se_acc, se])
```

### Links
https://pandas.pydata.org/docs/

http://sinhrks.hatenablog.com/entry/2015/04/28/235430
