# fr4nk3n
















---

## 08/20 | jujuroom

### 1456 , westmenu

sooooo

im working on the west menu

what are the problems im having

### 1717 , just pushed something

gonna do another pass,  
taking some notes
















---

## 08/17 | jujuroom

### 1858 , misc rambles

so what am i starting on

guess im looking at west-menu

i think im gonna branch it

### 1925 , some remarks on TMS

#### i think i need to write this down

so  
how does TMS work  
right now,

i clone over the src from root into the tms/src

i thought TMS's src was 11ty,  
im afraid to check how old the tms version is

maybe i should charge into that

### 2019 ,

the more i look into it,  
it seems like alot of kinda fucked

### 2115 ,

all the overhead for TMS is ridiculous

### 2124 , sanity

so im setting up a sanity for it

looks like i need a

```
meta
---
starters
sandwiches
salads/wraps
pizza
```

### 2337 , finished west menu port to sanity

going to highdive

---

## 08/13 | jujuroom

### 1422 , reference-able rsync

- [Rsync#Full_system_backup](https://wiki.archlinux.org/title/Rsync#Full_system_backup)

ran this,  
`rsync -aAXHv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} / /path/to/backup`

split my backups into...  

- Documents/
- w0m/ --exclude=Documents
- / --exclude=home/+list mentioned above

now i need to move those two other files back

rsync'd 20-10-05/w0m with same command

this feels longer than the root / one

i need some sane defaults to exclude stuff like

- node_modules
- cache

SO MUCH FASTER

`sudo du -sh */`

8.3G vs 4.3G 

`sudo rsync -aAXHv --exclude={"*/node_modules/*","*/.cache/*"} / /path/to/backup`

turns out i excluded node_modules from the 20-12-24 one,  
im guessing .cache will help going forward,  
maybe even a `*/cache/*` | `*/Cache/*` | `*/^cache$/*`  
i should learn regex

`sudo rsync -aAXHv --exclude={"*/node_modules/*","*/.cache/*","/.cache/","*/cache/*","*/Cache/*"} / /path/to/backup`

^ this cut 20G off my home/  
2/3  
66%

without that excludes, home is 270% larger,  
christ

really need to learn regex

other links
- [https://docs.npmjs.com/cli/v7/commands/npm-cache](https://docs.npmjs.com/cli/v7/commands/npm-cache)
- [https://superuser.com/questions/171534/list-the-current-folder-folders-sizes-with-the-terminal](https://superuser.com/questions/171534/list-the-current-folder-folders-sizes-with-the-terminal)

---

## 08/12 | jujuroom

### 1457 , i think all of yesterday got derped

this is like the hundredth time

### 1527 , started to open anna/ back up

### 2110 , switched anna to sanity

wtf went on in there @_@ :P

### 2152 , cleaning tabs up

---

## 08/10 | annabrab => sanity

### 1712 , holy shit

so little recap

anna updated her forestry files 9 days ago,  
and she borked everything

so a little more diggin,

i have that anna-redo that i did right before i got my tooth knocked out

i need to figure out how to get it to work with the submodule,  
it shouldnt be that hard,  
just some npm scripts?  
whats that one that one that i had to learn for the travmed course?

[shelljs](https://github.com/wommy/technomad-express/blob/dev/package.json#L22)

i have some more ideas,  

i thought i set up a client folder for working with tms

```
client/
	_data/
	_components/
		_html5
		_page
		_post
		header
	_pages/
		default/
			
```

more on this later

### 1839 , 

i think i need to get that shx working

does there need to be two commands?  
an import to tms,
and export from tms

anyway i just need to see how much is working currently

---

## 08/09 | jujuroom

### 0959 , jegan layout

just writing some rambles here

i should reference that blogpost

### 1044 , jegan stuffs

so i need to model the data,  
i might just do that here

soooo

Art/
	bondage bear
	shoe
		flamers
		ruffle socks
		butterfly
		leg & boot
	cow
		regular
		chocolate
		strawberry
		blueberry
	lava shroom
	my plants wear leather
		white
		with words
	lust
	dont be a dick
	zodiac
		aries
		taurus
		gemini
		cancer
		leo
		virgo
		libra
		scorpio
		sagittarius
		capricorn
		aquarius
		pisces
	led zeppelin
		black
		white
	rainbow penis
		white
		rainbow
	skull cone
	horny
	praise me
	play with me
	devil inside
	vibin
	crown of death
	dead inside
	skull flame
	cumfort me
	live delicously
	lit
	be nice of leaf
	spooky smoke
	flowers grow
	witchy crystal
	deadly flutter
	light me up
	skull plant
		black
		white
	mushroom
		booty
		booty + titty
		titty

Merch/
	lighters
		shoe
			flamers
			ruffle socks
			butterfly
			leg & boot
		cow
			regular
			chocolate
			strawberry
			blueberry
		lava shroom
		my plants wear leather
			white
			with words
		lust
		dont be a dick
		zodiac
			aries
			taurus
			gemini
			cancer
			leo
			virgo
			libra
			scorpio
			sagittarius
			capricorn
			aquarius
			pisces
		led zeppelin
			black
			white
		rainbow penis
			white
			rainbow
		skull cone
		horny
		praise me
		play with me
		devil inside
		vibin
		crown of death
		dead inside
		skull flame
		cumfort me
		live delicously
		lit
		be nice of leaf
		spooky smoke
		flowers grow
		witchy crystal
		deadly flutter
		light me up
		skull plant
			black
			white
		mushroom
			booty
			booty + titty
			titty
	art print
		size
			11x17
			8.5x11
			4x6
		1-38 + zodiac
	custom portrait
		type
			pet
			nude
			art
		color
			black
			white
			shapes
		size
			11x17
			8.5x11
			4x6
	misc
		sticker
			deadly flutter
			cumfort me
			my plants wear leather
			live deliciously
			play with me
			skull plant
		keychain
			mushroom
		tattoo
			bondage bear
		pin
			deadly flutter
		patch
			deadly flutter
		candle
			1-35 + zodiac
	Rebels
		tattoo design
		custom lighter case + matching art lighter
		lighter case + matching art lighter
			light me up
			horny
			mushroom
			live deliciously
			devil inside
			cumfort me
			be nice or leaf
			praise me
		custom nude lighter
		3 mushroom lighters + sticker set
		lighter wrap
			1-26
			zodiac
		mushroom keychain
		Art Print
			11x17
			1-38 + zodiac
		custom portrait lighter
		2 pack mystery lighters

### 1154 , breakpoint, some thoughts

so the original idea to move stuff into art was genius,  
im going to do one more pass to tighten it up, (titanup)

Merch/
	misc
		tattoo
			bondage bear
		keychain
			mushroom
		sticker
			deadly flutter
			cumfort me
			my plants wear leather
			live deliciously
			play with me
			skull plant
		candle
			1-35 + zodiac
		pin
			deadly flutter
		patch
			deadly flutter
	art print
		size
			11x17
			8.5x11
			4x6
		1-38 + zodiac
	Custom
		custon art lighter + case
		custom lighter
			portrait
			nude
			pet
		tattoo design
		custom portrait
			type
				pet
				nude
				art
			color
				black
				white
				shapes
			size
				11x17
				8.5x11
				4x6
	Rebels
		art lighter + case
			light me up
			horny
			mushroom
			live deliciously
			devil inside
			cumfort me
			be nice or leaf
			praise me
		mushroom set, 3 lighters + sticker
		lighter wrap
			1-26 + zodiac
		2 pack mystery lighters
	lighters
		shoe
			flamers
			ruffle socks
			butterfly
			leg & boot
		cow
			regular
			chocolate
			strawberry
			blueberry
		lava shroom
		my plants wear leather
			white
			with words
		lust
		dont be a dick
		zodiac
			aries
			taurus
			gemini
			cancer
			leo
			virgo
			libra
			scorpio
			sagittarius
			capricorn
			aquarius
			pisces
		led zeppelin
			black
			white
		rainbow penis
			white
			rainbow
		skull cone
		horny
		praise me
		play with me
		devil inside
		vibin
		crown of death
		dead inside
		skull flame
		cumfort me
		live delicously
		lit
		be nice of leaf
		spooky smoke
		flowers grow
		witchy crystal
		deadly flutter
		light me up
		skull plant
			black
			white
		mushroom
			booty
			booty + titty
			titty

### 1228 ,

ok so now im gonna try to tackle it from the art perspective

Art/
	bondage bear
		tattoo
	shoe
		flamers
			lighter
		ruffle socks
			lighter
		butterfly
			lighter
		leg & boot
			lighter
	cow
		regular
			lighter
		chocolate
			lighter
		strawberry
			lighter
		blueberry
			lighter
	lava shroom
		lighter
	light me up
		art lighter + case
	horny
		art lighter + case
	mushroom
		booty
			lighter
		booty + titty
			lighter
		titty
			art lighter + case
			lighter
	live deliciously
		art lighter + case
	devil inside
		art lighter + case
	cumfort me
		art lighter + case
	be nice or leaf
		art lighter + case
	praise me
		art lighter + case
	mushroom
		set, 3 lighters + sticker
		keychain
	my plants wear leather
		white
			lighter
		with words
			lighter
	deadly flutter
		sticker
		pin
		patch
	cumfort me
		sticker
	my plants wear leather
		sticker
	live deliciously
		sticker
	play with me
		sticker
	skull plant
		sticker
	lust
		lighter
	dont be a dick
		lighter
	zodiac
		aries
			lighter
		taurus
			lighter
		gemini
			lighter
		cancer
			lighter
		leo
			lighter
		virgo
			lighter
		libra
			lighter
		scorpio
			lighter
		sagittarius
			lighter
		capricorn
			lighter
		aquarius
			lighter
		pisces
			lighter
	led zeppelin
		black
			lighter
		white
			lighter
	rainbow penis
		white
			lighter
		rainbow
			lighter
	skull cone
		lighter
	horny
		lighter
	praise me
		lighter
	play with me
		lighter
	devil inside
		lighter
	vibin
		lighter
	crown of death
		lighter
	dead inside
		lighter
	skull flame
		lighter
	cumfort me
		lighter
	live delicously
		lighter
	lit
		lighter
	be nice of leaf
		lighter
	spooky smoke
		lighter
	flowers grow
		lighter
	witchy crystal
		lighter
	deadly flutter
		lighter
	light me up
		lighter
	skull plant
		black
			lighter
		white
			lighter
	

	?
		lighter wrap
			1-26 + zodiac
		art print
			11x17
			4x6
			8.5x11
		candle
			1-35 + zodiac


	??
		2 pack mystery lighters


	custom
		lighter & case
		tattoo
		nude lighter
		portrait
			pet
			nude
			art portrait

	misc
	Custom
		custom lighter
			portrait
			pet
	Rebels
	
### 1316 , ok im going crazy, switching to Moleskin

---

## 08/07 | jujuroom

### 1501 , rambles

what to write..

im watching some sanity videos

---

## 08/06 | jujuroom 

### all my shit from yesterday got deleted somehow , 1153

gonna disable my todo buttons

### 1237 , got that done, gotta merge it now

### 1400 , merged it, dunno what to do now

### 1544 , sanity todo

---

## 08/02 | jujuroom

### rambles , 1245

so i think imma start 11ty from scratch 

i need to focus on the possibility of publishing these

### new project

`mkdir $1; cd $1; git init; gh repo create`
`echo '# $1' >> README.md`
`git add .; git commit -m 'init: readme'; git push -u origin dev`

### 11ty from scratch , 1305

---

# 07/19 | jujuroom

## rambles, 1318

### combining the todo APIs

so what does i need todo

## 1537 , DONE

- quick strapi todo
- alpine fetch

### alpine post

## 2030 , did so much

---

# 07/15 | jujuroom

## 1601 , jegan store

soooooooooo, whats up

im trying to work on my filter method

i need to create like a little mini nav that changes display state by filtering results

so what do i need

i need to create a project


im already thinking of all these events, im glad i spent the time

---

# 7/13 | jujuroom

## misc rambles , 1455

think im gonna cue up strapi 

## mike call , 1627

- wireframe
- set up a call

allows me to work on something

from mike,  
- similar websites
- payments

models  
- Login  
- User - stored on your end

put the catalog up  
- less than 100 products  

catalog  
- product categories
- products
- details
	- id
	- quantity
	- weight
	- shipping

views  
- homepage
- login
- catalog
- product page
- add form to cart
- cart
- cart => Order database
- Order schema  

APIs  

---

- homepage
- login
	- createUser
	- authenticateUser
- catalog list
	- filterByCategory
- catalog item
- item page
	- item metaData
		- name
		- picture
		- price
		- quantity
	- addToCart form
		- quantity
- User.Cart
	- display cart items
	- addOrder form
		- payments
			- credit card
			- crypto
				- bitcoin
				- eth
				- USDC
				- monero

loose categories
- seeds
- clones
- brand

---

routes / pages
- home
	- product
- login
- user
	- cart

methods / functions / interactivity
- User
	- .create
	- .authenticate
- User.authenticated
	- Details
		- .name
		- .address
		- .paymentMethod
	- Cart
		- .submitOrder
- Catalog
	- .filterByCategory
	- Product
		- .addToCart( quantity )

---
end mike
---

## strapi setup , 1704

---

# 7/12 | jujuroom

## fixed up some startup scripts , 1321

gotta start on some jegan

### jegan stock - linode, tskoalite

### cleaned up ts-koa-lite , 1407

gonna finish that tho, get those jegan defaults in there

### having trouble with naming and placing , 1415

so im running into the same problem as tms,  
which is some type of versioning, includes problem  
template dir or submodule

think im gonna break on it 

### back , 1435

hit up keith on signal

## megan sql

## got a working copy up , 1633

gonna break

### back , 1644

## tryna clean some yt tabs , 2130

i guess i got alot done today

i would like to take some time to think outloud about some things

fuggin clipboard isnt working on server Q_Q

---

# 7/7 | jujuroom 

## starting , 1313

just talked to rian for 2 hours,  
shes a cutie but whoa

N E WAY

did dentist form, getting to work

## traversy media mongoose oauth , 1355

## recipe instapot fajita , 1507

## ate, back on mongoose oauth , 1549

## got dotenv to work after hours , 1744

---

# 7/6 | jujuroom

## 1244 , tm-todo filter

ok so what am i doing

i want to create a filter on my todos

### 1316 , been cleaning up my tmux, wip

### 1344 , didnt think id be editing my .config/i3

### 1415 , hostname rd

### 1624 , cant get njk to work

### 1644 , tryna commit and push exphbs

### 1754 , watched some vids on vim

