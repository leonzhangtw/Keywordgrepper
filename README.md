IoT Firmware Keyword Grepper Tools 
===


# Description
利用正則表達式比對符合規則的檔案名稱、檔案類型、檔案內特定字串，將結果輸出成excel報表(.xlsx)的自動化檢測程式。

使用者可自由新增規則。

未來會支援更多不同的檔案類型以及收尋有密碼保護的檔案。

適用於Linux、Windows、MacOS
建議使用Python 2.7.x環境執行
下載後，目錄內會以下四個檔案

* README.md 說明檔
* Patternset.py 規則清單
* Keywordsgreper.py 檢測程式
* setup.ini 參數設定檔


# Features


# Usage
## Step1:修改參數檔setup.ini
設定[Read Path]的p1參數，指定要收尋的資料夾的路徑。
設定[Output Path]的o參數，指定Report要輸出在哪。

Example:
```bash=
[Read Path]
p1 = /
[Output Path]
o =  /
```


## STEP2 執行程式
```=bash
python Keywordsgreper.py setup.ini
```

# 備註
可自由修改Patternset.py，參考範例後，客制自己的規則function後，加入Patternset Class的__init__內呼叫即可。

