import urllib3


http = urllib3.PoolManager(                                                        cert_reqs='CERT_REQUIRED', # Force certificate check.
    ca_certs='/etc/ssl/certs/ca-bundle.crt'
)

test = ['expired', 'wrong.host', 'self-signed', 'sha1-2016', 'sha1-2017', 'sha256', '1000-sans', '10000-sans', 'incomplete-chain', 'rsa8192', 'mozilla-old', 'mozilla-intermediate', 'mozilla-modern', 'dh480', 'dh1024', 'dh2048', 'dh-small-subgroup', 'dh-composite', 'superfish', 'edellroot', 'dsdtestprovider']


for t in test:
    try:
        r = http.request('GET', "https://%s.badssl.com" % t)
    except Exception as e:
        print "%s failed" % t, e
    else:
        print "%s pass" % t


    