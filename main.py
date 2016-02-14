#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
		
def bus_rtpi_get_result(number):
    try:
        number = str(number)
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        url = "http://dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery="+str(number)
        req = urllib2.Request(url, None, headers)
        response = urllib2.urlopen(req)
        html = response.read()
        html = html.replace("""<img src="/Templates/Public/Styles/Images/icon-small-accessible.gif" alt="Accessible" class='' />""",'A')
        html = html.replace("""<img src="/Templates/Public/Styles/Images/icon-small-R-pred.gif" alt="R Prediction" class='' />""",'R')
        html = html.replace("""<img src="/Templates/Public/Styles/Images/icon-small-E-pred.gif" alt="E Prediction" class='' />""",'E')
        soup = BeautifulSoup(html, "html.parser")
        result = []
        for results in soup.findAll(id="rtpi-results"):
            for row in results.findAll("tr"):
                for col in row.findAll("td"):
                    result.append(' '.join(col.text.split()))
            break
        for results in soup.findAll(id="ctl00_FullRegion_MainRegion_ContentColumns_holder_RealTimeStopInformation1_lblStopAddress"):
            Location = results.text
            break
        for results in soup.findAll("strong"):
            if "Last Updated at" in results.text:
                LastUpdated = ' '.join(results.text.replace("Last Updated at","").split()) 
                break
        tags_open = ["    <Bus>\n        <Route>","        <Destination>","        <ExpectedTime>","        <Notes>"]
        tags_close = ["</Route>","</Destination>","</ExpectedTime>","</Notes>\n    </Bus>"]
        n = 0
        xml = ""
        xml += "<RealTimeInformationResults>\n"
        xml += "    <StopNumber>"+str(number)+"</StopNumber>\n"
        xml += "    <StopAddress>"+Location+"</StopAddress>\n"
        xml += "    <LastUpdated>"+LastUpdated+"</LastUpdated>\n"
        for bus in result:
            xml +=  str(tags_open[n%4]) + bus + str(tags_close[n%4]) + "\n"
            n += 1
        xml +=  "</RealTimeInformationResults>\n"
        return xml.strip("\n")
    except:
        return ""

def bus_html_table(stop, buses=[], header=False, Notes=True):
    if Notes:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td><td>Notes</td></tr>\n"
    else:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td></tr>\n"
    html = bus_rtpi_get_result(stop)
    soup = BeautifulSoup(html, "html.parser")
    routes = []
    destinations = []
    expectedtimes = []
    notes = []
    table = ""
    for route in soup.findAll("route"):
        routes.append(route.text)
    for destination in soup.findAll("destination"):
        destinations.append(destination.text)
    for expectedtime in soup.findAll("expectedtime"):
        expectedtimes.append(expectedtime.text)
    for note in soup.findAll("notes"):
        notes.append(note.text)
    for n in range(len(routes)):
        if buses == [] or routes[n] in buses:
            if Notes:
                table += "<tr><td>"+routes[n]+"</td><td>"+destinations[n]+"</td><td>"+expectedtimes[n]+"</td><td>"+notes[n]+"</td></tr>\n"
            else:
                table += "<tr><td>"+routes[n]+"</td><td>"+destinations[n]+"</td><td>"+expectedtimes[n]+"</td></tr>\n"
    if header:
        return "<table>\n"+head+table+"</table>"
    else:
        return "<table>\n"+table+"</table>"

def bus_order_html_table(rows, header=True, Notes=True):
    if Notes:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td><td>Notes</td></tr>\n"
    else:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td></tr>\n"
    times = ["Due"]
    rows = rows.replace(head,"")
    for t in range(60*24):
        minute = (t)%60
        hour = (4 + (t - minute)/60)%24
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        times.append(str(hour)+":"+str(minute))
    rows = rows.replace("<table>\n","").replace("</table>","")
    results = ""
    for time in times:
        for row in rows.split("\n"):
            if time in row:
                results += row+"\n"
    if header:
        return "<table>\n"+head+results+"</table>"
    else:
        return "<table>\n"+results+"</table>"

#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
		
