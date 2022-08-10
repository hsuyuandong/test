from flask import Flask #載入Flask
#建立application物件，可以設定靜態檔案的路徑處理
app=Flask(
    __name__,
    static_folder="dao",  #靜態檔案的資料夾名稱，要對應到左方資料夾
    static_url_path="/hui"  #靜態檔案對應的網址路徑，若要取名則舉例為/abc
) 
#所有在 daohui 資料夾底下的檔案，都對應到網址路徑 /檔案名稱


#建立路徑 / 對應的處理函式
@app.route("/")
def index():   #回應路徑 / 的處理函式
    return "Hello Flask"  #回傳網站首頁內容

#建立路徑 /data 對應的處理函式
@app.route("/data")
def Bigdata():
    return "My data"

#動態路由:建立路徑/user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def Name(username):
    if username=="東東":
        return "你好管理者 "+username
    else:
        return "歡迎 "+username


#啟動網站伺服器，可透過port參數指定埠號
app.run(port=9527)
