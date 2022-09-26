# inAnalysis2Backend 使用說明
###### tags: 碩士
## 啟動方式
1. 在inAnalysis2Backend的根目錄，使用python 3.6，啟動src中的apps.py檔案
2. 指令 ```python3.6 ./src/apps.py```
## 資料庫位置和重製方式
* 資料庫有分成兩個部分，一個是SQLdata，另一個是file system
  * SQL是指標資料，指向file system的資料，方便查找，這些事需要清楚的部分之一。
    * 進入SQL之後，請保留原本的table名稱和schema，並且把除了course以外的所有table中的row全數刪除，即可完成這部分的重製。
  * file system 是用來儲存實際的資料，主要會有三個部分、使用者訓練出來的模型、使用者的資料、使用者執行遇到的執行狀況，這三者都需要進行清除，不過這些資料夾都在Incore裏頭，請到Incore專案查看說明。
