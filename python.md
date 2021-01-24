### 開始の呪文

```python
if __name__ == '__main__':
```

### ディレクトリの中のファイルを取得してまわす。
```glob```の場合
```python
In [13]: import glob

In [14]: glob.glob('*.txt')
Out[14]: ['hage.txt', 'hige.txt']
```

```pathlib```の場合

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
16進数 -> 10進数
```python
In [5]: int('a', 16)
Out[5]: 10
```
10進数 -> 16進数
```python
In [12]: hex(10)
Out[12]: '0xa'
```

16進数 -> 2進数
```python
n [1]: a = '007f'

In [2]: b = '060f'

In [5]: bin(int(a + b, 16))[2:]
Out[5]: '11111110000011000001111'

In [6]: bin(int(a + b, 16))[2:].zfill(32)
Out[6]: '00000000011111110000011000001111'
```



### format
```python
In [28]: 'Taro={looks} id={id:04d}'.format(looks='hage', id=2)
Out[28]: 'Taro=hage id=0002'
```

### 正規表現

マッチ

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

### 内包表記
```python
In [3]: [i for i in range(0,5,1) if i % 2 == 0]
Out[3]: [0, 2, 4]
```

```Grep```ライク
```python
In [6]: lst
Out[6]: ['hage', 'hige', 'hoge', 'aaa', 'bbb', 'ccc']

In [8]: [i for i in lst if 'h' in i]
Out[8]: ['hage', 'hige', 'hoge']``
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

ファイルの存在確認
```python
os.path.exists('hoge.txt')  # ファイル/ディレクトリがあるか？
os.path.isfile('file')      # ファイルがあるか？
os.path.isdir('dir')        # ディレクトリがあるか？
```

### 反転
```python
In [12]: 'hagehagehage'[::-1]
Out[12]: 'egahegahegah'
```

### ディクショナリ
```python
In [13]: dict = {
    ...: '0':'hage',
    ...: '1':'hige',
    ...: }

In [14]: dict['0']
Out[14]: 'hage'

```

### 終了
```python
sys.exit()
```

### basename
```python
In [40]: os.path.basename(s)
Out[40]: 'hoge.py'

In [41]: os.path.splitext(s)
Out[41]: ('/hage/hige/hoge', '.py')
```

### argv + basename + mkdir + loop
```python
import sys
import os
if __name__ == '__main__'
    args = sys.argv[1:]     # プログラム名以外をゲット
    basename = os.path.splitext(sys.argv[0])[0]
    os.mkdir(basename)
    for i in args:
        print(i)
```

### docopt

[python_docopt_sample.py](./python_docopt_sample.py)

```python
In [77]: run python_docopt_sample.py hige

In [78]: args
Out[78]:
{'--help': False,
 '-a': None,
 '-b': 'hikari',
 '<file>': 'hige'}
```

### シェル動作

```python
import shutil
shutil.copy('a', 'b')     # file copy
shutil.copytree('a, 'b')  # directory copy
shutil.move('a', 'b')     # move
os.unlink('a')            # remove
shutil.rmtree('a')        # remove directory
```
### subprocess

```python
In [80]: import subprocess

In [81]: from subprocess import PIPE

In [82]: p = subprocess.run("ls *", shell=True, stdout=PIPE, stderr=PIPE)

In [83]: p.stdout
Out[83]: b'awk.md\neclipse.md\nelectric.md\njava.md\nlinux.md\nmarkdown.md\nmatplotlib.md\npandas.md\npython.md\npython_debugger.md\npython_docopt_sample.py\nraspberry_pi.md\nREADME.md\nregexp.md\nsed.md\nshellscript.md\nvim.md\n\nimage:\n2020_06_20_violinplot.png\n2020_1024a0.PNG\n2020_1024a1.PNG\n2020_1024b0.PNG\n2020_1024d0.PNG\n2020_1024e.PNG\n2020_1024f0.PNG\n2020_1024g.PNG\n'

In [90]: p.stdout.decode('utf-8')
Out[90]: 'awk.md\neclipse.md\nelectric.md\njava.md\nlinux.md\nmarkdown.md\nmatplotlib.md\npandas.md\npython.md\npython_debugger.md\npython_docopt_sample.py\nraspberry_pi.md\nREADME.md\nregexp.md\nsed.md\nshellscript.md\nvim.md\n\nimage:\n2020_06_20_violinplot.png\n2020_1024a0.PNG\n2020_1024a1.PNG\n2020_1024b0.PNG\n2020_1024d0.PNG\n2020_1024e.PNG\n2020_1024f0.PNG\n2020_1024g.PNG\n'

In [91]: print(p.stdout.decode('utf-8'))
awk.md
eclipse.md
electric.md

In [93]: subprocess.getoutput('ls *')
Out[93]: 'awk.md\neclipse.md\nelectric.md\njava.md\nlinux.md\nmarkdown.md\nmatplotlib.md\npandas.md\npython.md\npython_debugger.md\npython_docopt_sample.py\nraspberry_pi.md\nREADME.md\nregexp.md\nsed.md\nshellscript.md\nvim.md\n\nimage:\n2020_06_20_violinplot.png\n2020_1024a0.PNG\n2020_1024a1.PNG\n2020_1024b0.PNG\n2020_1024d0.PNG\n2020_1024e.PNG\n2020_1024f0.PNG\n2020_1024g.PNG'

In [94]: subprocess.getoutput('ls *').split()
Out[94]: 
['awk.md',
 'eclipse.md',
 'electric.md' ]

In [99]: subprocess.getoutput('echo "hige"|sed -e "s/i/a/g"')
Out[99]: '"hage"'
```



### Links
[note.nkmk.me](https://note.nkmk.me/)
