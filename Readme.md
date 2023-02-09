# 前提

・Chromeをインストールできる(インストール済み)の環境で実行してください。

# 実行環境
・ Python3.6以上

・Ubuntu Desktop 22.04.1 LTS

・selenium==4.7.2

・Flask==2.2.2

# Chromeをインストールする方法

## Raspberry Piについて
　調べましたが、CPUアーキテクチャの問題から対応してない事が判明し、Chromeをインストールできませんでした。


　ChromeのOSS版であるchromiumは今回のソースコードには対応してません。

　そのため、Ubuntuを動かせるマシンを使う。もしくは、VPSを自前で契約し、そのインスタンス上でUbuntuを動かす必要があります。

1. パッケージを更新する

```
sudo apt update
sudo apt upgrade

```

2. Chromeのパッケージをダウンロード


```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

wgetがインストールされてないとエラーが出たら、このコマンドを実行してからchromeのパッケージをダウンロードする
```
sudo apt install wget
```


3. Chromeをインストール

```
sudo dpkg -i google-chrome-stable_current_amd64.deb
``` 

4. インストール時のエラー修復

```

sudo apt install -f
```

# 依存ライブラリのインストール

```
python3 -m pip install selenium flask
```

# port解放

私たちの実行環境では、BOTのサーバーと翻訳サーバーを分けた。
そのため、外部からアクセス出来るようにポートを開放する
同じサーバーでは不要

```
sudo apt install ufw
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 5493/tcp
```

VPSの場合は、このコマンドとは別でダッシュボードからも設定する必要がある。
これは、VPSによって変わってくるため `VPS名 外部アクセス` 等で調べれば出てくると思われる

# 実行
このように入力する。
ターミナルを開いてる間は常時起動するため、別作業等をする場合は、もう一つターミナルを起動する必要がある

`python3 main.py`

