curl "http://iatiregistry.org/api/3/action/organization_list?all_fields=true" > publishers.json



mkdir in
cd in
for i in {0..70}; do wget --load-cookies ../cookies.txt --content-disposition "https://docs.google.com/spreadsheet/fm?id=t1dbmZEqIWg5uuqN0GNw_rQ.00522594596467399731.7863298463475304452&fmcmd=5&gid=$i"; done  


