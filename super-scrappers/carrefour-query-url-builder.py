import base64
import json
import requests
import urllib.parse

HOST = "https://www.carrefour.com.ar"
QUERY_PATH_ROOT = "_v/segment/graphql/v1"
QUERY_PATH_VARIABLES = "workspace=master&maxAge=short&appsEtag=remove&domain=store&locale=es-AR&__bindingId=ecd0c46c-3b2a-4fe1-aae0-6080b7240f9b&operationName=productSearchV3&variables=%7B%7D"
MAX_ITEMS_PER_PAGE = 100

def request_page(category, page_id):
	item_from = page_id * MAX_ITEMS_PER_PAGE
	item_to = (page_id + 1) * MAX_ITEMS_PER_PAGE - 1

	extensions_variables = {
		"hideUnavailableItems":False,
		"skusFilter":"ALL_AVAILABLE",
		"simulationBehavior":"default",
		"installmentCriteria":"MAX_WITHOUT_INTEREST",
		"productOriginVtex":False,
		"map":"c",
		"orderBy":"OrderByScoreDESC",
		"from": item_from,
		"to": item_to,
		"selectedFacets":[{"key":"c","value":category}],
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

	return requests.get(query_path)

def retrieve_items(category):
	pages = 1
	current_page = 0
	total_items = 0
	while current_page < pages:
		print("Retrieving from {} to {}".format(current_page * MAX_ITEMS_PER_PAGE, (current_page + 1) * MAX_ITEMS_PER_PAGE - 1))
		response = request_page(category, current_page)
		if not response.ok:
			print("Request failed, aborting")
			print(f"URL: {response.url}")
			return
		else:
			print("Request ok")
		data = response.json()
		try:
			print("DATA:", data)
			total_items = data['data']['productSearch']['recordsFiltered']
		except TypeError:
			print("Unexpected data error")
			print(f"URL: {response.url}")
			print(data)
			return
		pages = total_items // MAX_ITEMS_PER_PAGE + 1
		filename = "carrefour-{}-{}.json".format(category, current_page)
		with open(filename, "w") as output:
		    # Writing data to a file
		    product_list = data['data']['productSearch']['products']
		    output.write(json.dumps(product_list))
		current_page += 1

categories = ["almacen", "electro-y-tecnologia", "bazar-y-textil", "desayuno-y-merienda", "bebidas", "lacteos-y-productos-frescos"]

for category in categories:
	retrieve_items(category)