def bus_rtpi_get_result(number):
    try:
        number = str(number)
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        url = "http://dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery="+str(number)
        req = urllib2.Request(url, None, headers)
        response = urllib2.urlopen(req)
        html = response.read()
        html = html.replace("""<img src="/Templates/Public/Styles/Images/icon-small-accessible.gif" alt="Accessible" class='' />""",'A')
        html = html.replace("""<img src="/Templates/Public/Styles/Images/icon-small-R-pred.gif" alt="R Prediction" class='' />""",'R')
        html = html.replace("""<img src="/Templates/Public/Styles/Images/icon-small-E-pred.gif" alt="E Prediction" class='' />""",'E')
        soup = BeautifulSoup(html, "html.parser")
        result = []
        for results in soup.findAll(id="rtpi-results"):
            for row in results.findAll("tr"):
                for col in row.findAll("td"):
                    result.append(' '.join(col.text.split()))
            break
        for results in soup.findAll(id="ctl00_FullRegion_MainRegion_ContentColumns_holder_RealTimeStopInformation1_lblStopAddress"):
            Location = results.text
            break
        for results in soup.findAll("strong"):
            if "Last Updated at" in results.text:
                LastUpdated = ' '.join(results.text.replace("Last Updated at","").split()) 
                break
        tags_open = ["    <Bus>\n        <Route>","        <Destination>","        <ExpectedTime>","        <Notes>"]
        tags_close = ["</Route>","</Destination>","</ExpectedTime>","</Notes>\n    </Bus>"]
        n = 0
        xml = ""
        xml += "<RealTimeInformationResults>\n"
        xml += "    <StopNumber>"+str(number)+"</StopNumber>\n"
        xml += "    <StopAddress>"+Location+"</StopAddress>\n"
        xml += "    <LastUpdated>"+LastUpdated+"</LastUpdated>\n"
        for bus in result:
            xml +=  str(tags_open[n%4]) + bus + str(tags_close[n%4]) + "\n"
            n += 1
        xml +=  "</RealTimeInformationResults>\n"
        return xml.strip("\n")
    except:
        return ""

def bus_html_table(stop, buses=[], header=False, Notes=True):
    if Notes:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td><td>Notes</td></tr>\n"
    else:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td></tr>\n"
    html = bus_rtpi_get_result(stop)
    soup = BeautifulSoup(html, "html.parser")
    routes = []
    destinations = []
    expectedtimes = []
    notes = []
    table = ""
    for route in soup.findAll("route"):
        routes.append(route.text)
    for destination in soup.findAll("destination"):
        destinations.append(destination.text)
    for expectedtime in soup.findAll("expectedtime"):
        expectedtimes.append(expectedtime.text)
    for note in soup.findAll("notes"):
        notes.append(note.text)
    for n in range(len(routes)):
        if buses == [] or routes[n] in buses:
            if Notes:
                table += "<tr><td>"+routes[n]+"</td><td>"+destinations[n]+"</td><td>"+expectedtimes[n]+"</td><td>"+notes[n]+"</td></tr>\n"
            else:
                table += "<tr><td>"+routes[n]+"</td><td>"+destinations[n]+"</td><td>"+expectedtimes[n]+"</td></tr>\n"
    if header:
        return "<table>\n"+head+table+"</table>"
    else:
        return "<table>\n"+table+"</table>"

def bus_order_html_table(rows, header=True, Notes=True):
    if Notes:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td><td>Notes</td></tr>\n"
    else:
        head = "<tr><td>Routes</td><td>Destinations</td><td>Expected<br/>Times</td></tr>\n"
    times = ["Due"]
    rows = rows.replace(head,"")
    for t in range(60*24):
        minute = (t)%60
        hour = (4 + (t - minute)/60)%24
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        times.append(str(hour)+":"+str(minute))
    rows = rows.replace("<table>\n","").replace("</table>","")
    results = ""
    for time in times:
        for row in rows.split("\n"):
            if time in row:
                results += row+"\n"
    if header:
        return "<table>\n"+head+results+"</table>"
    else:
        return "<table>\n"+results+"</table>"