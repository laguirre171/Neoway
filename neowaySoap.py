import json
import httplib2
import pprint

h = httplib2.Http(".cache")
(resp_headers, content) = h.request("http://example.org/", "GET")
pprint.pprint(resp_headers)
