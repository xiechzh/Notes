import time

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#**************************************************************************************************************
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

#**************************** JAXSTA ****************************
#****************************************************************

data-jumphost.jaxsta.io  // NOT USING ANYMORE


#****************************************************************
#****************************************************************

# ===== 取出空格 =====
title = ' love u  '
title = title.strip()

# 滚动广告字幕
content = '钻石永久远，一颗永流传!'
while True:
    print('\r', content, end='', flush=True)  # 去掉flush参数效果也一样
    content = content[1:] + content[0]
    time.sleep(0.5)


# 链接 ssh data-tunnel
$ cd .ssh
$ .ssh data-tunnel


# connect to database
def conenct_tunnel():
    tunnel = SSHTunnelForwarder(
        ("data-access.jaxsta.io", 22),
        ssh_username="ec2-user",
        ssh_private_key="/Users/ryanjadidi/jaxsta/credentials/jaxsta-vault/Keypairs/downey.pem",
        remote_bind_address=("fenderreadreplica.cmtoqsralyh5.eu-west-1.rds.amazonaws.com", 5432),
        local_bind_address=("localhost", 5434),  # could be any available port
    )

    tunnel.start()

    conn = psycopg2.connect(
        database="jaxsta_data",
        user="sophie_xie",
        password="m33rkat",
        host=tunnel.local_bind_host,
        port=tunnel.local_bind_port,
    )

    return