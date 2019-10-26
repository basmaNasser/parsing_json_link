import urllib2
import re
import json
import datetime
from datetime import datetime, timedelta,time


def parse(firstDate, lastDate, weekDay):

    link = "https://jsonmock.hackerrank.com/api/stocks/search?key=value&page=1"
    req = urllib2.Request(link)
    response = urllib2.urlopen(req)
    the_page = response.read()
    parsed_json = (json.loads(the_page))
    data=json.dumps(parsed_json, indent=4, sort_keys=True)
    for i in range(0,len(parsed_json['data'])):
        Date=parsed_json['data'][i]['date']
        openval=parsed_json['data'][i]['open']
        closeval=parsed_json['data'][i]['close']
        Date =datetime.strptime(str(Date), "%d-%B-%Y").date()
        weekday= Date.strftime('%A')
        firstDate1=datetime.strptime(str(firstDate), "%d-%B-%Y").date()
        lastDate1=datetime.strptime(str(lastDate), "%d-%B-%Y").date()
       
        if  weekDay in weekday:
            if Date >= firstDate1 and Date < lastDate1  :
                print Date,openval,closeval
        

parse('1-january-2000','22-February-2000','Monday')
