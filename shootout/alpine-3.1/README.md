# TryTLS testing with Alpine Edge

```console
# cat /etc/alpine-release
3.1.4
```

<!-- markdownlint-disable MD013 -->

python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https    | java-net      | php-file-get-contents
---------------- | --------------- | -------------- | ---------- | ------------- | ------------- | ---------------------
FAIL(MD5)        | FAIL(MD5)       | N/A            | PASS       | PASS w/NO SNI | PASS w/NO SNI | PASS w/NO SNI

## python2-requests

```console
# python --version
Python 2.7.12
```

```console
# trytls https python run.py
platform: Linux
runner: trytls 0.3.4 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: python run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for domain-match.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for wildcard-match.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for dh1024.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for domain-mismatch.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for wildcard.mismatch.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for weak-sig.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:38364]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS invalid localhost certificate [reject localhost:45282]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python2-urllib2

```console
# python --version
Python 2.7.12
```

```console
# trytls https python run.py
platform: Linux
runner: trytls 0.3.4 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: python run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 PASS denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:37353]
 PASS invalid localhost certificate [reject localhost:34921]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python3-urllib

```console
# python3 --version
loop: eval: line 1: python3: not found
```

```console
# trytls https python3 run.py
platform: Linux
runner: trytls 0.3.4 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: python3 run.py
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: failed to launch the stub
      output: No such file or directory
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: failed to launch the stub
      output: No such file or directory
ERROR protect against the Logjam attack [reject www.ssllabs.com:10445]
      reason: failed to launch the stub
      output: No such file or directory
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: failed to launch the stub
      output: No such file or directory
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: failed to launch the stub
      output: No such file or directory
ERROR protection against POODLE attack [reject sslv3.dshield.org:443]
      reason: failed to launch the stub
      output: No such file or directory
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: failed to launch the stub
      output: No such file or directory
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
ERROR support for TLS server name indication (SNI) [accept tlsfun.de:443]
      reason: failed to launch the stub
      output: No such file or directory
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
ERROR valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: failed to launch the stub
      output: No such file or directory
ERROR valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: failed to launch the stub
      output: No such file or directory
ERROR support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: failed to launch the stub
      output: No such file or directory
ERROR TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: failed to launch the stub
      output: No such file or directory
ERROR certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: failed to launch the stub
      output: No such file or directory
ERROR certificate validity starts in future [reject future.badtls.io:11001]
      reason: failed to launch the stub
      output: No such file or directory
ERROR mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: failed to launch the stub
      output: No such file or directory
ERROR Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: failed to launch the stub
      output: No such file or directory
ERROR certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: failed to launch the stub
      output: No such file or directory
ERROR expired certificate [reject expired.badtls.io:11006]
      reason: failed to launch the stub
      output: No such file or directory
ERROR invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: failed to launch the stub
      output: No such file or directory
ERROR denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
      reason: failed to launch the stub
      output: No such file or directory
ERROR denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
      reason: failed to launch the stub
      output: No such file or directory
ERROR denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: failed to launch the stub
      output: No such file or directory
ERROR valid localhost certificate [accept localhost:46695]
      reason: failed to launch the stub
      output: No such file or directory
ERROR invalid localhost certificate [reject localhost:39064]
      reason: failed to launch the stub
      output: No such file or directory
ERROR use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: failed to launch the stub
      output: No such file or directory
```

## go-nethttp

```console
# go version
go version go1.3.3 linux/amd64
```

```console
# trytls https go run run.go
platform: Linux
runner: trytls 0.3.4 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: go run run.go
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: Get https://www.ssllabs.com:10443: crypto/rsa: verification error
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: Get https://www.ssllabs.com:10444: tls: unexpected ServerKeyExchange
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: Get https://www.ssllabs.com:10445: remote error: handshake failure
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: Get https://cve.freakattack.com:443: tls: unexpected ServerKeyExchange
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: Get https://cve2.freakattack.com:443: tls: unexpected ServerKeyExchange
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: Get https://sslv3.dshield.org:443: tls: server selected unsupported protocol version 300
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: Get https://self-signed.badssl.com:443: x509: certificate signed by unknown authority
 PASS expired certificate [reject expired.badssl.com:443]
      output: Get https://expired.badssl.com:443: x509: certificate has expired or is not yet valid
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: Get https://wrong.host.badssl.com:443: x509: certificate is valid for *.badssl.com, badssl.com, not wrong.host.badssl.com
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: Get https://incomplete-chain.badssl.com:443: x509: certificate signed by unknown authority
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: Get https://superfish.badssl.com:443: x509: certificate signed by unknown authority
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: Get https://edellroot.badssl.com:443: x509: certificate signed by unknown authority
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: Get https://dsdtestprovider.badssl.com:443: x509: certificate signed by unknown authority
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      output: Get https://self-signed.badssl.com:443: x509: certificate signed by unknown authority
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      output: Get https://badcert-edell.tlsfun.de:443: x509: certificate signed by unknown authority
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:36661]
 SKIP invalid localhost certificate [reject localhost:42844]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

```console
# java -version
java version "1.7.0_75"
OpenJDK Runtime Environment (IcedTea 2.5.4) (Alpine 7.75.2.5.4-r0)
OpenJDK 64-Bit Server VM (build 24.75-b04, mixed mode)
```

```console
# trytls https java Run
platform: Linux
runner: trytls 0.3.4 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: java Run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
 FAIL support for TLS server name indication (SNI) [accept tlsfun.de:443]
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:40652]
 SKIP invalid localhost certificate [reject localhost:42013]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-net

```console
# java -version
java version "1.7.0_75"
OpenJDK Runtime Environment (IcedTea 2.5.4) (Alpine 7.75.2.5.4-r0)
OpenJDK 64-Bit Server VM (build 24.75-b04, mixed mode)
```

```console
# trytls https java Run
platform: Linux
runner: trytls 0.3.4 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: java Run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
 FAIL support for TLS server name indication (SNI) [accept tlsfun.de:443]
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:44143]
 SKIP invalid localhost certificate [reject localhost:39491]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## php-file-get-contents

```console
# php --version
PHP 5.6.24 (cli) (built: Jul 27 2016 07:30:07)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
```

```console
# trytls https php run.php
platform: Linux
runner: trytls 0.3.4 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: php run.php
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
 FAIL support for TLS server name indication (SNI) [accept tlsfun.de:443]
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:39053]
 SKIP invalid localhost certificate [reject localhost:40473]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```
