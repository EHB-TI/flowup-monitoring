#in progress

from xmlObject import Heartbeat
import xml.etree.ElementTree as ET


def parse(data):
    myroot = ET.fromstring(data)
    dataArray = []
    for elements in myroot:
        for x in elements:
            dataArray.append(x.text)
    result = Heartbeat(dataArray[0], dataArray[1], dataArray[2], dataArray[3], dataArray[4], dataArray[5])
    return format(result)

def format(data):
    new_data = "{} - {} - {}".format(data.nameService,data.RAMload, data.CPUload)
    return new_data

data = """
<heartbeat>
    <header>
      <code>2000</code>
      <origin>FrontEnd</origin>
      <timestamp>2021-05-25T12:00:00+01:00</timestamp>
    </header>
    <body>
      <nameService>Website</nameService>
      <CPUload>5.63</CPUload>
      <RAMload>86.13</RAMload>
    </body>
</heartbeat>"""