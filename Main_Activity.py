
"""模拟器运行后只需要挂在后台即可，不能最小化模拟器"""

import win32gui
import win32con
import win32api
import cv2

from Screen import Screen
from begin_action1 import begin_action1
from begin_action2 import begin_action2
from pipei import pipei

#TODO
#这里可以修改你的模拟器名称，只需改下面这条语句的第二个变量
handle = win32gui.FindWindow('Qt5QWindowIcon','联想模拟器')
hWnd_child_list = []
win32gui.EnumChildWindows(handle, lambda hWnd, param: param.append(hWnd), hWnd_child_list)
for child in hWnd_child_list:
    if 'RenderWindowWindow' == win32gui.GetWindowText(child):
        order = child
rect = win32gui.GetWindowRect(handle)  # 得到句柄坐标
length = rect[2] - rect[0]
width = rect[3] - rect[1]
print("长：", length)
print("宽：", width)

#win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)  # 显示窗口

win32gui.SetWindowPos(handle, win32con.HWND_BOTTOM, 0, 0, 0, 0, win32con.SWP_NOSIZE)  # 调整窗口位置
screen = Screen(win_title='', win_class=None, hwnd=handle)
screen.capture('test.png')
target = cv2.imread('test.png')

i = 1
cishu = int(input('进行任务的次数：'))
while (i <= cishu):
    print('第', i, '次任务开始')
    while begin_action1(target) > 0.3:
        screen.capture('test.png')
        target = cv2.imread('test.png')
        continue
    while begin_action1(target) <= 0.3:
        screen.capture('test.png')
        target = cv2.imread('test.png')
        #TODO
        #这里可以修改你电脑上的模拟器开始行动点击的坐标，只需修改下面这一行
        begin_action = win32api.MAKELONG(1437, 864)
        win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, begin_action)  # 模拟鼠标按下
        win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, begin_action)  # 模拟鼠标弹起
        continue
    while begin_action2(target) > 0.3:
        screen.capture('test.png')
        target = cv2.imread('test.png')
        continue
    while begin_action2(target) <= 0.3:
        screen.capture('test.png')
        target = cv2.imread('test.png')
        #TODO
        #这里可以修改你电脑上的模拟器开始行动点击的坐标，只需修改下面这一行
        begin_action = win32api.MAKELONG(1372, 689)
        win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, begin_action)  # 模拟鼠标按下
        win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, begin_action)  # 模拟鼠标弹起
        continue
    while pipei(target) > 0.3:
        screen.capture('test.png')
        target = cv2.imread('test.png')
        continue
    print('第', i, '次任务完成')
    while pipei(target) <= 0.3:
        screen.capture('test.png')
        target = cv2.imread('test.png')
        #TODO
        #这里可以修改你电脑上的模拟器结算界面点击的坐标，只需修改下面这一行
        begin_action = win32api.MAKELONG(933,531)
        win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, begin_action)    #模拟鼠标按下
        win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, begin_action)  #模拟鼠标弹起
    i = i + 1