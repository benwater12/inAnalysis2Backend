# inAnalysis2Backend 使用說明
## 啟動方式
1. 在inAnalysis2Backend的根目錄，使用python 3.6，啟動src中的apps.py檔案
2. 指令 ```python3.6 ./src/apps.py```
## 資料庫位置和刪除方式
* 資料庫有分成兩個部分，一個是SQLdata，另一個是file system
  * SQL是指標資料，指向file system的資料，方便查找，這些是需要清除的部分之一。
    * 進入SQL之後，請保留原本的table名稱和schema，並且把除了course以外的所有table中的row全數刪除，即可完成這部分的重製，同時，**如果已經將file system中的database刪除的話，這一步一定要做! 否則會出現錯誤**
    
  * file system 是用來儲存實際的資料，主要會有三個部分、使用者訓練出來的模型、使用者的資料、使用者執行遇到的執行狀況，這三者都需要進行清除，不過這些資料夾都在Incore裏頭，請到Incore的部分看說明。
## 重要資訊
* 因為github為公開，重新安裝時，需要使用者在根目錄中新建一個secret.cfg，詳細需要填寫的內容以下
* 然後，要登入inanalysis的信箱(密碼在桌面上)，同時把google_token.pickle刪除，找一個實驗室的朋友，新註冊一個帳號，之後google會進行網頁認證，走過一次流程，程式碼會更新一個google_token.pickle。

```
host=the_IP_of_backend
port=the_port_of_backend
secretkey=the_Secret_Key(can be any string)
dbhost=the_IP_of_sqlDB
dbuser=the_username_of_sqlDB
dbpwd=the_password_of_sqlDB
dbschema=the_schema_of_sqlDB
corehost=the_IP_of_Incore
coreport=the_port_of_Incore
frontendhost=the_IP_of_frontend
frontendport=the_port_of_frontend
```
## SQL Schema
![Screenshot_2022-09-26_16-24-23](https://user-images.githubusercontent.com/22317334/192229775-7857cf29-b66b-4862-82f7-5ce8f951b929.png)
![Screenshot_2022-09-26_16-24-30](https://user-images.githubusercontent.com/22317334/192229785-5e10bfe0-ab73-482e-bfd8-aef77bdde291.png)
