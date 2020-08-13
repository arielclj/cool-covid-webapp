import urllib3
import http.cookiejar

http = urllib3.PoolManager()

# Testing access to login page
url_login = 'http://localhost:8201/en/login/'
req_login = http.request('GET', url_login)
print('HTTP response code for login page: ' + str(req_login.status))

# Testing access to dashboard page with previous cookie issued
login_headers = { \
    'Connection': 'keep-alive' , \
'Cache-Control': 'max-age=0' , \
'Upgrade-Insecure-Requests': '1' , \
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36' , \
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' , \
'Sec-Fetch-Site': 'none' , \
'Sec-Fetch-Mode': 'navigate' , \
'Sec-Fetch-User': '?1' , \
'Sec-Fetch-Dest': 'document' , \
'Accept-Encoding': 'gzip, deflate, br' , \
'Accept-Language': 'en-US,en;q=0.9' , \
'Cookie': 'csrftoken=DgJ6w91Wsnv6r6TAFhjvnm7er1RjVSXjjOART9QESoxss1OUW0tXakUzRz38i1W9; sessionid=sqqfjqhe5eifwy1hbzghou0manwu981w' , \
            }
url_dashboard = 'http://localhost:8201/en/dashboard/'
req_dashboard = http.request('GET', url_dashboard, headers=login_headers)
print('HTTP response code for dashboard page: ' + str(req_dashboard.status))

# Testing access to upload, database, figure pages
urllist = {
    'upload': 'http://localhost:8201/en/upload/',
    'database': 'http://localhost:8201/en/database/',
    'figure': 'http://localhost:8201/en/figure/',
}
for page, url in urllist.items():
    req = http.request('GET', url)
    print('HTTP response code for %s page: ' % (page) + str(req.status))

# urls available upon user upload
# urllist_uploaded = [
#     'http://localhost:8201/en/column_list/',
#     'http://localhost:8201/en/figure_design/',
#     'http://localhost:8201/en/retention/advance/'
# ]

