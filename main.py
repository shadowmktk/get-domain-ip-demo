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
