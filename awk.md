### 基本
awk 'パターン {アクション}' ファイル名

```awk
ls -l | awk '$5 >= 1000000 { print }'   # ファイルサイズが約1MB以上の行を出力する

awk '$3 == "hage" { print $5 }' hages.txt   #
awk '$0 ~/hage/{ print $5 }' hages.txt   # 行全体で正規表現マッチ
awk '$1 ~/^d/ && $9 ~/^\.d/'{ print $5 }' hages.txt   # 第１フィールドと第９フィールドで正規表現マッチ
awk 'NR==2 {print $3}'  # 2行目の3番目のやつを出力
echo "aaa139"|awk '{printf "%1d.%2d\n", substr($1,4,1), substr($1,5,2)}'  # 139を抜き取り1.39と表示
echo "a_b_c" |awk -F'_' '{print $2}'  # フィールドセパレータ
```

### ループ
```awk
awk '\
NR==1{ cnt=split($0, array, ","); } \                               # splitで$0を","で分解して、arrayに入れる
END{ for ( i=1; i<=10; i++){ printf "%-15s %-12s\n", array; } } \   # ループでprintfする
'
```

### リンク

[awkのまとめ](http://www.osaka-kyoiku.ac.jp/~kokugo/nonami/awk/awkmini.html)

