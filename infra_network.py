####################################################################################################
# First Release v1.0
# - Provide method 
#     Check Endpoint
#     Sample for contextroot:
#          from infra_network import checkEndpoint
#          checkEndpoint("https://www.google.com/test") <--- Contextroot without port or with port
#          'Pass'            <--- Success Case
#          'NotPass'         <--- Fail Case
#     Sample for host & port:
#          from infra_network import checkDomainPort
#          checkEndpoint("www.google.com",443) 			<--- Contextroot without port or with port
#          'Pass'            <--- Success Case
#          'NotPass'         <--- Fail Case
####################################################################################################
import socket
from urllib.parse import urlparse

def checkEndpoint(
			url
		):
	try:
		url_parse = urlparse(url)
		if (url_parse.port == None) and ((url_parse.scheme == "http")):
			url_parse_port = 80
		else:
			if (url_parse.port == None) and ((url_parse.scheme == "https")):
				url_parse_port = 443
			else:
				url_parse_port = url_parse.port
				print("Out of if")
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((url_parse.hostname,url_parse_port))
		if result == 0:
		   return "Pass"
		else:
		   return "NotPass"
	except:
		pass
	return False

def checkDomainPort(
			host,port
		):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((host,port))
		if result == 0:
		   return "Pass"
		else:
		   return "NotPass"
	except:
		pass
	return False





		