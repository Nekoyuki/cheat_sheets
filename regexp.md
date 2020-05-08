|文字|説明|同様|例|マッチする|マッチしない|
|---|---|---|---|---|---|
|\d|任意の数字|[0-9]||||   
|\D|任意の数字以外|[^0-9]||||
|\s|任意の空白文字|[\t\n\r\f\v]||||
|\S|任意の空白文字以外|[^\t\n\r\f\v]||||
|\w|任意の英数字|[a-zA-Z0-9_]||||
|\W|任意の英数字以外|[\a-zA-Z0-9_]||||
|\A|文字列の先頭|^||||
|\Z|文字列の末尾|$||||
|.|任意の一文字|-|a.c|abc,acc,aac|abbc,accc|
|^|文字列の先頭|-|^abc|abcdef|defabc|
|$|文字列の末尾|-|abc$|defabc|abcdef|
|*|０回以上の繰り返し|-|ab*|a,ab,abb,abbb|aa,bb|
|+|１回以上の繰り返し|-|ab+|ab,abb,abbb|a,aa,bb|
|?|０回または１回|-|ab?|a,ab|abb|
|{m}|m回の繰り返し|-|a{3}|aaa|a,aa,aaaa|
|{m,n}|m〜n回の繰り返し|-|a{2, 4}|aa,aaa,aaaa|a,aaaaa|
|[]|集合|-|[a-c]|a,b,c|d,e,f|
|[^]|集合以外|-|[^a-c]|d..z|a,b,c|
|縦線|和集合（または）|-|a縦線b|a,b|c,d|
|()|グループ化|-|(abc)+|abc,abcabc|a,ab,abcd|


https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3
