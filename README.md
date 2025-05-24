### algorithm-in-python

## 環境設定(Anaconda で python3.11.7 を使用)

# 1. 現状の確認

Anaconda にある全ての環境を確認

```cmd
. % conda info -e
```

現環境にインストールされているライブラリ一覧確認

```cmd
. % conda list
```

# 2. 仮想環境の作成

```cmd
. % conda create -n <環境名> python=<利用したいバージョン> [<ライブラリ名>=<利用したいバージョン>]
```

# 3. 仮想環境の切り替え

```cmd
. % conda activate <環境名>
```

# 参考

https://qiita.com/ell/items/fb60d2fd765650417c7a
