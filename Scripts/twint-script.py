#!c:\users\hp\onedrive\masaüstü\web_scrapping\web_scrapping\scripts\python.exe -x
# EASY-INSTALL-ENTRY-SCRIPT: 'twint','console_scripts','twint'
__requires__ = 'twint'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('twint', 'console_scripts', 'twint')()
    )
