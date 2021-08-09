# rd

---

## 08/09 | dadChair

### 1510 , jeganmones sanity v2

soooooooo whats the fix

this is gonna be long and detailed

1. spin up a new sanity
2. model content <= DOOZY

```js
{
	type: 'document',
	name: 'art',
	fields: [
		{ type:'string', name:'name' },
		{ type:'image', name:'image' },
	]
}
```

### 1634 , schema round 2

so art has a type of document

	











---

## 08/07 | dadChair

### 2239 , jeganmones is now on sanity

my god this has been a long time in the making

it still needs some work tho

### jeganmones squarespace site layout

/
	/components
		header
			nav
				Home
				Shop
				Collabs
				Contact
			h1
				.siteTitle
			nav
				ig
				cart
		footer
			form-newsletter
			email-me
			follow-me

Pages
	index
		fold-1
			callToAction
				.siteTitle
				.siteSubTitle
				btn -> /shop
			img
		fold-2
			hero
		fold-3
			featured
		fold-4
			about
		fold-5
			involved
				blm
				lgbtq
				nature
	merch
		h3 pageTitle
		main
			aside nav filters
			art-list.3col
				art-card
					art.img
						?> figcaption
						.hover 
							transition2 2nd img
							quick-view
								dialog / modal
									next/prev
					art.title
					art.price
			footer
				CTA show on etsy
	collabs
		CTA collab
		list
			published work
			daughters of darkness
			bratbox
			sisterepic
			put art on billboards
			tripleaaanimals
			boop my nose
			tattoos
	contact
		fold-1
			details
				.title
				.subtitle
			img
		fold-2
			form
	cart
		!cart 

	TODO: mobile this ^












---

## 08/02 | auntSams

### 1736 , rambles

so what am i getting into here 

think im gonna go over the old redis stuff a lil

- [tm redis in node](https://www.youtube.com/watch?v=oaJq1mQ3dFI0)
- [tm redis](https://www.youtube.com/watch?v=Hbt56gFj998)
- [redis: ioredis](https://www.youtube.com/watch?v=H6rikGCYPUk)
- [ben: redis + graphql node](https://www.youtube.com/watch?v=_Zwqn7FV6ms)

this is what i want to work on

### 2045 , finished ben's redis and graphql

took lots of fudging,  
- removed express
- swapped ioredis for node-redis
- probably more










---





















## 7/30 | dad chair | 2223 | rambles

oh man im having a bunch of weird feels rn

im glad i wrote that blogpost yesterday,  
going to aunt sams, just the whole thing was great

### fixed a bunch of junk | 2254

i feel alot better

i finally got to a bunch of things ive been putting off forever

so strange how a little accomplishment can breathe momentum

, im gonna smoke

### gonna buy this yubikey , 2304

### fuckin wit redis , 029





---












# 07/29 | aunt sams

## 1620 , warming up

- TODO building rd in strapi

## 1723 , setting up 11ty and nginx

- changed nginx config  

- `/etc/nginx/sites-available/technomad`

- |
```
server { 
-	root	/???
+	root	/srv/technomad
+	location /todo/ {}
```

- `sudo yarn build --output /srv/technomad/todo`

























---

















# 07/13 | dadchair

## 2108 , conceptualizing strapi routes?

so i need to figure out the methods for strapi

so i need to GET / stocks  
what do i display?  
is that the dashboard?  

list of all stock

i think im gonna piggie-back some 11ty on this


































---

# 07/09 | backyard

## rambles , 1920

so here i am in the backyard

what am i doing exactly

i set up nerdtree, thats nice

im going to git mv rename rd's 

### did that, got a lost in loop , 2114



























---

# 06-25 | great_room
## 2309 , jegan stock sqlite

ok so keiths a butthole  
viewing this file sucks too  
onto it

---

---

---

---

---

---

---

---

# 06-18 | jujuroom 

## resume/FMR , 1647

so what am i doing

so i did a first draft of FMR,  
ill push that now

so what do i need to do to pushit

### pushed , 1839

what did i want to do next?  
i think it was set up tailwind to do sanitize

or add my experience to resume

### 2008 , added resume-md

gonna quick restart

---

# 06-11 | cy4n kyleKeeler

### 1406 , gonna blast this chromebook

made cy4n folder in brave, waiting for the sync

https://docs.google.com/document/d/1lTWTJFa_Bsyht3WY0tuzImyIbXGu0Ri3z6GmGg6Pr_Q/edit

---

# 06-09 | cy4n drewKeystone

## 1628 , setting up cy4n, install

- [x] zsh
- [x] tmux
- [x] neovim
- [x] powerline
- [x] brave-browser-beta
- [x] gh
- [x] yarn

---

# 06-04 | cy4n drewsKeystone

### 1411 , working on settecase site
