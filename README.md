# inAnalysis2Backend 使用說明
## 啟動方式
1. 在inAnalysis2Backend的根目錄，使用python 3.6，啟動src中的apps.py檔案
2. 指令 ```python3.6 ./src/apps.py```
## 資料庫位置和刪除方式
* 資料庫有分成兩個部分，一個是SQLdata，另一個是file system
  * SQL是指標資料，指向file system的資料，方便查找，這些是需要清除的部分之一。
    * 進入SQL之後，請保留原本的table名稱和schema，並且把除了course以外的所有table中的row全數刪除，即可完成這部分的重製。
    
  * file system 是用來儲存實際的資料，主要會有三個部分、使用者訓練出來的模型、使用者的資料、使用者執行遇到的執行狀況，這三者都需要進行清除，不過這些資料夾都在Incore裏頭，請到Incore的部分看說明。
## 重要資訊
* 因為github為公開，重新安裝時，需要使用者在根目錄中新建一個secret.cfg，詳細需要填寫的內容以下

````
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