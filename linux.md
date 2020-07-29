### コマンド
```bash
hostnamectl     # カーネルやOS情報
uname -r        # カーネルバージョン表示
depmod          # カーネルモジュールの依存関係リストを更新
```

### ネットワーク環境の確認
```bash
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
```bash
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
```bash
BOOTPROTO=none
IPADDR="172.16.0.10"
GATEWAY="172.16.0.1"        # デフォルトゲートウエイ設定
DEFROUTE=yes                # デフォルトゲートウエイ設定
DNS1="172.16.0.1"           # DNSサーバ
```


リンク   
[@IT/ ネットワーク環境の確認](https://www.atmarkit.co.jp/ait/articles/0109/29/news004.html)

[ifconfigの出力結果に書いてあること](https://qiita.com/pe-ta/items/aff8db72530c6baa11b2)

[CentOS7 ifcfg設定](https://qiita.com/liqsuq/items/50173a587029e5d6ca23)

### ハードウエハ情報の確認
基本   
```bash
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
```bash
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
```bash
lsmod | grep hoge
ifconfig eth<n> down
modprobe -r hoge
:
modprobe new_hoge
modinfo new_hoge
```

リンク   
[【 lshw 】コマンド――ハードウェアの情報を表示する](https://www.atmarkit.co.jp/ait/articles/1904/11/news023.html)

[【 lspci 】コマンド――PCIデバイスの情報を表示する](https://www.atmarkit.co.jp/ait/articles/1901/18/news046.html)

[【 lsusb 】コマンド――USBデバイスの一覧と詳細情報を表示する](https://www.atmarkit.co.jp/ait/articles/1901/17/news028.html)

[UbuntuでNICを認識しない場合の対処法](https://qiita.com/hatt0519/items/06ac708f08d9570f2b93)

[ネットワークカードを認識させるには](https://www.atmarkit.co.jp/flinux/rensai/linuxtips/091usenic.html)

[PLANEX「USB-LAN1000R」レビュー](http://yurugadge-channel.com/article/179638968.html)

[【Linux】対処法: 有線LANのドライバe1000eが動作しない。](http://datyotosanpo.blog.fc2.com/blog-entry-190.html?id=VDPD#VDPD)

[Marvell Driver Downloads](https://driverdownloads.aquantia.com/)

### 起動/Boot
```bash
/etc/default/grub   # 基本設定ファイル

cp /boot/grub2/grub.cfg /boot/grub2/grub.cfg.org    # backup
grub2-mkconfig -o /boot/grub2/grub.cfg              # 
```

リンク   
[CentOS7 ブートローダ周り](https://qiita.com/moukuto/items/c78f29f9bd1221baffca)

[【 grub2-set-default／grub-set-default 】コマンド――GRUB 2のデフォルト起動メニューを設定する](https://www.atmarkit.co.jp/ait/articles/1901/31/news048.html)


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
