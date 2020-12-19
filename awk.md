### 基本
awk 'パターン {アクション}' ファイル名

```sh
ls -l | awk '$5 >= 1000000 { print }'   # ファイルサイズが約1MB以上の行を出力する

awk '$3 == "hage" { print $5 }' hages.txt   #
awk '$0 ~/hage/{ print $5 }' hages.txt   # 行全体で正規表現マッチ
awk '$1 ~/^d/ && $9 ~/^\.d/'{ print $5 }' hages.txt   # 第１フィールドと第９フィールドで正規表現マッチ
awk 'NR==2 {print $3}'  # 2行目の3番目のやつを出力
```
