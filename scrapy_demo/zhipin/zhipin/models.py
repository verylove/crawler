#encoding: utf-8
from datetime import datetime,timedelta


class ProxyModel(object):
    EXPIRING_DELAY = 5

    def __init__(self,proxy_dict):
        self.ip = proxy_dict['ip']
        self.port = proxy_dict['port']
        self.expire_str = proxy_dict['expire_time']
        self.proxy = "https://{}:{}".format(self.ip,self.port)

    @property
    def expire_time(self):
        date_str,time_str = self.expire_str.split(" ")
        year,month,day = date_str.split("-")
        hour,minute,second = time_str.split(":")
        date_time = datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
        return date_time

    @property
    def is_expiring(self):
        now = datetime.now()
        # 如果在10秒钟后即将过期
        if (self.expire_time-now) < timedelta(seconds=self.EXPIRING_DELAY):
            return True
        else:
            return False

