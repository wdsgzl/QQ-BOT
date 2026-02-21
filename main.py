import win32gui
import win32con
import win32clipboard as w
import time
from datetime import datetime, timedelta
import config
import weather

TARGET_HOUR = 8
TARGET12_HOUR = 20
TARGET_MINUTE = 5
CITY_CODE = config.city_code
QQ_WINDOW_NAME = config.name

def send(name, msg):
    #打开剪贴板
    w.OpenClipboard()
    #清空剪贴板
    w.EmptyClipboard()
    #设置剪贴板内容
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    #获取剪贴板内容
    date = w.GetClipboardData()
    #关闭剪贴板
    w.CloseClipboard()
    #获取qq窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('unfind window')
    #显示窗口
    win32gui.ShowWindow(handle,win32con.SW_SHOW)
    #把剪切板内容粘贴到qq窗口
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
    #按下后松开回车键，发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    #time.sleep(1)#延缓进程
    
def init(msg):
    print('start')
    send(config.name, str(msg.to_string(index=False, header=False)))
    print(msg)
    print('end')

def judge_time():
    now = datetime.now()
    if (now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE) or (now.hour == TARGET12_HOUR and now.minute == TARGET_MINUTE):
        return True
    return False
def calculate_sleep_seconds(target_hour=8, target_minute=0):
    """计算距离下一个目标时间（如8:00）需要休眠的秒数"""
    now = datetime.now()
    # 构造今天的目标时间
    target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    
    # 如果当前时间已过目标时间，取明天的目标时间
    if now > target_time:
        target_time += timedelta(days=1)
    
    # 计算精确的休眠秒数
    sleep_seconds = (target_time - now).total_seconds()
    # 确保休眠时间为正数
    return max(sleep_seconds, 0)

if __name__ == '__main__':

   while True:
        if judge_time():
            init(weather.get_weather(CITY_CODE))
            time.sleep(43200)
        else:
            sleep_sec = calculate_sleep_seconds(TARGET_HOUR, TARGET_MINUTE)
            print(f'[{datetime.now()}] 距离下次发送还有 {sleep_sec/3600:.2f} 小时，开始休眠')
            time.sleep(sleep_sec)
       #if(current_time := datetime.now()=)
        #time.sleep(10)
        #init(weather.get_weather('101190408'))