# Dublin-Bus-RTPI-Scraper


## About
A Python Scraper for a clean scrape of Dublin Bus RTPI times


## Contents
1. main.py


## How to use it
Basically you can copy the code in main.py to your project, some examples are below.


## Examples


### Get resutlts in xml form from one bus stop
#### For example stop 1385
xml =  bus_rtpi_get_result(1385)
print xml

### Get results in html form from one bus stop
#### For example stop 1385
table = bus_html_table(1385)
print table


### Get only certain bus route results from one bus stop in html form
#### For example show the 16 bus from stop 1348
table = bus_html_table(1348, ["16","16c"])
print table


### Get only certain bus routes from certain bus stops in html form
#### For example, show only the 68 and 122 from 1385, the 49 and 54a from the 2634 and finally the 9 and 16 from the 1348 stop
for pairs in [[1385,["68a","68","122"]] , [2634,["49","54a"]] , [1348,["9","16","16c"]] ]:
    table += bus_html_table(pairs[0], pairs[1])
	page =  bus_order_html_table(table)
	print page

	
## Disclaimer
I'm not in any way affiliated with Dublin Bus whatsoever.


## Demo
To see this script in action, check out http://www.dublinbus.co.nr
:)