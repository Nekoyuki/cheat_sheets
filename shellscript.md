### 判定
数値比較
```bash
-eq, -ne, -lt, -le, -gt, -ge
```

文字列比較
```bash
=, !=
```

ファイル比較
```bash
-nt, -ot
```

その他
|オプション|意味|
|-|-|
|-z|文字列長0か|
|-n|文字列長が0より大きいか|
|-e|パスが存在するか|
|-d|ディレクトリが存在するか|
|-f|ファイルが存在するか|
|-L|リンクが存在するか|
|-s|ファイルサイズが0より大きいか|
|-r|ファイルが読み取り可能か|
|-w|ファイルが書き込み可能か|
|-x|ファイルが実行可能か|

AND/OR/NOT
```bash
&&, ||, !
```

if文
```bash
if [ -s /tmp/hage.txt ];then
    :
elif
    :
else
    :
fi
```

注意
[ の直後と ] の直前には必ず半角スペースが必要

### ループ
```bash
for i in 1 2 3 4
do
    :
done

```

### 終了ステータス
```bash
echo $?
test "abc" = "abc" ; echo $?    # 例
```

### suffixを削る
```bash
BASENAME=`basename ${0%.*}`
```

### Date
```bash
date "+%Y_%m_%d_%H_%M"
```

### リンク
https://shellscript.sunone.me/
