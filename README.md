
# DomainSeeker

快速翻墙，仅供学习使用。
注：严禁用于商业及任何违法用途。

# 使用方法

仅支持Linux/Windows/Mac

## Linux/Mac

1. cd DomainSeeker/data
2. make
3. cd ..
4. sudo ./start.sh 
5. 将DNS服务器改为 本机ip---可使用 ip addr查看
6. 重启网络服务和浏览器即可

* 更新hosts：sudo ./update.sh

## Windows

* 下载 DomainSeeker.zip，解压
* 下载地址：https://github.com/harrisonpan/DomainSeeker/releases/latest/
* 右键管理员身份运行 start.bat或update.bat(更新hosts)


# 局域网共享使用

若想让同局域网内所有设备使用DNS翻墙功能，请

* 修改文件config.json
 "local_dns_server" : "127.0.0.1",
 127.0.0.1 把此IP换成 电脑本地IP

* 同一局域网下，把手机DNS改为 运行程序的电脑本地IP即可

# 效果
![](http://www.codedev.cn/data/attachment/forum/201704/22/104649r8gr6gqwl4q7g683.png)


# 数据引用

  * https://raw.githubusercontent.com/vokins/yhosts/master/hosts
  * https://raw.githubusercontent.com/aoccin/adaway/master/hosts
  * https://github.com/racaljk/hosts


# 更多请参阅

  * http://www.codedev.cn/forum.php?mod=viewthread&tid=10
