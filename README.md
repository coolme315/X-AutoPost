本ソフトウェアはconfig.pyで設定をし、X-AutoPost.exeを起動するだけで
config.pyで指定したメッセージをXにポストするソフトです。

必要なものは以下

1.Xのアカウント

2.XのAPIキー(5種。API,API SECRET,Bearer Token,ACCESS Token,Access Token Secret)

3.config.pyを編集できるテキストエディタ

1と2は

https://qiita.com/neru-dev/items/857cc27fd69411496388

を参考に取得してください。

動作確認環境はWindows10

ビルドバージョンはPython3.9.7

たぬえさ3にも対応しています。

引数1にポストしたい文字列を入れるとその文字列をポストします。

リリース時点で改行には対応していません。

SpecialThanks


翻訳ちゃん(さよなり様)
https://github.com/sayonari/twitchTransFreeNext

DoorBellBot(L4yLa様)
https://github.com/L4yLa/TwitchBots

【Python】X API v2経由でポスト（ツイート）する(holy様)
https://zenn.dev/holy0306/articles/009b5b4744e230
