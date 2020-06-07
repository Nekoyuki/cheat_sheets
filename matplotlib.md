
### お絵描き
Boxplot/hist + figsize変更 + Y軸調整

```python
In [63]: import seaborn as sns

In [64]: df = sns.load_dataset('iris')

In [66]: df.boxplot()

In [67]: df.hist()

In [68]: import matplotlib.pyplot as plt

In [46]: plt.figure(figsize=[5,5]); plt.ylim([0,3]); df.boxplot()
```

### violinplot
x/y/data、をきちんと指定する必要あり。meltで一次元のシリーズに変換要。

```python
In [78]: df.head()
Out[78]:
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa

In [80]: dfx = df.drop('species', axis=1).melt()

In [81]: dfx.head()
Out[81]:
       variable  value
0  sepal_length    5.1
1  sepal_length    4.9
2  sepal_length    4.7
3  sepal_length    4.6

In [87]: sns.violinplot(data=dfx, x='variable', y='value')
```

### 調整

```python
plt.figure(figsize=[5,5])           # キャンバスサイズ
plt.titl('hageX', fontsize=30)      # タイトル
plt.ylim([0,3])                     # Yの値の最小、最大値
plt.xlable('hage', fontsize=30)     # Xラベル
plt.tick_params(axis='x', labelsize = 10, labelrotation=90, colors='white')     # 軸ラベルの調整
plt.yticks([0, 0.5, 1.0])           # Yグリッド
plt.tight_layout()                  # うまいこと出力図の範囲を綺麗に収める
plt.text(2.0, -0.4, 'hage', fontsize=15)    # テキスト
```

[tick_params](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.tick_params.html)

### 画像の保存

```python
tips.groupby('day').mean()['total_bill'].plot(kind='bar').get_figure().savefig('hage.png')
```

### リンク

https://matplotlib.org/3.1.0/index.html
