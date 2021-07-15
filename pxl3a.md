# 07/13 | highdive

## rambles about jegan stock POST info , 2359

ok so what methods do i have / need to make

getStock()
	returns all

postProduct( name, materials[] )
	name
	ref( materials[].map(ea => postMaterial( ea, this.id )) )
	addQuantity( this.id )

postMaterial( name, productId )
	name
	ref( productId )
	quantity: addQuantity( this.id )

postStock( name, ref )
	name
	( ref.length === 1
		? ref( getIdByName( ref ) )
		: ref.map( ea => postStock( this.id ) )
	)
	quantity: addQuantity( this.id )

addQuantity( stockId, num )
	id
	ref( stockId )
	quantity( num || 0 )



























---

# 7/8 | redo costcoGas

## rambles , 1239

so i need to redo the todos

what do i need?

- server
- router
- data
- views

so i need to config typescript  
then set up koa for the server  
set up the routes  
and the api  
talk to the database  
queries are gonna be weird  
so are views  

