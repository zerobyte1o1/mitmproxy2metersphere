- 启动后默认锁定graphql关键字，可以更改后点击update keywoeds按钮更新关键字

[图片]

- Update Keywoeds按钮
    - 点击后会根据输入框的文字更新监听关键字。
    - 点击后会删除json之前的所有内容，重新写入。
- Entry按钮
    - 未点击状态，只会监听当前过滤的接口并显示，并不会录入到mitm2mester.json文件中

[图片]
  - 点击Entry按钮后，按钮会变成蓝色，之后捕获的接口会存入mitm2meter.json文件中

[图片]

- 启动后默认锁定graphql关键字，可以更改后点击update keywoeds按钮更新关键字

[图片]

- Update Keywoeds按钮
    - 点击后会根据输入框的文字更新监听关键字。
    - 点击后会删除json之前的所有内容，重新写入。
- Entry按钮
    - 未点击状态，只会监听当前过滤的接口并显示，并不会录入到mitm2mester.json文件中

[图片]
  - 点击Entry按钮后，按钮会变成蓝色，之后捕获的接口会存入mitm2meter.json文件中

[图片]

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



![](https://secure2.wostatic.cn/static/tLRhYwzMFXid2Gb6imL6MY/image.png?auth_key=1681457350-6NBJzZ4pUMJc4Env5LGE2U-0-e89e9afb0d61f6fecc73a4667f21e605)

## 安装并配置SwitchyOmega

- 安装SwitchyOmega
以chrome为例：打开扩展模式后，下载[https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN)

    ![](https://secure2.wostatic.cn/static/9YKV5ySjAcXUh81bzBygDR/image.png?auth_key=1681457350-9Q3hERwf2x5nWUaP9Nt5g7-0-40335fdd7443931e46ecce819e7cb18d)
- 配置SwitchyOmega
点击选项。

    ![](https://secure2.wostatic.cn/static/xyikS32VaPCK4PMLhhyNqY/image.png?auth_key=1681457350-upYTzGVLYEQvY5f9817DVa-0-c1fa2ff66ef29f56f57c3cfd76a6ad33)

    创建情景模式

    ![](https://secure2.wostatic.cn/static/cxCHQXrBFZXR2UhaTT2xoJ/image.png?auth_key=1681457350-mWvkjk4MP6QAQedZLgsALw-0-a06441cd9bc703baf51dad13d7b22698)

    输入如下内容并保存

    ![](https://secure2.wostatic.cn/static/v5SUR38zRNcs1w6KXqf1oH/image.png?auth_key=1681457350-qPbn7NHrCwEfyz7oWL41bG-0-3ccfae573915305fb3fce66324a3c33d)

## 运行m2m

- 双击启动m2m
失败场景1：

    ![](https://secure2.wostatic.cn/static/gYrCxEJ7mN4Ska4qns9eCS/1680238494062.jpg?auth_key=1681457350-ic1hEJxbzk9PjVDKVq8xU2-0-0f9036b5d6281a6fa21b0fc322f1bcfe)

    解决方法1：

    ![](https://secure2.wostatic.cn/static/9VyiGenYQz4SATZKDDwk4Z/image.png?auth_key=1681457350-fweiG5Nn8u43BN4wAtj3bZ-0-be48123c4d675aeabc536cdb865fabfa)

    失败场景2：

    ![](https://secure2.wostatic.cn/static/7bFJfoTVEQLRcU7pb44BKR/image.png?auth_key=1681457350-rx4qHkva3uxC89AbW5za8S-0-ca2d707a4bb6e3bc0dd53ccc8140c5dc)

    解决方法2：

    用chmod 777 文件名赋予文件可执行权限

    ![](https://secure2.wostatic.cn/static/feMUmp3kCycTa81L7tC99p/image.png?auth_key=1681457350-5pGGWrqmPU2S7iaSSE6RWw-0-283dde6cb8488c8bbb28b766bef4c426)

    到这个界面时代表监听已打开8083端口

    - 启动后默认锁定graphql关键字，可以更改后点击update keywoeds按钮更新关键字

    ![](https://teletraan.feishu.cn/space/api/box/stream/download/asynccode/?code=NWYwYjY2ZmRhMWRhYjdmMWJjN2Y1YWU2YzU2MTdmYzZfM29vUEpvR2lHcE9IRWpGVmRXY0FBOGprcEl4bnBWV3hfVG9rZW46QTFqRmJRMTBCb1l3MEN4YVZDR2NoUlhqbk1oXzE2ODE0NTczODQ6MTY4MTQ2MDk4NF9WNA)

    - Update Keywoeds按钮
        - 点击后会根据输入框的文字更新监听关键字。
        - 点击后会删除json之前的所有内容，重新写入。
    - Entry按钮
        - 未点击状态，只会监听当前过滤的接口并显示，并不会录入到mitm2mester.json文件中

        ![](https://teletraan.feishu.cn/space/api/box/stream/download/asynccode/?code=MDZlZTg1YzIzMzM1ZTE2MjJhMzEzYzQzMjlmYmNjODhfZUQ4bUNoRlFUUkR0RUVNYTIzekVEMGo2UlpMczg5V0lfVG9rZW46UFRNYWJkT0pZb0o0Vmh4a3d3S2NHWk9vblBoXzE2ODE0NTczODQ6MTY4MTQ2MDk4NF9WNA)

        - 点击Entry按钮后，按钮会变成蓝色，之后捕获的接口会存入mitm2meter.json文件中

        ![](https://teletraan.feishu.cn/space/api/box/stream/download/asynccode/?code=YmMxYTUyNjRmZDE2NmY0OGE2M2IxZGVkZmViM2NkOTVfSnZmbXpVTG5udWFGWFFWRTBXZGhiUlBSc0ZEalRUYmRfVG9rZW46TjN0eGJFeTA0b2ZvQld4ZWtSY2NkdGt6bjdnXzE2ODE0NTczODQ6MTY4MTQ2MDk4NF9WNA)

    打开浏览器代理

    ![](https://secure2.wostatic.cn/static/fJYPVfQtpoYLQ59312juPM/image.png?auth_key=1681457350-kfsQ5MuTFp4JUCrxTdYaiM-0-e4f39087f3f5fdd73da25a725a9178fe)

## 安装证书（首次）

在开启了m2m以及浏览器代理之后，在输入框输入mitm.it

![](https://secure2.wostatic.cn/static/fZZpdF8GXYh7Uc6WUJGimj/image.png?auth_key=1681457350-9cj2ncG9gzfRcg6wJvme1C-0-d222d53e5724b3bdb541c07269d683ef)

根据系统不同get不同的证书

-  windows证书安装



    ![](https://secure2.wostatic.cn/static/4nVnvKDVJKXzKBaLb8YPye/image.png?auth_key=1681457350-ePAGF1qR1KHvqdaGBJDbo5-0-ca94fd2f722122a9d7f8287b9aac8ba9)

    双击mitmproxy-ca.p12进入导入证书的页面，点击“下一步”

    ![](https://secure2.wostatic.cn/static/cDJvbXFDsS96jTAvcjt7sY/image.png?auth_key=1681457350-j6LxdmFsc3rMU6mJNbqvKY-0-19dc7a2838a9de9c80fb9f085e0b60fe)

    不用输入密码，直接“下一步”

    ![](https://secure2.wostatic.cn/static/2UkjZEfmaf6XGNTc1VFzPh/image.png?auth_key=1681457350-bcRLqF5cVFAq72GQLGopuv-0-11629c99dc18f6b3810475734fc66a9c)

    选择“将所有的证书都放入下列存储”，接着选择“受信任的根证书颁发机构”

    ![](https://secure2.wostatic.cn/static/6HpEQPEeEog1aYq9ux2E5S/image.png?auth_key=1681457350-azoDSUksDQfsFwGAoQDQcD-0-c01151f6cc7e28ee6599329bfb3f1545)

    最后，弹出警告窗口，直接点击“是”

    ![](https://secure2.wostatic.cn/static/sCeeji2z728zFfkogD15X7/image.png?auth_key=1681457350-uyXr2GGUpcAZPXv8Ev7Fc6-0-154ecba3c7f3a9500c2765789ae1f001)
- mac
Mac 下双击 mitmproxy-ca-cert.pem 即可弹出钥匙串管理页面，然后找到 mitmproxy 证书，点击打开其设置选项，选择始终信任即可

    ![](https://secure2.wostatic.cn/static/hi3Shkt1YA2D2ZafCowT1t/image.png?auth_key=1681457350-sVbc45tBen1Ndh8TJPQk3Q-0-c13bf4c84f6aba432fb36f05f3c06ae5)

## 捕获接口

- 
entry后为录入的接口

    ![](https://secure2.wostatic.cn/static/hpqJi44rswFpJXZhDmY1LL/image.png?auth_key=1681457350-8v43zqWLMdRVhhJeRDT4SW-0-21992af18bd6b140e79f4c1ca4f654c8)

    m2m会在同目录实时生成json文件mitm2meter.json，该文件为持续覆盖状态，再次开启m2m会覆盖这个文件，若需要保存上次的录制，请将上次的mitm2meter.json文件转移至其他目录。



## 导入到Metersphere平台

> 接口测试→接口定义→更多操作→导入→格式选择Metersphere上传mitm2meter.json文件点击保存即可



