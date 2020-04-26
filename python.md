### 開始の呪文

```python
if __name__ == '__main__':
```

### ディレクトリの中のファイルを取得してまわす。

```python
import pandas as pd
from pathlib import Path
p = Path(".")
for i in p.glob("*.csv"):
    print(i.name)
    print(i.cwd())
    df = pd.read_csv(i)
```

```python
In [84]: from pathlib import Path

In [85]: p = Path('.')

In [89]: g = p.glob('*.csv')

In [90]: g.__next__()
Out[90]: WindowsPath('aaa.csv')

In [91]: g.__next__()
Out[91]: WindowsPath('bbb.csv')

```


### ファイルを読み込む。
```python
with open('aaa.csv', 'r') as f:
    r = f.readline()
    while(r):
        print(r, end='')
        r = f.readline()
```

### ループ
```python
for i in range(1,10,2):
    print(i)
```

### 16進数
```python
int('10', 16)
```

### format
```python
In [12]: 'Taro={aaa} {bbb:x}'.format(aaa='hage', bbb=20)
Out[12]: 'Taro=hage 14'
```

### 正規表現
```python
In [152]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm")
Out[152]: <re.Match object; span=(0, 22), match='Hanage=10cm, Mimige=20'>

In [153]: v = re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm")

In [154]: bool(v)
Out[154]: True

In [155]: v.group(1)
Out[155]: '10'

In [156]: v.group(2)
Out[156]: '20'
```

```.*```と```.*?```の違い。
なるべく多くマッチと、なるべく少なくマッチ。

```python
In [108]: re.match('.*(\d+)', 'hage hage 12345').group(1)
Out[108]: '5'

In [109]: re.match('.*?(\d+)', 'hage hage 12345').group(1)
Out[109]: '12345'
```

置換
```python
In [112]: re.sub('<a.*?>|</a>', '', '<a href="hige">hage hage 12345<a/>')
Out[112]: 'hage hage 12345'
```

### 判定
値の比較
```python
< , <= , > , >=, ==, !=
```

オブジェクトの比較
```pyhton
is, is not, in, not in
```

論理演算子
```python
and, or, not
```

if文で```False```と判定されるもの
```python
bool(False), None, 0, 0.0, '', [], {}
```

