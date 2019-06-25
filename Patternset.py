class Patternset():

    def __init__(self):
        # do not change varible name
        self.keywordpattern = {}
        self.pathpattern = {}

        # Choose pattern set into our IoT Device Testls case

        self.add_PathKeywordPattern()
        self.add_SensitiveKeywordPattern()
        self.add_DomainKeywordPattern()
        self.add_ProtocolKeywordPattern()
        self.add_WebServerKeywordPattern()

    def add_PathKeywordPattern(self):
        # Sensitive file name
        self.pathpattern['passwd'] = '/etc/passwd'
        self.pathpattern['shadow'] = '/etc/shadow'
        self.pathpattern['password'] = 'password'
        # Certificate file extension
        self.pathpattern['pem'] = '\.pem'
        self.pathpattern['psk'] = '\.psk'
        self.pathpattern['key'] = '\.key'
        # Database file extension
        self.pathpattern['db'] = '\.db'
        self.pathpattern['sqlite'] = '\.sqlite'
        self.pathpattern['sqlite3'] = '\.sqlite3'
        # ssh key
        self.pathpattern['known_hosts'] = 'known_hosts'
        self.pathpattern['id_rsa'] = 'id_rsa'
        self.pathpattern['id_rsapub'] = 'id_rsa\.pub'


    def add_SensitiveKeywordPattern(self):
        # Password keyword
        self.keywordpattern['passwd'] = 'passwd=.*'
        self.keywordpattern['password'] = 'password=.*'
        self.keywordpattern['privatekey'] = 'PRIVATE KEY'
        # oauth
        # self.keywordpattern['oauth'] = 'oauth=.*'
        # self.keywordpattern['client_id'] = 'client_id'
        # self.keywordpattern['clientid_ad'] = 'client_id=.*'

    def add_DomainKeywordPattern(self):
        # Email Account
        self.keywordpattern['email'] = '[A-Za-z0-9]{1}[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
        # IPv4 address
        self.keywordpattern['ipv4'] = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        # IPv6 address
        self.keywordpattern['ipv6'] = '(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,6}\Z)|(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,5}\Z)|(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,4}\Z)|(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,3}\Z)|(\A([0-9a-f]{1,4}:){1,5}(:[0-9a-f]{1,4}){1,2}\Z)|(\A([0-9a-f]{1,4}:){1,6}(:[0-9a-f]{1,4}){1,1}\Z)|(\A(([0-9a-f]{1,4}:){1,7}|:):\Z)|(\A:(:[0-9a-f]{1,4}){1,7}\Z)|(\A((([0-9a-f]{1,4}:){6})(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|(\A(([0-9a-f]{1,4}:){5}[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|(\A([0-9a-f]{1,4}:){5}:[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,4}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,3}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,2}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,1}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A(([0-9a-f]{1,4}:){1,5}|:):(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A:(:[0-9a-f]{1,4}){1,5}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)'
        # self.keywordpattern['ipv6'] = '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'


    def add_ProtocolKeywordPattern(self):
        # Connection key word ,can upload/download file form internet
        self.keywordpattern['scp'] = 'scp'
        self.keywordpattern['telnet'] = 'telnet'
        self.keywordpattern['ssh'] = 'ssh'
        self.keywordpattern['ftp'] = 'ftp'
        self.keywordpattern['curl'] = 'curl'
        self.keywordpattern['wget'] = 'wget'

    def add_WebServerKeywordPattern(self):
        # Commom Web Server Name
        self.keywordpattern['apache'] = 'apache'
        self.keywordpattern['lighttpd'] = 'lighttpd'
        self.keywordpattern['alphapd'] = 'alphapd'
        self.keywordpattern['httpd'] = 'httpd'
        self.keywordpattern['nginx'] = 'nginx'