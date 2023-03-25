# Changuito Smart

Changuito Smart es una aplicación para calcular los precios de compras en una zona geográfica determinada. Consultamos precios de productos en los sitios web de diversos supermercados, y te ayudamos a armar tu lista de compras con el mejor precio posible. También te ayuda a localizar en un mapa la ruta óptima para que gastes lo menos posible cerca de tu casa.

## Implementación

Un servicio scrapper consulta los sitios web de las grandes cadenas de supermercados, y los procesa y almacena en una base de datos propia (Elastic Cloud) para poder realizar búsquedas personalizadas. Obtenemos la ubicación de todos los supermercados disponibles mediante el servicio de Precios Justos de la nación, y utilizamos el servicio de Open Street Maps para ubicarlos en un mapa.
