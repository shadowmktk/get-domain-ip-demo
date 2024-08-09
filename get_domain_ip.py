import dns.resolver

def GetDomainIP(domain: str, rdtype: str='A', nameservers='127.0.0.1'):
    myResolver = dns.resolver.Resolver()

    if nameservers != '127.0.0.1':
        myResolver.nameservers = nameservers

    query_object = myResolver.resolve(qname=domain, rdtype=rdtype)

    return query_object
