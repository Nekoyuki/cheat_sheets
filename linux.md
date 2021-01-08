### コマンド
```sh
hostnamectl     # カーネルやOS情報
uname -r        # カーネルバージョン表示
depmod          # カーネルモジュールの依存関係リストを更新
```

### ネットワーク環境の確認
```sh
ifconfig
ip a

ip route                                            # ルーティングテーブル確認

more /etc/hostname                                  # ホスト名
more /etc/sysconfig/network-scripts/ifcfg-eth0      # eth0の設定ファイル

vi /etc/resolv.conf                                 # DNS設定, systemctl restart network
vi /etc/nsswitch.conf                               # ネットワークデータベースの検索順位定義
nslookup

systemctl status network

systemctl status NetworkManager
nmcli general hostname hoge                         # ホスト名変更
nmcli device                                        # デバイス確認
```

```ifcfg-eth0```の例, DHCPの場合
```sh
TYPE=Ethernet
BOOTPROTO=dhcp              # DCHPか固定IPか, dhcp/none
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_PEERDNS=yes
IPV6_PEERROUTES=yes
IPV6_FAILURE_FATAL=no
NAME=enp0s3
ONBOOT=yes                  # NICの自動起動, on/off
NM_CONTROLLED=NO            # NetworkManagerを使用しない
```

固定IPの場合
```sh
BOOTPROTO=none
IPADDR="172.16.0.10"
GATEWAY="172.16.0.1"        # デフォルトゲートウエイ設定
DEFROUTE=yes                # デフォルトゲートウエイ設定
DNS1="172.16.0.1"           # DNSサーバ
```

[@IT/ ネットワーク環境の確認](https://www.atmarkit.co.jp/ait/articles/0109/29/news004.html)

[ifconfigの出力結果に書いてあること](https://qiita.com/pe-ta/items/aff8db72530c6baa11b2)

[CentOS7 ifcfg設定](https://qiita.com/liqsuq/items/50173a587029e5d6ca23)

### ハードウエハ情報の確認
基本   
```sh
lshw                # /proc, /dev/, /sys の情報を参照
lshw -short         # 短縮表示
lshw -c cpu,memory
lshw -c network

lspci               # PCI device情報
lspci -vv           # 詳細

lsusb

lsmod               # module確認
modprobe hoge       # hogeモジュール読み込み
```

インストール
```
yum install lshw
yum install pciuti      # for lspci
yum install usbutils    # for lsusb
yum install ethtool
yum install net-tools           # ifconfig/route/netstat/arp
yum install iproute2            # ip addr/ip route/ss/ip neighbor
yum install bind-utils          # nslookup
repoquery --tree-requires lshw  # Package relationship tree view
```

応用   
```sh
lspci | grep 'Ethernet\|Network'    # どこのNICを使っているか
lshw -c network                     # どこのNICを使っているか

dmesg | grep "eth0\|eth1\|Ether"    # Driver名を調べる, igb, e1000とか

modinfo <driver name>
modinfo -F version <driver name>    # Driver version

ethtool -i eth0                     # eth0が読み込んでいるドライバ情報

udevadm info --query=all --path=/sys/class/net/eth0
udevadm info -a --path=/sys/class/net/eth0
```

応用その２、ドライバの入れ替え
```sh
lsmod | grep hoge
ifconfig eth<n> down
modprobe -r hoge
:
modprobe new_hoge
modinfo new_hoge
```

[【 lshw 】コマンド――ハードウェアの情報を表示する](https://www.atmarkit.co.jp/ait/articles/1904/11/news023.html)

[【 lspci 】コマンド――PCIデバイスの情報を表示する](https://www.atmarkit.co.jp/ait/articles/1901/18/news046.html)

[【 lsusb 】コマンド――USBデバイスの一覧と詳細情報を表示する](https://www.atmarkit.co.jp/ait/articles/1901/17/news028.html)

[UbuntuでNICを認識しない場合の対処法](https://qiita.com/hatt0519/items/06ac708f08d9570f2b93)

[ネットワークカードを認識させるには](https://www.atmarkit.co.jp/flinux/rensai/linuxtips/091usenic.html)

[PLANEX「USB-LAN1000R」レビュー](http://yurugadge-channel.com/article/179638968.html)

[【Linux】対処法: 有線LANのドライバe1000eが動作しない。](http://datyotosanpo.blog.fc2.com/blog-entry-190.html?id=VDPD#VDPD)

[Marvell Driver Downloads](https://driverdownloads.aquantia.com/)

### 起動/Boot
```sh
/etc/default/grub   # 基本設定ファイル

cp /boot/grub2/grub.cfg /boot/grub2/grub.cfg.org    # backup
grub2-mkconfig -o /boot/grub2/grub.cfg              # 
```

[CentOS7 ブートローダ周り](https://qiita.com/moukuto/items/c78f29f9bd1221baffca)

[【 grub2-set-default／grub-set-default 】コマンド――GRUB 2のデフォルト起動メニューを設定する](https://www.atmarkit.co.jp/ait/articles/1901/31/news048.html)


### コンソールの解像度変更

[CentOS 7インストール後の設定](https://www.storange.jp/2017/03/centos-7.html)

[コンソールを高解像度で表示する](http://linux.kororo.jp/cont/tips/console_vga.php)

### カーネル
```sh
zcat initramfs-xxx.img | cpio -idv  # initrdの中身をみる。圧縮の解凍になるので注意！
find . | cpio --quiet -H newc -o | gzip -9 -n > /boot/imagefile.img # cpioイメージの圧縮
```
[初期 RAM ディスク (initrd) を使用する](https://doc.kusakata.com/admin-guide/initrd.html)

[Linuxがブートするまで](https://keichi.dev/post/linux-boot/)

### ベンチマーク
bashで100万回ループ
```sh
cat /etc/centos-release
dmidecode -s processor-version
time for ((i=0;++i<1000000;))
>do
>:
>done
```

[お手軽なベンチマークあれこれ](https://luna2-linux.blogspot.com/2015/05/blog-post.html?m=0)

### デスクトップ環境
```sh
yum groups install "GNOME Desktop" -y
```

[CentOS7にGNOMEをインストールしてデスクトップ環境を使えるようにする](https://ips.nekotype.com/5100/)

### 時刻合わせ
```sh
date --set @"$(wget -q https://ntp-a1.nict.go.jp/cgi-bin/jst -O - | sed -n 4p | cut -d. -f1)"
date -s "$(curl -s --head http://www.google.co.jp | grep ^Date | cut -b 7-)"
date -s "$(CURL -L "http://www.google.com/" 2>&1 | grep ^Date | cut -d' ' -f2-)"
```

[ntpを使わずに時刻を合わせるワンライナー](https://qiita.com/pankona/items/258fed78c168918a8ad2)
[[CentOS]Webプロキシ配下からサーバー時刻を同期する方法~NTPコマンドを使わない方法~](https://blog.trippyboy.com/2014/centos/centosweb%E3%83%97%E3%83%AD%E3%82%AD%E3%82%B7%E9%85%8D%E4%B8%8B%E3%81%8B%E3%82%89%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E6%99%82%E5%88%BB%E3%82%92%E5%90%8C%E6%9C%9F%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)

