**移動 ```motion```**

```vim
gm          "表示されている画面の真ん中にジャンプ
25%         "ファイル全体の25%位置にある行に移動。
```

[http://vim-jp.org/vimdoc-ja/motion.html]

**ジャンプ ```jump-motion```**

```vim
CTRL+O      "ジャンプしてきた元の古いカーソル位置に戻る(移動)。
CTRL+I      "CTRL+Oの逆に移動。
:ju[mps]    "ジャンプリスト表示
```

[http://vim-jp.org/vimdoc-ja/motion.html#jump-motions]

```vim
g;          "最後の変更箇所へ移動
g,          "g;の逆の移動。
```

[http://vim-jp.org/vimdoc-ja/motion.html#change-list-jumps]


**囲む ```surround```**

```vim
ds'         " d(elete)s(urrounding)'
di'         " d(elete)i(nside of)'

cs'"        " c(hange)s(urrounding)'(with)"
ci'         " c(hange)i(nside of)'

S'          " S(urrounded by visual mode with)'
vawS'       " v(isual)aw(ord)S(urround)(with)'

yss'        " y(ank)s(urround)s(entence with)'
ysiw'       " y(ank)s(urround)i(nner)w(ord with)'
```

[http://vim-jp.org/vimdoc-ja/motion.html#object-select]

[https://github.com/tpope/vim-surround]

**大文字小文字変換 ```swap upper/lower letter```**

```vim
vwU	"ヴィジュアルモード(v)でワード単位(w)選択し、大文字変換(U)
vwu	"ヴィジュアルモード(v)でワード単位(w)選択し、小文字変換(u)
~ "大文字 <-> 小文字
```

**ファイルを挿入する ```insert```**

```vim
:r ファイル	"指定したファイルの内容を現在のファイルに流しこみ
:r !コマンド	"コマンド実行結果を現在のファイルに流しこみ
```

[https://vim-jp.org/vimdoc-ja/insert.html#inserting-file]

**コマンドラインウィンドウ ```command line window```**

```vim
q:
ENTER "カーソル行のコマンドを再度、実行
CTRL + c "カーソル行のコマンドを、コマンドラインにコピー
```

[https://vim-jp.org/vimdoc-ja/cmdline.html#cmdline-window]

[https://vim-jp.org/vimdoc-ja/usr_20.html#20.5]

[http://nanasi.jp/articles/howto/editing/use-command-history.html]

**レジスタ ```register```**

```vim
:reg
"0p "レジスタ0をペースト
```

**バッファー```buffer```**

```vim
:ls "バッファー一覧を表示
:b 1 "バッファー１を開く
```

**ビジュアルモード ```Visual mode```**

```vim
CTRL + V (Visual Block) + $ + A (Append)    "不揃いの複数の行末に何かを追加する方法。
```

[http://vim-jp.org/vimdoc-ja/visual.html]

**繰り返しコマンド実行 ```repeating``` ```command```**

```:global``` 条件を指定その条件にマッチするときだけ処理を実行する。
```vim
:g/{pattern}/{cmd}	             "{pattern}にマッチする{cmd}を実行する。
:g/^/cmd	                      "すべての行に対して{cmd}を実行する。
:g/^/ if {expr}|{cmd}	        "{expr}の条件に合う行に対して{cmd}を実行する。
:g/{pattern}/if {expr}|cmd	    "{pattern}と{expr}の条件に合う行に対して{cmd}を実行する。
```

```vglobal``` 条件を指定その条件にマッチしないときだけ処理を実行する。
```vim
:v/{pattern}/{cmd}	             "{pattern}にマッチしない{cmd}を実行する。
:v/^/if {expr}|{cmd}	        "{expr}の条件に合わない行に対して{cmd}を実行する。
:v/{pattern}/if {expr}|{cmd}	"{pattern}と{expr}の条件に合う行に対して{cmd}を実行する。
```

```vim
:g/hage/norm gJ                              " g("hage"にマッチした行でコマンド実行) > gJ(空白無で２行にわたる行を連結) 
:g/hage/m 0                                  " g("hage"にマッチした行でコマンド実行) > 行を逆順に並べ替える
:%g/^[0-9]/d                                 " 先頭が数字の行を削除。 %(全体選択) > g(パターンにマッチした行でコマンド実行) > d(削除)
:%s/\s\+$//                                  " 行末の空白を取り除く。 %(全体選択) > s(置換) > \s(空白メタ) > +(複数回マッチ) > $(行末マッチ)
:v/\S/d                                      " 空白行を消す。 v(パターンにマッチしない行でコマンド実行) > \S(空白以外メタ) > d(削除)
:g/^$/d                                       " 空白行を消す。 g(パターンにマッチ行したでコマンド実行) > ^$(空行) > d(削除)
:%norm jdd                           " 1行置きに削除
:g/^/+d                                 "偶数行を削除
:1d|g/^/+d　　　　　　　  "奇数行を削除
:g/^/ if line('.') % 2 == 0 | s/aaa/bbb/g     " 偶数行だけ置換する
```

[http://vim-jp.org/vimdoc-ja/various.html#:normal-range]

[http://vim-jp.org/vimdoc-ja/repeat.html#repeating]

[http://vim-jp.org/vimdoc-ja/usr_12.html]

**EXコマンド**   
[http://vim-jp.org/vimdoc-ja/vimindex.html#ex-cmd-index]

**文字クラス（メタ文字）**   
[http://vim-jp.org/vimdoc-ja/pattern.html#/character-classes]

**正規表現 ```regexp``` ```pattern```**

[http://vim-jp.org/vimdoc-ja/pattern.html#pattern-overview]

**ユナイト ```Unite```**

```vim
:Ur "レジスタ一覧表示
:Ub "バッファー一覧表示
:Uf "ファイル一覧表示
```
