import pytest
from parseXML import parse

def test_parse():
    xmlVoorbeeld = """
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
        </heartbeat> """
    result = parse(xmlVoorbeeld)
    assert result == "FrontEnd:Website - 2021-05-25T12:00:00+01:00 - 86.13 - 5.63 - 2000"
