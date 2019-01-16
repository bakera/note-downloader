# note-downloader

note.muの記事をダウンロードして保存するだけのPythonスクリプト

## 使い方

コマンドラインから以下のように実行します。

python note-downloader.py {note_id}

{note_id} はnoteの記事URLの末尾につくIDです。

### 例:

https://note.mu/bakera/n/nefa5dd4a64db を保存するなら、
python note-downloader.py nefa5dd4a64db


## 保存されるファイル

{note_id}.html というファイル名のファイルがカレントディレクトリに作られます。

中身は note のAPIから取得した記事本文のHTML断片です。
断片を単にそのまま保存するので、正当なHTMLにはなっていません。
必要に応じて外側のHTMLを追加する必要があります。

### 画像の扱い

記事内に画像がある場合でも、画像ファイルは保存しません。
img要素のsrc属性にabsolute-URLで書かれているので、保存したHTMLをローカルで開くと表示されたりはします。
