
import requests
def caller(url):
    
    with open('domains.txt','r') as  subdomains:
        for subdomain in subdomains:
           subdomain_line = subdomain.strip()
           try:
                response = requests.get('https://'+subdomain_line+'.'+url)   
                if response.status_code == 200:
                    print('[+] successful https://'+subdomain_line+'.'+url+' [+]')   
           except :
             pass




caller("google.com")
