import string
import random
from cStringIO import StringIO

class randomHttp(object):
    def __init__(self):
        self.protocol = 'HTTP'
        self.space = ' '
        self.slash = '/'
        self.period = '.'
        self.colon_space = ': '
        self.crlf = "\r\n"
        self.methods= ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT']
        self.request_headers = ['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 
                                'Accept-Datetime', 'Authorization', 'Cache-Control', 'Connection', 
                                'Cookie', 'Content-Length', 'Content-MD5', 'Content-Type', 'Date', 
                                'Expect', 'From', 'Host', 'Permanent', 'If-Match', 'If-Modified-Since',
                                'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 
                                'Origin', 'Pragma', 'Proxy-Authorization', 'Range', 'Referer', 'TE', 
                                'User-Agent', 'Via', 'Warning', 'X-Requested-With', 'DNT', 
                                'X-Forwarded-For', 'X-Forwarded-Proto', 'Front-End-Https',
                                'X-ATT-DeviceId', 'X-Wap-Profile', 'Proxy-Connection']
        self.status_codes =     {100: 'Continue', 101: 'Switching Protocols', 102: 'Processing',
                                200: 'OK', 201: 'Created', 202: 'Accepted', 
                                203: 'Non-Authoritative Information', 204: 'No Content',
                                205:'Reset Content', 206:'Partial Content', 207: 'Multi-Status', 
                                208: 'Already Reported', 226: 'IM Used', 300: 'Multiple Choices',
                                301: 'Moved Permanently', 302: 'Found', 303: 'See Other', 
                                304: 'Not Modified', 305: 'Use Proxy', 306:'Switch Proxy', 
                                307:'Temporary Redirect', 308:'Permanent Redirect', 400:'Bad Request', 
                                401:'Unauthorized', 402:'Payment Required', 403:'Forbidden', 
                                404: 'Not Found', 405:'Method Not Allowed', 406:'Not Acceptable', 
                                407:'Proxy Authentication Required', 408:'Request Timeout', 
                                409:'Concflit', 410:'Gone', 411:'Length Required', 
                                412:'Precondition Failed', 413:'Request Entity Too Large', 
                                414:'Request-URI Too Long', 415:'Unsupported Media Type', 
                                416:'Requested Range Not Satisfiable', 417:'Expectation Failed', 
                                418:'I\'m a teapot', 419:'Authentication Timeout', 
                                420:'Enhance Your Calm', 422:'Unprocessable Entity', 423:'Locked', 
                                424:'Failed Dependency', 425:'Unordered Collection', 
                                426:'Upgrade Required', 428:'Precondition Required', 
                                429:'Too Many Requests', 431: 'Request Header Fields Too Large',
                                440: 'Login Timeout', 444: 'No Response', 449: 'Retry With', 
                                450: 'Blocked by Windows Parental Controls', 
                                451: 'Unavailable For Legal Reasons', 451: 'Redirect', 
                                494: 'Request Header Too Large', 495: 'Cert Error', 496: 'No Cert',
                                497: 'HTTP to HTTPS', 499: 'Client Closed Request', 
                                500: 'Internal Server Error', 501: 'Not Implemented', 
                                502: 'Bad Gateway', 503: 'Service Unavailable', 504: 'Gateway Timeout',
                                505: 'HTTP Version Not Supported', 506: 'Variant Also Negotiates', 
                                507: 'Insufficient Storage', 508: 'Loop Detected', 
                                509: 'Bandwidth Limit Exceeded', 510: 'Not Extended', 
                                511: 'Network Authentication Required', 520: 'Origin Error', 
                                521: 'Web server is down', 522: 'Connection timed out',
                                523: 'Proxy Declined Request',  524: 'A timeout occurred', 
                                598: 'Network read timeout error', 599: 'Network connect timeout error'}
        self.response_headers = ['Access-Control-Allow-Origin', 'Accept-Ranges', 'Age', 'Allow', 
                                'Cache-Control', 'Connection', 'Content-Encoding', 'Content-Language',
                                'Content-Length', 'Content-Location', 'Content-MD5', 'Content-Disposition',
                                'Content-Range', 'Content-Type', 'Date', 'ETag', 'Expires', 
                                'Last-Modified', 'Link', 'Location', 'P3P', 'Pragma', 'Proxy-Authenticate',
                                'Refresh', 'Retry-After', 'Server', 'Set-Cookie', 'Status',
                                'Strict-Transport-Security', 'Trailer', 'Transfer-Encoding',
                                'Upgrade', 'Vary', 'Via', 'Warning', 'WWW-Authenticate', 'X-Frame-Options',
                                'Public-Key-Pins', 'X-XSS-Protection', 'Content-Security-Policy',
                                'X-Content-Security-Policy', 'X-WebKit-CSP', 'X-Content-Type-Options',
                                'X-Powered-By', 'X-UA-Compatible'] 

    def makeMethod(self):
        return {'method': random.choice(self.methods)}

    def makePath(self, max_ext=3, min_path=10, max_path=30):
        path = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + self.slash) for _ in range(min_path, max_path)) 
        ext = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(max_ext)) 
        return {'path':self.slash + path, 'extension':ext}
        
    def makeProtocol(self):
        return {'protocol': self.protocol}
        
    def makeVersion(self, minor = [0, 1], major = [1, 2]):
        return {'version': {'major': str(random.choice(major)), 'minor':str(random.choice(minor))}}
            
    def makeRandomHeads(self, head_dict, min_head_c=0, max_head_c=10, min_head_vl=0, max_head_vl=25):
        heads = {}
        for i in range(min_head_c, max_head_c):
            h = random.choice(head_dict)
            heads[h] = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + '/' + ';' + '=' + ',') for _ in range(min_head_vl, max_head_vl))
        return {'headers': heads}
       
    def makeData(self, max_size=4000):
        return {'data': '%01x' % random.randrange(16**max_size)}

    def makeRcode(self):
        rcode = random.choice(self.status_codes.keys())
        return {'rcode': str(rcode), 'status': self.status_codes[rcode]}

    def makeSpecificHeads(self, key='Farts', value='Mozilla/4.0'):
        return {str(key): str(value)}
                
    def requestObject(self):
        req = {}
        req.update(self.makeMethod())
        req.update(self.makePath())
        req.update(self.makeProtocol())
        req.update(self.makeVersion())
        req.update(self.makeRandomHeads(self.request_headers))
        req.update(self.makeData())
        req['headers'].update(self.makeSpecificHeads( key='Content-Length', value=len(req['data']) ))
        req['headers'].update(self.makeSpecificHeads( key='User-Agent', value='Mozilla/4.0' ))
        req['headers'].update(self.makeSpecificHeads( key='Host', value='farts.farts' ))
        return req
        
    def responseObject(self):
        resp = {}
        resp.update(self.makeProtocol())
        resp.update(self.makeVersion())
        resp.update(self.makeRcode())
        resp.update(self.makeRandomHeads(self.response_headers))
        resp.update(self.makeData())
        resp['headers'].update(self.makeSpecificHeads( key='Content-Length', value=len(resp['data']) ))
        resp['headers'].update(self.makeSpecificHeads( key='Server', value='Farts v1.0' ))
        return resp

    def request(self):    
        reqObj = self.requestObject()
        reqFile = StringIO()
        
        # line one
        reqFile.write(reqObj['method'])
        reqFile.write(self.space)
        reqFile.write(reqObj['path'])
        reqFile.write(self.period)
        reqFile.write(reqObj['extension'])
        reqFile.write(self.space)
        reqFile.write(reqObj['protocol'])
        reqFile.write(self.slash)
        reqFile.write(reqObj['version']['major'])
        reqFile.write(self.period)
        reqFile.write(reqObj['version']['minor'])
        reqFile.write(self.crlf)
        # headers
        for k,v in reqObj['headers'].iteritems():
            reqFile.write(k)
            reqFile.write(self.colon_space)
            reqFile.write(v)
            reqFile.write(self.crlf)
        reqFile.write(self.crlf)
        # data
        reqFile.write(reqObj['data'])
        reqFile.write(self.crlf)
        reqFile.write(self.crlf)
        return reqFile.getvalue()
        
    def response(self):
        respObj = self.responseObject()
        respFile = StringIO()
        respFile.write(respObj['protocol'])
        respFile.write(self.slash)
        respFile.write(respObj['version']['major'])
        respFile.write(self.period)
        respFile.write(respObj['version']['minor'])
        respFile.write(self.space)
        respFile.write(respObj['rcode'])
        respFile.write(self.space)
        respFile.write(respObj['status'])
        respFile.write(self.crlf)
        for k,v in respObj['headers'].iteritems():
            respFile.write(k)
            respFile.write(self.colon_space)
            respFile.write(v)
            respFile.write(self.crlf)
        respFile.write(self.crlf)
        respFile.write(respObj['data'])
        respFile.write(self.crlf)
        respFile.write(self.crlf)
        return respFile.getvalue()
