from urllib.parse import urlencode
from urllib.request import Request, urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = 'https://mf2012-06.npb.local:9777/api/v2/scan/rundetails'
url2 = 'https://mf2012-06.npb.local:9777/token'

#urlhandle = urlopen(url2, context = ctx)

req = Request(url2)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
#req.add_header('Authorization', 'bearer AQAAANCMnd8BFdERjHoAwE_Cl-sBAAAAvEX6xRU4ykudlp-xXL343AAAAAACAAAAAAADZgAAwAAAABAAAACCf4LBZmevmBkcIfZw3jGAAAAAAASAAACgAAAAEAAAAKkdXmYy-1WzlldiuS8CGZ7QAAAAYURZoNZeFynOmR0NgXG_ABnN5w5J2JlQI6eHlnMD_shMMQh92whWuLesxi-k4UiFwh-d5j-GKCjEJknnKMzNfzFtD2Ncl5zXvzaYCOmraIsRahQ2D6bZ0VZCU490dhFa3tApmLppUY5IDjJnWMnCfs4LuDTvpuOVCHnpdIQJRB35sRZ-JIN-cHKrj-7famw2gh5-CX1qug0v9SdRYcAH59ojP198VWYsRA3ME7W3LLorTPq-KNcUoaaGZzAVO8_sVmmelFC4dT9zII8tlSAf3BQAAAC3YoyW36tv83lyPyQybY1Dk0Fvtw')
response = urlopen(req, context=ctx)
#data = urlopen(response, context=ctx).read().decode()
# js = json.loads(data)
# print(js)
