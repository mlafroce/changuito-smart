import base64
import json
import requests
import urllib.parse

HOST = "https://www.carrefour.com.ar"
QUERY_PATH_ROOT = "_v/segment/graphql/v1"
QUERY_PATH_VARIABLES = "workspace=master&maxAge=short&appsEtag=remove&domain=store&locale=es-AR&__bindingId=ecd0c46c-3b2a-4fe1-aae0-6080b7240f9b&operationName=productSearchV3&variables=%7B%7D"

extensions_variables = {
	"hideUnavailableItems":False,
	"skusFilter":"ALL_AVAILABLE",
	"simulationBehavior":"default",
	"installmentCriteria":"MAX_WITHOUT_INTEREST",
	"productOriginVtex":False,
	"map":"c",
#	"query":"almacen",
	"orderBy":"OrderByScoreDESC",
	"from":100,
	"to":199,
#	"selectedFacets":[{"key":"c","value":"almacen"},{"key":"priceRange","value":"37 TO 6130"}],
	"selectedFacets":[{"key":"priceRange","value":"37 TO 6130"}],
	"fuzzy":"0",
	"searchState": None,
	"facetsBehavior":"Static",
	"categoryTreeBehavior":"default",
	"withFacets":False
}

extensions_variables_str = json.dumps(extensions_variables, separators=(',', ':'))
extensions_variables_encoded = base64.b64encode(extensions_variables_str.encode('ascii')).decode('ascii')

extensions = {"persistedQuery":{"version":1,"sha256Hash":"8d81f8e7468bea2046b664a5a1d9e4bb4e1f3f9e340dcb3701fd68b15c0e8025","sender":"vtex.store-resources@0.x","provider":"vtex.search-graphql@0.x"},"variables":extensions_variables_encoded }

extensions_encoded = urllib.parse.quote(json.dumps(extensions, separators=(',', ':')))

query_path = f"{HOST}/{QUERY_PATH_ROOT}?{QUERY_PATH_VARIABLES}&extensions={extensions_encoded}"

resp = requests.get(query_path)

print(resp.json())
