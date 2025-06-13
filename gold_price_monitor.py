'''
Author: hbh
Date: 2025-06-13 10:49:29
LastEditors: hbh
LastEditTime: 2025-06-13 15:04:03
Description: 浙商/民生金价实时监控: 提供金价数值的实时价监控
             version: 1.0
'''

import logging
import requests
# 用于创建图形用户界面
import tkinter as tk  # 基础模块

# 设置日志记录
logging.basicConfig(level=logging.INFO)

# URL(实时金价api)
zsUrl = "https://api.jdjygold.com/gw2/generic/jrm/h5/m/stdLatestPrice?productSku=1961543816"
msUrl = "https://api.jdjygold.com/gw/generic/hj/h5/m/latestPrice"

def fetch_data():
    try:
        # 发送 GET 请求给浙商API
        zs_response = requests.get(zsUrl)
        zs_response.raise_for_status()  # 检查请求是否成功
        zs_data = zs_response.json()
        
        # 发送 GET 请求给民生API
        ms_response = requests.get(msUrl)
        ms_response.raise_for_status()  # 检查请求是否成功
        ms_data = ms_response.json()


        # 提取 price 和 upAndDownAmt for ZS
        zs_price = zs_data['resultData']['datas']['price']

        # 提取 price 和 upAndDownAmt for MS
        ms_price = ms_data['resultData']['datas']['price']

        # 更新 GUI - 动态更新
        zs_price_label.config(text=f"浙商 Price: {zs_price}")
        ms_price_label.config(text=f"民生 Price: {ms_price}")

    except requests.exceptions.RequestException as e:
        zs_price_label.config(text="ZS 请求出错")
        ms_price_label.config(text="MS 请求出错")
    except ValueError as e:
        zs_price_label.config(text="ZS 解析 JSON 失败")
        ms_price_label.config(text="MS 解析 JSON 失败")
    except KeyError as e:
        zs_price_label.config(text="ZS 数据缺失")
        ms_price_label.config(text="MS 数据缺失")

    # 每隔 1 秒钟调用一次 fetch_data 函数
    root.after(1000, fetch_data)

# 创建主窗口
root = tk.Tk()
root.title("金价监控")

# 设置窗口最小尺寸（宽度，高度）
root.minsize(width=200, height=100)
# 设置窗口置顶
root.attributes('-topmost', True)

# 初始化时 - 创建标签以显示价格和涨跌幅（浙商）
zs_price_label = tk.Label(root, text="浙商 Price: ", font=("Arial", 16))
zs_price_label.pack(pady=10)

# 初始化时 -创建标签以显示价格和涨跌幅（民生）
ms_price_label = tk.Label(root, text="民生 Price: ", font=("Arial", 16))
ms_price_label.pack(pady=10)

# 启动数据获取
fetch_data()

# 启动 GUI 主循环
root.mainloop()