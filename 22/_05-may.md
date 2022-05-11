

































may
-

10 , fr r0y
--

1719 , eleventyFetch
---

1849 , fuggin incorrectly nested a ']'
---

1915 , spit-balling about pagination
---

so i think i need to split the array and rejoin it

so whats the schema shape

```
data = [
	2022[]:
		may[],
		apr[],
		mar[],
		feb[],
		jan[],
	2021[]
]
```

im going to need to write a script that accounts/adjusts for the `Z offset`
	big groan on that front


























9 , fr r0y
--

108 , still workin on marx
---

having cached queries should help alot
	i need a query for
		- [ ] last year: archive
		- [ ] this year
			- [ ] last quarter
			- [ ] this quarter

theres gonna be some weird magic im gonna have to do for it to build just right

	*[ _type == bookmark' && ( dateTime(_createdAt) < dateTime('2022-01-01T00:00:00Z') ) ]
	  | order(_createdAt desc)

`*[ _type == 'bookmark' `${ ? filter }`]`
		| order(_createdAt desc)


220 , volteer, dadChair
---

all im grabbin from sanity
- before this year
- before this month
- this month


1628 , to be 32
---















8 , fr r0y
--

229 , got alot done
---
just patched `powerline`? hope it holds

304 , added some more config
---
im workin on patching the sanity fetch to the 11ty fetch

657 , cleaning up tabs on fr4nk3n
---
once i get the marx up and running,
ooo-wee

so whats the plan
----

i gotta split marx into quarters, 21q1,2,3,4
split the quarters into months,
and the months into weeks

so i got my `_createdAt`
	i probably can turn the `datetime` into `Weeks`
	> `datetime` into `weeks`

> plug photos, mostly IG images


2008 , slept and awoke
---

so i gotta sort the marx by `datetime`












7 , fr r0y
--

1524 , splitting marx out of tudo
---

when i set up tudo, i was learning serverless
	just ported over basic express
	thats why i had 

just spent hours fixing dotfiles
----

2211 , getting back to it
---















5 , fr r0y
--


1957 , gotta twerk on marx
---
did a bunch of kukui ssh stuffs

2105 , ? mermaidJS NAH
---
workflow stuff is so hard, i dunno why

> what is it

i already have so much data,
	first list what i have

	```mermaid
	bMARXlet --> sanity

	```

sanity needs a better Vue,
	something i never set up

marx , 2119
----

- `GET`
- `POST`
- `PUT`
- `DEL`

2142 , made MARX in wmr
---

- [x] pathPrefix































2 , dadChair cy4n
--

0536 , havent slept
---

what am i doin

i fucked with `sway` for a few hours

fuggin `wayland` has snags,
	ie `x` is just so cooked into everything

---

2117 , setting up json-server
---

i need to 
	create an interface
	add to list bookmarklet
	couple different categories

later
	share menu mobile

i guess a server needs to run
	express? probs fastify

fastify specifically, is probs too much
	i dont need to learn another thing 
	i need to create a form 

which is nice because i pretty much set up the environment

001 , tmux rambles 
---

why is tmux so hard

145 , so hard? ha! i got it all working
---

i have no clue what i did

pm2 is such a hog

i do so much so often

> i just need to annotate it better

154 , brainstorming ON how to best log
---

thats what this whole thing is,
	a log

`this` is an entry on a log

all it needs is some BS `npx script`

> what is it named?

> what does it do?
> 	takes user input
> 	curls to an endpoint
> 		that means i need to set up an endpoint



```js 

```


it feels so nice to not be worried about constantly losing data , 0437
---

612 , think i got the nodecli fetch down
---

701 , thoughts
---
this should be the command
	`rd`

adds a new entry, `datetime`

but what i was really on

`rd`: a cli for GETs and POSTs
	it needs to be more cli
	maybe i could write straight json
	PUT will come down the line

	its like a weird logger
	it could be a tui

i guess i could ping my `yt-history`


741 , rambles
---

> logs are everything
>







---

1 , fr r0y
--

1510 , tudo
---

- [ ] wommy.io , wommy needs alot
	- [ ] new homepage
	- [ ] new nav
	- ¿ split each page into its own repo
		- [ ] monorepo

1733 , wom monorepo ( WMR ) , DONE
---

- .gitignore
	- node_modules
	- .pnpm-debug.log

- package.json
	- 

1757 , dotfiles , DONE
----

- nvim-nerdtree : default options = show hidden
- kitty.font : rm medium
- kitty.conf : fish & nvim
- rpi.fan : version X
- i3.conf: launch kitty into fish
- plug: gitgutter
- kitty.conf: bar to top

> feelsgoodman.gif

i needed to do alot of the above so that below works


1804 , wom monorepo ( WMR ) , DONE
---

> ok so where am i?


- package.json: {}
	- name
	- private: true
	- license: "Apache-2.0"

- pnpm-workspace.yaml
	- packages: []
		- pages/*

- .gitignore
	- node_modules
	- .pnpm-debug.log

- docs/
	- index

- pages/
	- index

1949 , wmr , done
---

- got 11ty workin

> whats next?

- content
- components

i cant seem to get workspaces working exactly how i like

it seems like the next `tudo` is `Rd`

2146 , brainstorm
---

> what do i need ,
> my problem comes from :

too many `youtube` videos

> solved by 

access from the `phone` during `drives`

---

i need a sort of shelf to store em

? is this where the `SQL` comes in?
	do i just use `json-server`

do i want to run a server process?
	i think id rather run `pm2`


























































