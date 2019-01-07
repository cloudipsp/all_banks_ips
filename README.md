CSV file of all banks domains and IPs provided by [FONDY Payment Service Provider](https://fondy.eu)
=====
```
python2.7 get_ips.py
```

resulting file acs_url.csv contains all banks main websites and 3DSecure pages domains which are called Access Controll Servers

file structure is

domain, port, bank country, ip list

sample row from acs_url.csv:

"3dsecure.maybank.com.sg","443","sg","['206.99.153.116']"

This can be used for example by internet providers to add IPs to whitelist 
in order customers could top up having negative account balance.

## get plain IP's by country
```
python2.7 get_ips_plain.py --country 'us' --file result_ips_us.csv
```


## Author

Maxim Kozenko, max.dnu@gmail.com
