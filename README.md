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



![](https://secure2.wostatic.cn/static/tLRhYwzMFXid2Gb6imL6MY/image.png?auth_key=1680252012-sZfqeg3erCgbsm2n6SEKn9-0-5bf54fff4d7418f1fab99555a5c6309e)

## 安装并配置SwitchyOmega

- 安装SwitchyOmega
以chrome为例：打开扩展模式后，下载[https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN)

    ![](https://secure2.wostatic.cn/static/9YKV5ySjAcXUh81bzBygDR/image.png?auth_key=1680252012-4LHy3t2W9VCqAVZer3BMxB-0-4b4165285f7a5b42b37072a3ef30ca66)
- 配置SwitchyOmega
点击选项。

    ![](https://secure2.wostatic.cn/static/xyikS32VaPCK4PMLhhyNqY/image.png?auth_key=1680252012-3ropEgH1LsaGKNobaUf8vG-0-f80426de4301d1f664a7c66b4db9bf7c)

    创建情景模式

    ![](https://secure2.wostatic.cn/static/cxCHQXrBFZXR2UhaTT2xoJ/image.png?auth_key=1680252012-tDfZ6eQ879L1dN7fhfpGEn-0-fa55efe4c89508a0a0a08deb82481166)

    输入如下内容并保存

    ![](https://secure2.wostatic.cn/static/v5SUR38zRNcs1w6KXqf1oH/image.png?auth_key=1680252012-4TU341agraae8TLQyvfduY-0-825305d8219088514bb3e7835b3057b9)

## 运行m2m

- 双击启动m2m
失败场景1：

    ![](https://secure2.wostatic.cn/static/gYrCxEJ7mN4Ska4qns9eCS/1680238494062.jpg?auth_key=1680252012-wCo9gbsn5DS2EyrGc4zyLy-0-9f467cd5e6877bb86b72c63d849abdcf)

    解决方法1：

    ![](https://secure2.wostatic.cn/static/9VyiGenYQz4SATZKDDwk4Z/image.png?auth_key=1680252012-gdkS3oqxLsEz5mY9EWmH3s-0-9424e3ed564baf47781cb7e8b502f9b9)

    失败场景2：

    ![](https://secure2.wostatic.cn/static/7bFJfoTVEQLRcU7pb44BKR/image.png?auth_key=1680252012-xrjaD7VdiL4Cc3PWVuVVEK-0-b2906321c47efcda0b0530f30b71698a)

    解决方法2：

    用chmod 777 文件名赋予文件可执行权限

    ![](https://secure2.wostatic.cn/static/feMUmp3kCycTa81L7tC99p/image.png?auth_key=1680252012-kGywS9vSTjQY2KA4gcGLnd-0-7323070103bffa3df4d542b65286478b)

    启动后输入想要过滤的url内容，回车



    ![](https://secure2.wostatic.cn/static/ngTGbTyr9a76KRy4NEZ2wu/image.png?auth_key=1680252012-6dJU66vCEBCuQiZVExZL3u-0-ae51e24963cfe23052acd3aeec06a313)

    ![](https://secure2.wostatic.cn/static/pzykDfCo8eU7oAc4by3p5E/image.png?auth_key=1680252012-eXwKLYhQrnQWSmNnHGsfXa-0-6035c973e08c93a8168e0767e8fa681c)

    到这个界面时代表监听已打开8083端口

    打开浏览器代理

    ![](https://secure2.wostatic.cn/static/fJYPVfQtpoYLQ59312juPM/image.png?auth_key=1680252012-nrnZCR1WBS2BF8Jsitz2LS-0-138906f6d54a737f3ad5b07dbdc7e086)

## 安装证书（首次）

在开启了m2m以及浏览器代理之后，在输入框输入mitm.it

![](https://secure2.wostatic.cn/static/fZZpdF8GXYh7Uc6WUJGimj/image.png?auth_key=1680252013-2bDAaY9k9P6oZA56eQfc5d-0-892b5f85263c85f5c18abcf786b8fe0b)

根据系统不同get不同的证书

-  windows证书安装



    ![](https://secure2.wostatic.cn/static/4nVnvKDVJKXzKBaLb8YPye/image.png?auth_key=1680252013-8TpdQmM1gvDDRvkF2GEnNq-0-dfad4ef1c1b5d9ddb088847e720ee91b)

    双击mitmproxy-ca.p12进入导入证书的页面，点击“下一步”

    ![](https://secure2.wostatic.cn/static/cDJvbXFDsS96jTAvcjt7sY/image.png?auth_key=1680252013-qSNVnUBTTQXwo1b8RM46g-0-1da3a3e02399109f9af71c7f416af89a)

    不用输入密码，直接“下一步”

    ![](https://secure2.wostatic.cn/static/2UkjZEfmaf6XGNTc1VFzPh/image.png?auth_key=1680252013-6wzkWrPrCguBZYTv2794v6-0-90e8d0c2b2efc20700d371a12a40de51)

    选择“将所有的证书都放入下列存储”，接着选择“受信任的根证书颁发机构”

    ![](https://secure2.wostatic.cn/static/6HpEQPEeEog1aYq9ux2E5S/image.png?auth_key=1680252013-2Twh7cYLhFSKaq21d88Csd-0-4068672a445c96f061b1a596a14ed38d)

    最后，弹出警告窗口，直接点击“是”

    ![](https://secure2.wostatic.cn/static/sCeeji2z728zFfkogD15X7/image.png?auth_key=1680252013-pLrgeqt7QtZABfxv82eQ3W-0-0cfa71b8449fe9f2c7b8e4b070725775)
- mac
Mac 下双击 mitmproxy-ca-cert.pem 即可弹出钥匙串管理页面，然后找到 mitmproxy 证书，点击打开其设置选项，选择始终信任即可

    ![](https://secure2.wostatic.cn/static/hi3Shkt1YA2D2ZafCowT1t/image.png?auth_key=1680252013-rim4P7WRFQ341iHiTTJBkj-0-63655f339b909194e0cc3ea7ad4ed76d)

## 捕获接口

- 
entry后为录入的接口

    ![](https://secure2.wostatic.cn/static/hpqJi44rswFpJXZhDmY1LL/image.png?auth_key=1680252363-aMDqcyxw1j6rwE43EVEsnq-0-dc405def5e8ce827c88e46f017c8cf0d)

    m2m会在同目录实时生成json文件mitm2meter.json，该文件为持续覆盖状态，再次开启m2m会覆盖这个文件，若需要保存上次的录制，请将上次的mitm2meter.json文件转移至其他目录。



## 导入到Metersphere平台

> 接口测试→接口定义→更多操作→导入→格式选择Metersphere上传mitm2meter.json文件点击保存即可

，