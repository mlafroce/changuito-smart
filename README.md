# Changuito smart

Trabajo práctico para la materia Taller de programación III de la Facultad de ingeniería de la UBA.

Para crear las imagenes
make docker-image


================
product schema
[
    {
        "name": "Mostaza Natura 250 g.",
        "nameComplete": "Mostaza Natura 250 g.",
        "complementName": "",
        "ean": "7791866004211",
        "measurementUnit": "un",
        "brand": "Natura",
        "categories": [
            "/Almacén/Sal, aderezos y saborizadores/Salsas y aderezos/",
            "/Almacén/Sal, aderezos y saborizadores/",
            "/Almacén/"
        ],
        "sellerName": "CARREFOUR",
        "PriceValidUntil": "2024-03-26T21:45:29Z",
        "Price": 174.5,
        "ListPrice": 174.5,
        "Tax": 0,
        "taxPercentage": 0,
        "spotPrice": 174.5,
        "PriceWithoutDiscount": 174.5
    },
    {
        "description": "",
        "productName": "Mostaza Natura 250 g.",
        "productReference": "630676",
        "linkText": "mostaza-natura-250-g-37830",
        "brandId": 2001545,
        "link": "/mostaza-natura-250-g-37830/p",
        "categoryId": "192",
        "priceRange": {
            "sellingPrice": {
                "highPrice": 174.5,
                "lowPrice": 174.5,
                "__typename": "PriceRange"
            },
            "listPrice": {
                "highPrice": 174.5,
                "lowPrice": 174.5,
                "__typename": "PriceRange"
            },
            "__typename": "ProductPriceRange"
        },
        "items": [
            {
                "name": "Mostaza Natura 250 g.",
                "nameComplete": "Mostaza Natura 250 g.",
                "complementName": "",
                "ean": "7791866004211",
                "measurementUnit": "un",
                "unitMultiplier": 1,
                "sellers": [
                    {
                        "sellerId": "1",
                        "sellerName": "CARREFOUR",
                        "sellerDefault": true,
                        "Price": 174.5,
                        "ListPrice": 174.5,
                        "Tax": 0,
                        "taxPercentage": 0,
                        "spotPrice": 174.5,
                        "PriceWithoutDiscount": 174.5,
                        "RewardValue": 0,
                        "PriceValidUntil": "2024-03-26T21:45:29Z",
                        "AvailableQuantity": 10000
                    }
                ]
            }
        ]
    }
]


================
Managing MongoDB from a Container
To manage your MongoDB server or to access, import, and export your data, you can use a second MongoDB container from which you will run the necessary CLI tools.

To open up a Mongo Shell session to your MongoDB Atlas server, use mongosh and specify the cluster URL.

docker run -it mongodb/mongodb-community-server:$MONGODB_VERSION mongosh "mongodb://username:password@clusterURL/database"
If you want to use the mongoexport tool to export an existing collection to a .json file, you can use the command from a separate MongoDB container. You will need to mount a volume to be able to access the resulting JSON file.

docker run -it -v $(pwd):/tmp mongodb/mongodb-community-server:$MONGODB_VERSION mongoexport --collection=COLLECTION --out=/tmp/COLLECTION.json "mongodb://username:password@clusterURL/database"
If you need to import data into a collection, you use the mongoimport tool, also available from the mongodb/mongodb-community-server:$MONGODB_VERSION image. Again, you will need to mount a volume to access a file stored on your local machine from inside the container.

docker run -it -v $(pwd):/tmp mongodb/mongodb-community-server:$MONGODB_VERSION mongoimport --drop --collection=COLLECTION "mongodb+srv://user:password@clusterURL/database" /tmp/COLLECTION.json
Any other tool that is packaged with a MongoDB installation can be accessed in the same fashion.
