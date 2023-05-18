# 编写原因

---

> Metersphere平台可导入postman，har，jmeter，swagger和metersphere的格式，但在尝试所有格式后，选择使用metersphere格式最为合适：metersphere的json格式相对易读，且导入时可以设置test的内容，而其他格式仅仅只能放入api。

# 功能介绍

---

- 通过开始输入的keyword，将捕获的接口过滤，只留有包含keyword的接口
- 去重过滤后的接口，保证只录入一遍
- 将接口实时的保存为metersphere格式的json文件，保存于当前目录

# 使用方法

---

## 选择版本

- m2m提供了三个版本，m2m_m，m2m_i，m2m.exe，分别对应mac M芯片，mac Inter芯片，windows x64三个版本，对应使用的电脑开启响应版本。

- 现已上传pypi，可以直接通过命令行 pip install viewm2m 下载，命令行viewm2m可直接运行。

![](https://secure2.wostatic.cn/static/tLRhYwzMFXid2Gb6imL6MY/image.png?auth_key=1681868014-axR5exhfz92zKV87hS63vZ-0-5b0ea666065d5c00f4b5fad5a1ed51e9)

## 安装并配置SwitchyOmega

- 安装SwitchyOmega
以chrome为例：打开扩展模式后，下载[https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN)

    ![](https://secure2.wostatic.cn/static/9YKV5ySjAcXUh81bzBygDR/image.png?auth_key=1681868014-kPzYtn9MHyr98PLriyd1D5-0-0e26cb32fb33a809778051b31f1f1d60)
- 配置SwitchyOmega
点击选项。

    ![](https://secure2.wostatic.cn/static/xyikS32VaPCK4PMLhhyNqY/image.png?auth_key=1681868014-6GKUk87iuVmGZC7YmzUSKJ-0-c605d7a56623723b4c0f2ec8679a772b)

    创建情景模式

    ![](https://secure2.wostatic.cn/static/cxCHQXrBFZXR2UhaTT2xoJ/image.png?auth_key=1681868014-nv9QP4uhzuNXBPC3nfirQw-0-37e4ff2c21cbbaf6e89100129b193431)

    输入如下内容并保存

    ![](https://secure2.wostatic.cn/static/v5SUR38zRNcs1w6KXqf1oH/image.png?auth_key=1681868014-igsXrNd4DKx9wTTY7Jv7d8-0-c6d959dbd2a1d89c90900810fcc31621)

## 运行m2m

- 双击启动m2m
失败场景1：

    ![](https://secure2.wostatic.cn/static/gYrCxEJ7mN4Ska4qns9eCS/1680238494062.jpg?auth_key=1681868014-dK4dsJsNuve7vKvGXFCmVf-0-09a39fb17091e98b88061bc41c7be70d)

    解决方法1：

    ![](https://secure2.wostatic.cn/static/9VyiGenYQz4SATZKDDwk4Z/image.png?auth_key=1681868014-szS752TjNrNMbiNzhgt3ev-0-1c99d9dfb47c56f4a24e8a048ab1e3a4)

    失败场景2：

    ![](https://secure2.wostatic.cn/static/7bFJfoTVEQLRcU7pb44BKR/image.png?auth_key=1681868014-uDvgABwJeH5WPGKabXvXV9-0-e4415bc153d2a97bc117f8ea833ae291)

    解决方法2：

    用chmod 777 文件名赋予文件可执行权限

    ![](https://secure2.wostatic.cn/static/feMUmp3kCycTa81L7tC99p/image.png?auth_key=1681868014-agR636wKJKibgjn5q4wo93-0-535b6a9c0955fd3c525157a491b69cab)

    到这个界面时代表监听已打开8083端口

- 启动后默认锁定graphql关键字，可以更改后点击update keywoeds按钮更新关键字

![](https://secure2.wostatic.cn/static/q9qNUwonu5TfvFANodxe71/image.png?auth_key=1681869105-ovJKyixHNTtCNbmi5SYNBz-0-788aeda1f410ff50aeda2ac0f3f4c56b)

- Update Keywoeds按钮
    - 点击后会根据输入框的文字更新监听关键字。
    - 点击后会删除json之前的所有内容，重新写入。
- Entry按钮
    - 未点击状态，只会监听当前过滤的接口并显示，并不会录入到mitm2mester.json文件中

    ![](https://secure2.wostatic.cn/static/u31Hp6RPk24C4r5aExxdj6/image.png?auth_key=1681869123-qngrSyLmZZxDdbXEYysjxL-0-5cf14e12d487834ef5e152e75373a540)

    - 点击Entry按钮后，按钮会变成蓝色，之后捕获的接口会存入mitm2meter.json文件中

    ![](https://secure2.wostatic.cn/static/hDseGqqAsxgirXifMMescq/image.png?auth_key=1681869133-2g8qVqkt3hRnhZWrKShP6M-0-01024884dab855680fea1af48b7ee494)

打开浏览器代理

![](https://secure2.wostatic.cn/static/fJYPVfQtpoYLQ59312juPM/image.png?auth_key=1681868014-nUVZFNEUijPxLCAKBDVcb2-0-d32ea05b84ea9ca5135e865c66393b2c)
## 安装证书（首次）

在开启了m2m以及浏览器代理之后，在输入框输入mitm.it

![](https://secure2.wostatic.cn/static/fZZpdF8GXYh7Uc6WUJGimj/image.png?auth_key=1681868015-baKcaQ4CYLku13HKWYFnd7-0-b9228fd5deb5b81c55e140add49766b7)

根据系统不同get不同的证书

-  windows证书安装



![](https://secure2.wostatic.cn/static/4nVnvKDVJKXzKBaLb8YPye/image.png?auth_key=1681868014-qV7ktwFBFH99VGat6uvsYJ-0-5fb4c6163d37fa9d230ab94e64919c61)

双击mitmproxy-ca.p12进入导入证书的页面，点击“下一步”

![](https://secure2.wostatic.cn/static/cDJvbXFDsS96jTAvcjt7sY/image.png?auth_key=1681868015-m4xU16hvdjTLvoapdLACws-0-c7a3cf222eecf62b9157dc24cbba011a)

不用输入密码，直接“下一步”

![](https://secure2.wostatic.cn/static/2UkjZEfmaf6XGNTc1VFzPh/image.png?auth_key=1681868015-hHz8a3DADGr8xX3ezv7aA5-0-9ac37482875d4a8f6d1fc012b4110461)

选择“将所有的证书都放入下列存储”，接着选择“受信任的根证书颁发机构”

![](https://secure2.wostatic.cn/static/6HpEQPEeEog1aYq9ux2E5S/image.png?auth_key=1681868015-943ZXrwBsRHVPzSMCAByL3-0-209cc81e7cc5a967bcdc2110a1f240fe)

最后，弹出警告窗口，直接点击“是”

![](https://secure2.wostatic.cn/static/sCeeji2z728zFfkogD15X7/image.png?auth_key=1681868015-9rzX9mqNsradHwmvw9yvTu-0-3f585f95c3d9252bbf799c21f02e1dd3)
- mac
Mac 下双击 mitmproxy-ca-cert.pem 即可弹出钥匙串管理页面，然后找到 mitmproxy 证书，点击打开其设置选项，选择始终信任即可

    ![](https://secure2.wostatic.cn/static/hi3Shkt1YA2D2ZafCowT1t/image.png?auth_key=1681868015-jWgnFiht7rgopoS8GznWDt-0-6e71474488f1784f773ffafaf19f2940)

## 捕获接口

- entry后为录入的接口

  ![img.png](img.png)
  m2m会在**桌面**实时生成json文件mitm2meter.json，该文件为持续覆盖状态，再次开启m2m会覆盖这个文件，若需要保存上次的录制，请将上次的mitm2meter.json文件转移至其他目录。



## 导入到Metersphere平台

> 接口测试→接口定义→更多操作→导入→格式选择Metersphere上传mitm2meter.json文件点击保存即可



