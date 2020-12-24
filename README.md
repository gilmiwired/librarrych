# 図書室空席確認システム　(librarycheack)

ここはホームページ用リポジトリよ

***アクセス数***<br>
<img src="https://profile-counter.glitch.me/librarycheck/count.svg" alt="" />

まぁ四人しか編集者がいないんで適当にブランチ切って適当に編集しちゃってください。

***

**注意点とか確認してほしいとことかそういうアレ**<br>

- commit時に競合するとき
	* 一応gitの標準機能で競合箇所を指摘してくれますが
	  競合するところが出てきそうなので(特にindex.html)新規ファイル作成時、書き換るときcommit時、にコメントするのを忘れないように

- 大幅な変更等をした場合
	* mdファイルを書き換えるかコミット時にdescriptionを書いといてください。

- やってほしいこと、できなかったとこがあったら
	* issueを書いてください。個別に連絡してくれても結構ですが

- 作業時
	* html、スクリプトを書くときデザインの確認として
	　atom-html-preview(atom内にあるッケージ)を使うと作業がはかどると思います。
    * できればtabを使うように

~~どんどんpullリクエスト送ってください。マージします。~~

***

***how to use***
- ラズパイ側
 * img　フォルダ内の webcam.pyを実行しましょう。

以上

- バックアップを残したいときはbackup/backup.pyを実行しましょう
 * バックアップはラズパイ側のローカルリポジトリにしか残らないので注意

サイト : [site](https://ibc-libcheck.netlify.app/)
資料等 : [google drive](https://drive.google.com/drive/folders/1YB1rYuMj9Dod96YIM1sCtQFkhL5izmdC?usp=sharing)
