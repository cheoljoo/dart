import math
import requests

print( math.sqrt(10))
resp =  requests.get("https://en.wikipedia.org/wiki/Computer_(job_description)")
print( resp)
# print resp.content


