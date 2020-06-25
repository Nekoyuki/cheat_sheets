### 基本

```sh
echo "hoge1 hoge2"|sed -r 's/hoge(.) hoge(.)/hige\1 hige\2/' # 正規表現 パターン再利用
```
