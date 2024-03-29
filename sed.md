### 基本

```sh
echo "hoge1 hoge2" |sed -r 's/hoge(.) hoge(.)/hige\1 hige\2/' # 正規表現 パターン再利用
echo "hage.sh" |sed 's/\.[^\.]*$//' # suffix (.*) を削る
echo "a b c" |sed -e 's/a/hage/' -e 's/b/hige/' -e 's/c/hoge/' # 複数の文字の変換
echo "hage=neko hige=mike" |sed -r 's/.* hige=([a-zA-Z.0-9]+).*/\1/'  # 空白か行末までのマッチ
cat hage.txt |sed '/hage/d'     # マッチする行の削除
```

### 正規表現

|説明|Perl|sed|
|---|---|---|
|数字|\d|[0-9]|
|数字以外|\D|[^0-9]|
|アルファベット、数字、アンダーバー|\w|[a-zA-Z_0-9]|
|アルファベット、数字、アンダーバー以外|\W|[^a-zA-Z_0-9]|
|空白文字|\s|[\f\n\r\t]|
|空白文字以外|\S|[^\f\n\r\t]|

|説明|Perl|sed|
|---|---|---|
|グループ化|(foo)|\(foo\)|
|直前の文字の0個または1個|?|\?|
|直前の文字の1個以上|+|\+|
|直前の文字のm個|{m}|\{m\}\d|
|連続スペース||[]*|
