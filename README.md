# Dublin-Bus-RTPI-Scraper

## About
A Python Scraper for a clean scrape of Dublin Bus RTPI times

## Contents
1. main.py

## How to use it
Basically you can copy the code in main.py to your project, some examples are below.

## Examples

### Get resutlts in xml form from one bus stop
xml =  bus_rtpi_get_result(1385)
print xml

<RealTimeInformationResults>
    <StopNumber>1385</StopNumber>
    <StopAddress>South Circular Road, Griffith College</StopAddress>
    <LastUpdated>13:52:09</LastUpdated>
    <Bus>
        <Route>122</Route>
        <Destination>Ashington via City Centre</Destination>
        <ExpectedTime>14:04</ExpectedTime>
        <Notes>A</Notes>
    </Bus>
    <Bus>
        <Route>68</Route>
        <Destination>Burgh Quay via Sth Circular Rd</Destination>
        <ExpectedTime>14:46</ExpectedTime>
        <Notes>A</Notes>
    </Bus>
</RealTimeInformationResults>

### Get results in html form from one bus stop
table = bus_html_table(1385)
print table

<table>
<tr><td>122</td><td>Ashington via City Centre</td><td>14:04</td><td>A</td></tr>
<tr><td>68</td><td>Burgh Quay via Sth Circular Rd</td><td>14:46</td><td>A</td></tr>
</table>

### Get only certain bus route results from one bus stop in html form
table = bus_html_table(1348, ["16","16c"])
print table

<table>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>13:56</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:09</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:19</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:43</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:52</td><td>A</td></tr>
</table>

### Get only certain bus routes from certain bus stops in html form
for pairs in [[1385,["68a","68","122"]] , [2634,["49","54a"]] , [1348,["9","16","16c"]] ]:
    table += bus_html_table(pairs[0], pairs[1])
page =  bus_order_html_table(table)
print page

<table>
<tr><td>Routes</td><td>Destinations</td><td>Expected Times</td><td>Notes</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>13:56</td><td>A</td></tr>
<tr><td>9</td><td>Charlestown via City Centre</td><td>13:59</td><td>A</td></tr>
<tr><td>122</td><td>Ashington via City Centre</td><td>14:04</td><td>A</td></tr>
<tr><td>49</td><td>Pearse St via Ballycullen Road</td><td>14:07</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:09</td><td>A</td></tr>
<tr><td>9</td><td>Charlestown via City Centre</td><td>14:14</td><td>A</td></tr>
<tr><td>54a</td><td>Pearse St via Harold's Cross</td><td>14:17</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:19</td><td>A</td></tr>
<tr><td>9</td><td>Charlestown via City Centre</td><td>14:29</td><td>A</td></tr>
<tr><td>49</td><td>Pearse St via Ballycullen Road</td><td>14:30</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:43</td><td>A</td></tr>
<tr><td>9</td><td>Charlestown via City Centre</td><td>14:44</td><td>A</td></tr>
<tr><td>68</td><td>Burgh Quay via Sth Circular Rd</td><td>14:46</td><td>A</td></tr>
<tr><td>54a</td><td>Pearse St via Harold's Cross</td><td>14:47</td><td>A</td></tr>
<tr><td>16</td><td>Dublin Airport via O'Connell Street</td><td>14:52</td><td>A</td></tr>
</table>

## Disclaimer
I'm not in any way affiliated with Dublin Bus whatsoever.

## Demo
To see this script in action, check out http://www.dublinbus.co.nr
:)

## Thanks
