# Crie um código em Python que teste se um site está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://g1.globo.com/')
except urllib.error.URLError:
    print('O site solicitado não está acessível no momento!')
else:
    print('O site está acessível!')
    print(site.read())
