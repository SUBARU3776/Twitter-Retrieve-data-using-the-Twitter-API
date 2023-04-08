# Twitter-Retrieve-data-using-the-Twitter-API
### このPythonスクリプトは指定したユーザーの最新のツイート情報をbearer tokenを使って取得し、Pandasデータフレームに格納してCSVファイルに保存するものです。

##### 具体的には、以下のような処理を行っています。

- HTTPリクエストを送信するためのrequestsライブラリーをインポートします。
- headers変数にbearer tokenをAuthorizationヘッダーに含めるための辞書を作成します。
- response.raise_for_status()を使用してステータスコードが正常であるかを確認します。
- next tokenを利用し、抽出可能なツイート情報が無くなるまで繰り返します。
- データをPandasのデータフレームに変換し、データフレームをエクスポートするためのCSVファイルに書き出します。
- データフレームの最初の5つの行が出力されます。
- 付属のフォルダには正規化と可視化のためのスクリプトが格納されています。<br>

#### 実行にはTwitter APIの認証情報が必要です。
##### 取得できるデータについては、APIリファレンスインデックスをご参照ください。
https://developer.twitter.com/en/docs/api-reference-index<br>

***********************************************************************************************************************************************************
### This Python script retrieves the latest tweet information for a specified user using a bearer token, stores it in a Pandas data frame, and saves it to a CSV file.

##### Specifically, the following process is performed.

- Import the requests library to send HTTP requests.
- Create a dictionary in the headers variable to include the bearer token in the Authorization header.
- Use response.raise_for_status() to check if the status code is normal.
- Use next token and repeat until there is no more tweet information available for extraction.
- Convert the data into a Pandas data frame and export the data frame to a CSV file for export.
- The first five rows of the dataframe will be output.
- The attached folder contains scripts for normalization and visualization.<br>

#### Twitter API credentials are required for execution.
#### Please refer to the API reference index for the data that can be obtained.
https://developer.twitter.com/en/docs/api-reference-index
