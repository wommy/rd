# jegs, wassup

so heres the email, heres what were gonna do

first keyterm: `Component`

components can be nested inside of others  
lets make some nested components: `List` & `List_Item`

the `List` creates `List_Item` s, based on an input  

heres an example from your etsy:
	
![nested list component](./imgs/gimp3-component-cropped.png)

``` js
// featured list with two objects
const featured = [
	{
		image: './lighter-pair.png',
		title: '2 Pack Art Lighters (choose your design...',
		price: 18,
		discount: .1,
		shipping: true,
	}, {
		image: './lighter-mushroom.png',
		title: 'Mushroom Lighter',
		price: 10,
		discount: .1,
		shipping: true,
	}
]

// give the List_Item a shape
const List_Item = ({ image, title, price, discount, shipping }) => `
	<List_Item>
		<img src=${image}/>
		<heading>${title}</heading>
		<div>${price*discount}</div>
		<div>${shipping}</div>
	</>
`

// iterates over List, applies shape to each data object
const List = data => List_Item(data) 

// outputs the above
export default = `<>
	<header>Featured items<header>
	${ List( featured ) }
</>`
```

i want to create two components: `List` and `List_Item`

what i need from you: 

- [ ] ListItem shape for example: ` List_Item: [ image, title, price ] `
- [ ] values for each of those properties



so what i need:

item schema:
