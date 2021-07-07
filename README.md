# Django App for Polotic course

### Autenticacion
| Usuario | Contraseña                                    |
|---------|-----------------------------------------------|
| admin   | admin                                         |
| mod     | moderator                                     |
| usuario | (Usar formulario de registro en /registrarse) |



## Objective

JAGUARETE KAA S.A. Wants to make a website to show off their products, taking adventage of the eCommerce system. 
Also responsive website.

## DB modeling: 

* Categories:
	* Description

* Products:
	* Title
	* Image
	* Description
	* Price
	* Category that belongs

* Cart:
	* User
	* List of products []
	* Total price of the cart

## Groups

* User: Can see the complete website except Add & Edit products page. Also can see the Cart page where its their cart information

* Moderator: Can see the whole website, but in the product page will see edit page and in the main page can see `Add Product Button` -> Where it will go to the Add product page
