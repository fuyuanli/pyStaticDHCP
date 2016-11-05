from dhcpy.Device import *
from dhcpy.Generate import *

devices = Device()
# 新增 HostNmae 為  FuYuanServer 的裝置, 期限為一天
devices.add("FuYuanServer","10:d:00:3:0",1)

# 檢查是否過期
devices.checkDays()

#產生設定檔
dhcpd = Generate()
dhcpd.conf()
