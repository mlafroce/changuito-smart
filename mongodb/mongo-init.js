db.createCollection("changuito");

db.Branches.insertMany([{
		id: "1-1-1302",
		name: "Coto cerca",
		location: {
			address: "Avda. Monseñor",
			lat: "-24.830882",
			long: "-65.428647",
			city: "Capital"
		},
		trade_name: "Coto S.A"
	},
	{
		id: "2-1-1302",
		name: "Coto lejos",
		location: {
			address: "Avda. Avda.",
			lat: "-24.830882",
			long: "-65.428647",
			city: "Capital"
		},
		trade_name: "Coto S.A"
	}, {
		id: "3-1-1302",
		name: "Carrefour cerca",
		location: {
			address: "Avda. Monseñor Tavella ",
			lat: "-24.830882",
			long: "-65.428647",
			city: "Capital"
		},
		trade_name: "Carrefour S.A"
	},
	{
		id: "4-1-1302",
		name: "Carrefour lejos",
		location: {
			address: "Avda. Monella",
			lat: "-24.830882",
			long: "-65.428647",
			city: "Capital"
		},
		trade_name: "Carrefour S.A"
	},
	{
		id: "5-1-1302",
		name: "Coto online",
		location: {
			online: true,
			city: "Capital"
		},
		trade_name: "Coto S.A"
	}
])


db.Products.insertMany([

	{
		id: "0000000000011",
		brand: "Sancor",
		price: {
			min: 100,
			max: 150
		},
		description: "Leche Sancor 1L",
		categories: "None"
	},
	{
		id: "0000000000012",
		brand: "La martona",
		price: {
			min: 100,
			max: 250
		},
		description: "Leche La martona 1L",
		categories: "None"
	},
	{
		id: "0000000000013",
		brand: "La serenisima",
		price: {
			min: 150,
			max: 200
		},
		description: "Leche La serenisima 1L",
		categories: "None"
	},

	{
		id: "0000000000021",
		brand: "Sancor",
		price: {
			min: 150,
			max: 150
		},
		description: "MAnteca Sancor 200gr",
		categories: "None"
	},

	{
		id: "0000000000031",
		brand: "Pureza",
		price: {
			min: 100,
			max: 120
		},
		description: "HArINA 0000 1kg",
		categories: "None"
	}, {
		id: "0000000000032",
		brand: "Pureza",
		price: {
			min: 100,
			max: 150
		},
		description: "harina 000 200gr",
		categories: "None"
	}, {
		id: "0000000000033",
		brand: "Blancaflor",
		price: {
			min: 90,
			max: 160
		},
		description: "HArINA blancaflor 0000 1kg",
		categories: "None"
	},
	{
		id: "0000000000041",
		brand: "Aguila",
		price: {
			min: 100,
			max: 230
		},
		description: "Chocolate aguila 500gr",
		categories: "None"
	}
])

// producto 1
db.Prices.insertMany([
	//sucursal 1
	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 100.00,
		"date": "2023-06-07"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 100.00,
		"date": "2023-06-08"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 110.00,
		"date": "2023-06-09"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 110.00,
		"date": "2023-06-10"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 140.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 150.00,
		"date": "2023-06-12"
	},
	//sucrsal2
	{
		"product_id": "0000000000011",
		"branch_id": "2-1-1302",
		"price": 110.00,
		"date": "2023-06-07"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "2-1-1302",
		"price": 110.00,
		"date": "2023-06-08"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "2-1-1302",
		"price": 110.00,
		"date": "2023-06-09"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "2-1-1302",
		"price": 110.00,
		"date": "2023-06-10"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "2-1-1302",
		"price": 150.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "2-1-1302",
		"price": 150.00,
		"date": "2023-06-12"
	},
	//sucrsal3
	{
		"product_id": "0000000000011",
		"branch_id": "3-1-1302",
		"price": 120.00,
		"date": "2023-06-07"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "3-1-1302",
		"price": 110.00,
		"date": "2023-06-08"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "3-1-1302",
		"price": 110.00,
		"date": "2023-06-09"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "3-1-1302",
		"price": 130.00,
		"date": "2023-06-10"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "3-1-1302",
		"price": 130.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "3-1-1302",
		"price": 130.00,
		"date": "2023-06-12"
	},
	//sucrsal4 solo tiene el producto los ultimos dias
	{
		"product_id": "0000000000011",
		"branch_id": "4-1-1302",
		"price": 150.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000011",
		"branch_id": "4-1-1302",
		"price": 150.00,
		"date": "2023-06-12"
	},
	//sucursal 1 algunos dias si otros no mismos precios que sucu 1
	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 100.00,
		"date": "2023-06-07"
	},

	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 110.00,
		"date": "2023-06-09"
	},

	{
		"product_id": "0000000000011",
		"branch_id": "1-1-1302",
		"price": 140.00,
		"date": "2023-06-11"
	}

])

// producto 2
db.Prices.insertMany([
	//sucursal 1
	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 110.00,
		"date": "2023-06-07"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 120.00,
		"date": "2023-06-08"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 130.00,
		"date": "2023-06-09"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 140.00,
		"date": "2023-06-10"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 140.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 150.00,
		"date": "2023-06-12"
	},
	//sucrsal2
	{
		"product_id": "0000000000012",
		"branch_id": "2-1-1302",
		"price": 120.00,
		"date": "2023-06-07"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "2-1-1302",
		"price": 130.00,
		"date": "2023-06-08"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "2-1-1302",
		"price": 130.00,
		"date": "2023-06-09"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "2-1-1302",
		"price": 130.00,
		"date": "2023-06-10"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "2-1-1302",
		"price": 150.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "2-1-1302",
		"price": 150.00,
		"date": "2023-06-12"
	},
	//sucrsal3
	{
		"product_id": "0000000000012",
		"branch_id": "3-1-1302",
		"price": 120.00,
		"date": "2023-06-07"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "3-1-1302",
		"price": 110.00,
		"date": "2023-06-08"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "3-1-1302",
		"price": 110.00,
		"date": "2023-06-09"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "3-1-1302",
		"price": 130.00,
		"date": "2023-06-10"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "3-1-1302",
		"price": 130.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "3-1-1302",
		"price": 130.00,
		"date": "2023-06-12"
	},
	//sucrsal4 solo tiene el producto los ultimos dias
	{
		"product_id": "0000000000012",
		"branch_id": "4-1-1302",
		"price": 150.00,
		"date": "2023-06-11"
	},
	{
		"product_id": "0000000000012",
		"branch_id": "4-1-1302",
		"price": 150.00,
		"date": "2023-06-12"
	},
	//sucursal 1 algunos dias si otros no mismos precios que sucu 1
	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 100.00,
		"date": "2023-06-07"
	},

	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 110.00,
		"date": "2023-06-09"
	},

	{
		"product_id": "0000000000012",
		"branch_id": "1-1-1302",
		"price": 140.00,
		"date": "2023-06-11"
	}
])
