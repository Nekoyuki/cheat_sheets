### 判定
数値比較
```bash
-eq, -ne, -lt, -le, -gt, -ge
```

文字列比較
```bash
=, !=, =~ (regexp, quoteしたらだめよ)
```

ファイル比較
```bash
-nt (newer), -ot (older)
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
if [[ -s /tmp/hage.txt ]];then
    :
elif
    :
else
    :
fi
```

注意
[ の直後と ] の直前には必ず半角スペースが必要

### 構文
ループ
```bash
for i in 1 2 3 4
do
    :
done
```

case文
```bash
for i in `seq 2`
do
    case $i in
        1) echo "hage" ;;
        2) echo "hige" ;;
    esac
done
```

### 特殊変数
変数名|設定される値|
|-|-|
$?|終了ステータス|
$!|バックグラウンドで実行されたコマンドのプロセスID|
$-|set コマンド、もしくはシェルの起動時のフラグの一覧|
$$|コマンド自身のPID(プロセスID)|
$#|実行時に指定された引数の数|
$@ $\*|シェルスクリプト実行時、もしくはset コマンド実行時の全パラメータ, $0は含まれない|
$LINENO|この変数を使用している行の行番号|
${PIPESTATUS[@]}|パイプで連結した各コマンドの終了ステータス|
$1, $2, …, ${10}, …|setコマンドあるいは、位置パラメータ|
${@:3}|$3以降のパラメータ|
${@:3:5}|$3から$5までのパラメータ|

### 配列
```bash
array=()                       # 生成
echo ${#array[@]}              # 要素数
array=(hage "${array[@]}")     # 先頭に要素追加
array+=( hage )                # 末尾に要素追加
unset array[1]              　 # 削除
array2=(${array[@]})           # 配列のコピー

# 配列作成
array =(
    hage
    hige
    hoge
)

# 配列参照
for i in ${array[@]}
do
    echo $i
done
```

### 出力
```bash
echo "hage" >&2               # 標準エラー出力へ
echo "hage" > hage.txt 2>&1   # 標準エラー出力もファイルへ出力
hage.sh < echo "hage"         # 入力のリダイレクト
```

### ヒアドキュメント
```bash
cat <<EOF
hage
EOF
```

```<<-```で行頭のタブを取り除く
```bash
cat <<-EOF
    hage
EOF
```

### suffixを削る
```bash
${変数#パターン}   # 先頭から最短一致した部分を取り除く
${変数##パターン}  # 先頭から最長一致した部分を取り除く
${変数%パターン}   # 末尾から最短一致した部分を取り除く
${変数%%パターン}  # 末尾から最長一致した部分を取り除く
```

```bash
FILENAME=${0##*/}                           # ファイル名取り出し（拡張子あり）
BASENAME=`basename ${0%.*}`                 # ファイル名取り出し（拡張子なし）
BASENAME=`basename $0|sed 's/\.[^\.]*$//'`  # ファイル名取り出し（拡張子なし）
EXT=${0##*.}                                # 拡張子
DIR=${0%/*}                                 # ディレクトリ
DIR=`dirname $0`                            # ディレクトリ
```

### Date
```bash
date "+%Y_%m_%d_%H_%M"
```

### 計算 ```(( ))```で囲む
```bash
$((++i))    # インクリメント
print 'x\n' $(((0x7802ef & 0xfffff0) | 0x3))  # 16進でマスク+アンドして、16進(0x)で出力
printf "%x" $((0x${hoge} + 0x80))               # 16進で計算して、16進で出力
printf "%02d\n" 6                               # 先頭0埋め、結果は、06
A="hagehage3"; printf '0x%02x\n' $((${A:${#A}-1:1}<<4))  # 最後の数字を取り、ビットシフト
```

### Tips
数字かどうか判定
```bash
if [[ ${i} =~ ^[0-9]+$ ]];then
    echo "number"
fi
```

### リンク
https://shellscript.sunone.me/

[Bashにおける括弧類の意味](https://qiita.com/yohm/items/3527d517768402efbcb6)

[Bash $((算術式)) のすべて - A 基本編](https://qiita.com/akinomyoga/items/9761031c551d43307374)

bash 配列まとめ](https://qiita.com/b4b4r07/items/e56a8e3471fb45df2f59)
