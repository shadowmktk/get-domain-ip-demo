# get-domain-ip-demo
Install requirements.
```
pip3 install dnspython
```

Get domain ip.
```
python3 main.py
```

Example.
```
ubuntu@ADMIN:~/get-domain-ip-demo$ cat main.py
import json
from get_domain_ip import GetDomainIP

def main():
    domain = 'www.taobao.com'

    result = GetDomainIP(domain)
    ip_list = json.dumps({'domain': domain, 'ip_list': [str(x) for x in result.rrset]})
    print(ip_list)

    ###
    domain_list = ['www.baidu.com', 'www.aliyun.com', 'www.tencent.com', 'www.qq.com', 'www.google.com']
    nameservers = ['223.5.5.5', '119.29.29.29']
    rdtype = 'A'

    for domain in domain_list:
        result = GetDomainIP(domain, rdtype, nameservers)
        ip_list = json.dumps({'domain': domain, 'ip_list': [str(x) for x in result.rrset]})
        print(ip_list)

if __name__ == '__main__':
    main()
ubuntu@ADMIN:~/get-domain-ip-demo$

ubuntu@ADMIN:~/get-domain-ip-demo$ python3 main.py
{"domain": "www.taobao.com", "ip_list": ["163.177.180.108", "163.177.180.107"]}
{"domain": "www.baidu.com", "ip_list": ["157.148.69.80", "157.148.69.74"]}
{"domain": "www.aliyun.com", "ip_list": ["110.52.116.148", "121.31.230.204", "116.162.103.107"]}
{"domain": "www.tencent.com", "ip_list": ["211.91.65.218", "211.91.65.122"]}
{"domain": "www.qq.com", "ip_list": ["61.241.54.211", "61.241.54.232"]}
{"domain": "www.google.com", "ip_list": ["157.240.17.35"]}
ubuntu@ADMIN:~/get-domain-ip-demo$
```
