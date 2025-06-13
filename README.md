<!--
 * @Author: hbh
 * @Date: 2025-06-13 15:32:00
 * @LastEditors: hbh
 * @LastEditTime: 2025-06-13 15:56:05
 * @FilePath: \gold-price-monitor\README.md
 * @Description: 
-->
# gold-price-monitor
京东金融的民生/浙商实时金价监控

目录结构
```markdown
gold-price-monitor/
├── gold_price_monitor.py
├── app.icns                # 图标文件（macOS 专用）
├── requirements.txt        # 依赖列表
└── README.md
```


## 打包命令

`pyinstaller --onefile --windowed --name "实时金价" --icon=icon.ico gold_price_monitor.py`


## 运行命令
`python gold_price_monitor.py`
`python hot_reload_launcher.py`


## 依赖包
1. pyinstaller==5.13.2  打包成exe可执行文件
2. 使用 watchdog 监控文件变化，重启程序（推荐）
    `pip install watchdog`
3. 



## 代码详解

`except requests.exceptions.RequestException as e`: 是用来捕获网络请求过程中出现的各种异常，比如连接失败、超时、返回非200等

`except (ValueError, KeyError) as e`: 是用来处理数据解析过程中的错误，比如数据格式错误、缺少字段等。

异常类型	触发原因	GUI 显示内容
RequestException	网络请求失败（如连不上服务器、超时等）	"请求出错"
ValueError	API 返回的内容不是有效的 JSON	"解析 JSON 失败"
KeyError	JSON 数据中缺少需要的字段（如 price）	"数据缺失"