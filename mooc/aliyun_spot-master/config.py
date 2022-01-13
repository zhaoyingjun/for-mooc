# coding=utf-8

access_id = ''
access_secret = ''
# 本地的 ssh key，对应的是 key_pair_name in aliyun console
ssh_key_file = "~/.ssh/aiwulan.pem"
# 密钥对名称(需要在 aliyun console 上创建)
key_pair_name = 'aiwulan'


# 下面的配置可以保持默认

# 实例所属的地域ID
region_id = 'cn-wulanchabu'
# 网络计费类型
internet_charge_type = 'PayByTraffic'
# 指定创建ECS实例的数量
amount = 1
# 指定ECS实例最小购买数量：当ECS库存数量小于最小购买数量，会创建失败；当ECS库存数量大于等于最小购买数量，按照库存数量创建
minamount = 1
# 公网出带宽最大值
internet_max_bandwidth_out = 10
# 后付费实例的抢占策略
spot_strategy = 'SpotWithPriceLimit'
# 设置实例的每小时最高价格
spot_price_limit = 3
# 系统盘大小
system_disk_size = '40'
# 系统盘的磁盘种类
system_disk_category = 'cloud_efficiency'
# 释放时间 hours
auto_release_hour = 1
# 实例类型(cpu/mem/disk) 详细可以查看 https://help.aliyun.com/document_detail/25378.html
instance_type = 'ecs.gn6i-c4g1.xlarge'
