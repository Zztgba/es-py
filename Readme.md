## 环境搭建文档

### Java环境配置

选择一个目录，下载java包(此处以jdk1.8为例)

下载项目中的jdk-8u241-linux-x64.tar.gz
```shell script
##安装
root@riak:/home/riak# cd /home/java  (安装路径)
root@riak:/home/riak# tar -zxvf jdk-8u201-linux-x64.tar.gz
##解压后目录下会多个jdk1.8.0_241文件夹

##配置环境
root@riak:/home/riak# vi /etc/profile
##底部加上以下内容
JAVA_HOME=/home/java/jdk1.8.0_241
PATH=$JAVA_HOME/bin:$PATH
CLASSPATH=.:$JAVA_HOME/lib/dt,jar:$JAVA_HOME/lib/tools.jar
export JAVA_HOME PATH CLASSPATH

##配置生效
root@riak:/home/riak# source /etc/profile

##测试环境安装
root@riak:/home/riak# java -version
java version "1.8.0_241"
Java(TM) SE Runtime Environment (build 1.8.0_241-b07)
Java HotSpot(TM) 64-Bit Server VM (build 25.241-b07, mixed mode)
```

### ES安装部署


```shell script
## 安装
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.3.zip
$ unzip elasticsearch-6.2.3.zip
$ cd elasticsearch-6.2.3/ 

## 启动
$ ./bin/elasticsearch

## 测试
$ curl localhost:9200
{
  "name" : "VTj9r4r",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "6RJcY3-oRcmijFShCXC7dQ",
  "version" : {
    "number" : "6.2.3",
    "build_hash" : "c59ff00",
    "build_date" : "2018-03-13T10:06:29.741383Z",
    "build_snapshot" : false,
    "lucene_version" : "7.2.1",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

#### ES常用配置

config/elasticsearch.yml

```
cluster.name: elasticsearch 
# 集群名称

node.name: "192.168.111.129"
# 当前机器的节点名

node.master: true
# 标识是否有资格为主节点 (true/false)

node.data: true
# 是否存储索引数据 (true/false)

index.number_of_shards: 5 
# 设置默认索引分片个数，默认为5片。7.X版本以上配置无效

index.number_of_replicas: 1
# 设置默认索引副本个数，默认为1个副本。7.x版本以上配置无效

network.bind_host: 192.168.0.1
# 设置绑定的ip地址，可以是ipv4或ipv6的，默认为0.0.0.0，绑定这台机器的任何一个ip。
 
network.publish_host: 192.168.0.1
# 设置其它节点和该节点交互的ip地址，如果不设置它会自动判断，值必须是个真实的ip地址。
 
network.host: 192.168.0.1
# 这个参数是用来同时设置bind_host和publish_host上面两个参数。
 
transport.tcp.port: 9300
# 设置节点之间交互的tcp端口，默认是9300。
 
transport.tcp.compress: true
# 设置是否压缩tcp传输时的数据，默认为false，不压缩。
 
http.port: 9200
# 设置对外服务的http端口，默认为9200。
 
http.max_content_length: 100mb
# 设置内容的最大容量，默认100mb

discovery.zen.ping.unicast.hosts: ["host1", "host2:port", "host3[portX-portY]"]
# 设置集群中master节点的初始列表，可以通过这些节点来自动发现新加入集群的节点。7.x版本无效
```

### Kibana安装部署

```shell script
##安装kibana
root@riak:/home/riak# wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.3-linux-x86_64.tar.gz
root@riak:/home/riak# tar -zxvf kibana-6.2.3-linux-x86_64.tar.gz
root@riak:/home/riak# cd kibana-6.2.3-linux-x86_64/

##设置kibana
root@riak:/home/riak# vim config/kibana.yml

server.port: 设置端口号,默认5601
server.host: ip
elasticsearch.hosts: ["http://192.168.111.129:9200", "localhost:9200", ...]
elasticsearch.username: ""
elasticsearch.password: ""
```

