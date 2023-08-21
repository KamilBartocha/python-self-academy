"""SOAP stands for Simple Object Access Protocol, as the name suggests nothing
but a protocol for exchanging structured data between nodes. It uses XML.

A SOAP message is an ordinary XML document containing the following elements:

- An Envelope element that identifies the XML document as a SOAP message
- A Header element that contains header information
- A Body element that contains call and response information
- A Fault element containing errors and status information"""

# SOAP call with requests lib
import requests
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                <soap:Body>
                    <CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                        <sCountryISOCode>IN</sCountryISOCode>
                    </CountryIntPhoneCode>
                </soap:Body>
            </soap:Envelope>"""
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.request(method="POST",
                            url=url,
                            headers=headers,
                            data=payload)

print(response.text)
print(response)
