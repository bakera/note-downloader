# note-downloader

note.muの記事をダウンロードして保存するだけのPythonスクリプト

## 使い方

### 特定の記事を保存する場合

コマンドラインから以下のように実行します。

python note-downloader.py {note_id}

{note_id} はnoteの記事URLの末尾につくIDです。


### マガジンに所属する記事全てを保存する場合

python note-magazine-downloader.py {magazine_id}

{magazine_id} はnoteのマガジンのURLの末尾につくIDです。


### 例:

記事 https://note.mu/bakera/n/nefa5dd4a64db を保存するなら、

```bash
python note-downloader.py nefa5dd4a64db
```

マガジン https://blog.bengo4.com/m/mefab063665cc 全体を保存するなら、

```bash
python note-magazine-downloader.py mefab063665cc
```


## 保存されるファイル

{note_id}.html というファイル名のファイルがカレントディレクトリに作られます。

中身は note のAPIから取得した記事本文のHTML断片です。
断片を単にそのまま保存するので、正当なHTMLにはなっていません。
必要に応じて外側のHTMLを追加する必要があります。

### 画像の扱い

記事内に画像がある場合でも、画像ファイルは保存しません。
img要素のsrc属性にabsolute-URLで書かれているので、保存したHTMLをローカルで開くと表示されたりはします。
