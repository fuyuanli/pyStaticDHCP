pyStaticDHCP
===
## 簡介
使用 Python3 產生 Static DHCP 設定檔。
 
 - 依照 macAddress 自動分配IP
 - 可以設定有效天數。
 - 裝置失效後，IP 將會釋放，不會浪費。


## 使用方法

### 引入函式
```python
from dhcpy.Device import *
from dhcpy.Generate import *
```

### 新增裝置
新增一台裝置，並將資料寫入users.json
```python
HOSTNAME = "myHost"
MACADDRESS = "00:00:00:00:00:00"
DAYS = 3

myDevice = Device()
myDevice.add(HOSTNAME,MACADDRESS,DAYS)
```
### 檢查過期裝置
檢查是否有裝置過期，有的話刪除裝置
```python
myDevice.checkDays()
```

### 產生 dhcpd.conf
```python
dhcpd = Generate()
dhcpd.conf()
```

## 設定 dhcp 
相關設定都在 dhcp.json， subnet 的部份在 subnet.json
