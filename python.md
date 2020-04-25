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

### 正規表現
```python
In [58]: import re

In [59]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm")
Out[59]: <re.Match object; span=(0, 22), match='Hanage=10cm, Mimige=20'>

In [60]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm") is None
Out[60]: False

In [62]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm").group()
Out[62]: 'Hanage=10cm, Mimige=20'

In [63]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm").group(1)
Out[63]: '10'

In [64]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm").group(2)
Out[64]: '20'

In [68]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm").start()
Out[68]: 0

In [69]: re.match('.*?(\d+).*?(\d+).*?', "Hanage=10cm, Mimige=20cm, Hige=30cm").end()
Out[69]: 22
```
