### 基本

```sh
echo "hoge1 hoge2"|sed -r 's/hoge(.) hoge(.)/hige\1 hige\2/' # 正規表現 パターン再利用
echo "hage.sh"|sed 's/\.[^\.]*$//' # suffix (.*) を削る
echo "a b c"|sed -e 's/a/hage/' -e 's/b/hige/' -e 's/c/hoge/' # 複数の文字の変換
```
