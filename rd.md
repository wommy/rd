# 02-17 | frontroom fr4nk3n

## continuing the technomad blog , 1517

i believe i last left off with the symlinking of the blog

separating the content and the build tool is important,  
it allows me to update the build tool separate from any site it powers  
also allowing me to create middleware per site basis,  

i just need to push some bullshit into the 11ty for rn,  
i can separate that shit out later

### taking longer than i thought , 1543

walking thru the 11ty starter, slapping em all in an 11ty/  
`mv $VAR /11ty`

### that took alot longer than i thought  , 1631

![its-working](https://i.giphy.com/media/BoBOKNtlR8rTi/giphy.webp)

---
# ---  
---
# ---  
---
# ---  
---
# ---  
---
# ---  
---

# 02-13 | frontroom fr4nk3n
## misc tasks, just opening this , 1810

set up the linode again
## todo , SSH scripts , scripts

i think im gonna fuck with this knexjs package,  
i do need to get jegan some shape, i could just slam thru all her objects  
strapi is just a react admin over knex and bookshelf,  
maybe poke at bookshelf for a few mins 

## todo , encrypted partition
## todo , nextcloud

so i think i need to go the sql route with keith,  
although i think the mongoose route offers some compromises

# 02-07 | frontroom fr4nk3n

## updating technomad.media

[its been a long time, i shouldnt have left you](https://www.youtube.com/watch?v=B8KNOTZRN4Q)

but srsly, lets [jack](https://www.youtube.com/watch?v=m0EiujcV3Tg)

so i know its been a long time,  
i guess i tried to make a post in sept, and in dec

##### im not trying to be a music blog, or am i?

## todo - dig up those posts 

### whats the actual move , 1620

so im glad i have all this context, i just need to make it somehow

i guess im going to use 11ty, i did just install it globally,  
which is a big honor, so thank you zach

the technomad-stack, or TMS is usually my spring point

##### [heres a banger from last night](https://www.youtube.com/watch?v=eL9_QYxvI5k)

i heard about this new internet protocol called gemini, i heard its like gopher
## todo - blog about setting it up

ok back to it, 

so im using a global install of //11ty.dev

so how do i want to export it?  
im thinking of making a public folder, that 11ty exports to  
visavis old apache

i just realized the other day that 11ty has a preconfigured server
theres so much server stuff that, once configured, would work
## todo , blog , 11ty mail server and serverless

### 11ty , 1637

whats 11ty's default template again?  
the generic theme

### found it //github.com/11ty/eleventy-base-blog , 1640

i think im just gonna use it

### its so hard to detail all the steps i just did , 1652

i cloned the site, with the //cli.github.com

and then pushed it to netlify with the //cli.netlify.com

now its live at //www-technomad-media-blog.netlify.app

## todo , DNS stuff for technomad.media

### so its up and live , 1655

### from thought about to published in < 20 mins

### put your own content on it , 1657

im so glad im typing this right now,  
because it gives me something to upload 

### symlink this folder to the blog somehow , 1659

so right not these two files are in two separate places,  
and thats actually a great thing

one of the mistakes of computing is putting things together

personally have had this happen to me

we gonna fix this with git submodules  
and i know thats a scary sentence, but trust me

### git submodules , 1703

- https://git-scm.com/book/en/v2/Git-Tools-Submodules
- https://www.atlassian.com/git/tutorials/git-submodule
- https://github.blog/2016-02-01-working-with-submodules/
- https://careerkarma.com/blog/git-submodules/

git submodules is the same as a sym link

i have a dotfile repo that i learned symlinking for  
https:/github.com/wommy/dotfiles#symbolic-links  
which in turn links to  
https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/#creating-symlinks-to-a-directory  
which details pointing to a directory, which is what we want for the blog too

### let get this working local , 1724 , taking a runto break 

# 02-07 | frontroom fr4nk3n

 ## learning react , 2013

  i need to start blogging again,  
 	aka i probably need to focus on publishing these

 	 	how to publish these
	
  ### todo , publish blog
  ### todo , learn fauna

## 2016 , building technomadmedia in react

interesting, should i publish the blog to fauna,  
i do want markdown but this might be a nice intermediary step,  
probably not the more i think about it

the blog shall be next

  ### todo , jegan react component
  ### todo , annabrabant.com

gotta type dunno about what

## TECHNOMADMEDIA IN REACT , 2035 

publish the old blog,  
i gotta dig it out the fucking graveyard  
thats later, first is just 

setting up a basic blog layout

its almost like i have a guide somewhere on how to do these things 

## 2110 ?	writing clients( anna, seamus, megan ).email
## 2134 ! completed anna , ? jegan next
## 2135 ? email jegan 

# 02-01 | frontroom fr4nk3n
 ### cacao tree mongo , 1357
 
 protein
  protein fuel
    blueberry, banana, almond mylk, almond butter, cinnamon, hemp protein, spirulina, date, maca, omega blend, kale
    10.50    
  post-workout protein
    banana, coconut mylk, ginger, tumeric, date, hemp protein, omega blend, cashew butter
    10.50
  high vibe
    banana, almond mylk, date, raw tahini, omega blend, spirulina, maca, romaine
    9.49
  breakfast blend
    banana, almond mylk, almond butter, cacao powder, omega blend, maca, romaine
    9.49
  spice of life
    banana, almond mylk, cacao power, cayenne, cinnamon, maca, date, omega blend, romaine
    10.50
  cold brew
    cold brew coffee, almond mylk, banana, cacao powder, cashew butter, date, omega blend
    10.50
  mango muscle
    mango, banana, almond mylk, tahini, cinnamon, maca, omega blend, brown rice protein, date
    10.50
 superfruit
  sunshine
  inner warmth
  ambrosia
  orange creamsicle
 green
  bee green
  on a beach n hawaii
  chia green
 elixirs
  root power
  refresh
  exhale
  i-thrive
  daily tonic
  
  ### 1527 ' megan stock
  
  ### 1546 ' netlify serverless

# 01-26 | frontroom fr4nk3n
## todo , 2041 , dillon site, blog conversations, dillion brooks
	### rambles , 2039

	it feels like forever since i typed in this,  

	i need to , added todo

	but i also need to get this serverless set up

	gotta set the axios up with 11ty,  
	thatll return me a data object,  
	write the list

# 01-17 | frontroom fr4nk3n
  ### keith sql, 1729
  
  wassup ladies n germs
  
  so ive been working with keith for a couple hours now,  
  im been working on my sql schema and data shape and all that
  
  i thought i should start writing here because  
  this might be better than that log

  ### 1900 ' quit restart , working with keith
  
  ### 1944 ' creating jegan-stock-log 

# 01-16 | frontroom fr4nk3n
  ### rambles , 2026

  how we do

  im watching the wings, they just scored,  
  im trying to get megan to help me model
  
  i just looked up some mongo bs  
  i know theyre lik ethe new rising company, but  
  i dont understand the void they fill,  
  i know that MySQL databases are a little too anal,  
  but i also know that most nosql databases resolve to sql
  
  
  im just curious about the arrangement,  
  i know postgres, PG is its own thing too,  
  
  i hate keiths tryton,  
  i need to be able to script everything,  
  
  speaking of, i have some written notes, pseudocode,  
  that i need to digitize, from memory:  
  
  - create database ,, username | jegan
  - create table ,, log
  - log 
    
  this is super weird because ive never done this before ' 2045
  
  what do i need to do,
  create a schema
  
  new schema
  add _id,
  ^= super schema
  super schema :: _id, createdAt
  
  ### 2123 ' watchin wings , wrote another dillion email
  
  these dillon emails need to be turned into blogposts  
  that selected individuals gets to comment on

  so whats the move
  
  set up a strapi,  
  link the backend to atlas,  
  invite dillon, keith, nessa, amit
  
  ### 2145 ' wings just scored , need to set up this strapi

  could run the mongo on my own server  
  need to look into express
  
  larkin scored

  logging this schema is needed,  
  if anything thats what i need to do
  
  setting up the blog is important too
  
  it could go either way, mongo or gSheets
  
  i like mongo's defaults, it would be great for a log
  
  i dunno why the log, feel fucked either way, might as well have it
  
  ### 2240 ' dooped around the house , watchin the preds

  thought id set up this stratlas
  
  ### 2251 ' setting up the stratlas

  i could point this at the linode EZPZ  
  thats a good feel, thanks keith
  
  new repo, stratlas

  ### 150 ' set up stratlas with .env , took fucking forever

  wrapping up
  
  i need to resend out invites
  
# 01-13 | frontroom fr4nk3n
### ramble , 1550 , from Moleskin

	whats the workflow i need

	- [ ] click a button
	- [ ] button triggers get()
	- [ ] get() returns promise of re-render

### how is this actually working , 1556

	11ty the build script

	when data runs, i want it to save the data to a file >> SEEDS  
	does that mean i want to seed? is seeding a step?

		? ask keith
	
### never ask keith , 1648

	so i create the schema,

	i just need to think functionally

		? tuskey

### wrote dillon email , 2015

	gonna eat, doubt ill be back


# 01-08

### frontroom fr4nk3n

	##### 1252

	so what am i doing

	#### sql serverless

	##### 1523

## set up bash alias mpv into dotfiles

	was trying to loop final frontier XD

# 01-04 - 

### frontroom fr4nk3n

  ##### 1457

  working on knex, sqlite3 junk

  i should just do the pg tutorial shit

  ##### 1933

  watching some trumpy news

  did the knex, got maria set up  

		? ask keith
	
### never ask keith , 1648

	so i create the schema,

	i just need to think functionally

		? tuskey

### wrote dillon email , 2015

	gonna eat, doubt ill be back


# 01-08

### frontroom fr4nk3n

	##### 1252

	so what am i doing

	#### sql serverless

	##### 1523

## set up bash alias mpv into dotfiles

	was trying to loop final frontier XD

# 01-04 - 

### frontroom fr4nk3n

  ##### 1457

  working on knex, sqlite3 junk

  i should just do the pg tutorial shit

  ##### 1933

  watching some trumpy news

  did the knex, got maria set up  
  got workbench to output the ERD

# 2021 - 01 - 04

### frontroom franken

  ##### 1606

  new year!  
  guess i should blob a little  
  melissa talked to me a little bit  
  it was nice, even tho her nastiness shone thru

  ## TODO ' 5th.dim.det form

  ## TODO ' music page , submodule

  what would a music page entail

  it would legit be a CMS because i'd just push to an endpoint

  saving a commit, 

  it would be that atlas endpoint?

  i wanna just echo and add a line of text

  i gotta see if that mongo is fast enough

  and then i just need to do some serverless

  as if thats so hard, HA

  i could just do a sqlite3 db with strapi on the linode

    remember 5thdimdet form
    maybe this first
  
  the music page would be same as the todo page  
  just a different category

  the sql db needs to go up first

  a netlify form could be quick or not,  
  if i snag, ill swap

  ## 5th dimension DET form

  #### how 2 start

  clone a repo



  ## update stack for vue
  
  ##### 1635

  this should be easy  
  i already have that other repo for it

  ##### 1652

  looks like i have 2 branches across 3 repos  
  @_@

  ##### 1833

  ' i did mom jump on the compy and then ky called

  gotta look up the next mailchimp thang

  ##### 1901

  FOUND IT

  ##### 2003

  cleaned up brave backup  
  bunch of other bookmark junk

  ##### 2009

  ## linode w/ keith, strapi

  ##### 2034

  got keiths key working, i believe  
  https://www.linode.com/docs/guides/use-public-key-authentication-with-ssh/

  
  ## start strapi

  ##### 026

  got strapi all set up, incl dev server

# 12-28 | blogpost - olde 2 vue

### frontroom fr4nk3n

  ##### 1409

  yup so here it goes

  i guess im porting olde 2 vue

    whats the first step?
  
  im trying not to fork repos, instead import em

  so im guessing that?

  ##### 1455

  ive been in a loop  
  whats the structure?

    i think i need to 
  
  - [ ] put 11ty-vue into TMS
  - [ ] start a template from that
  - [ ] ? somehow push that to technomad olde

  here goes nothing
  
  ##### 1503
  
    ^ this might be next, i just wanna build olde rn
    ? how do i do that
  
  new branch? probably bad moves

  ##### 1509 ' this feels so wrong

  ##### 1520

  so i finally got something up  

  ##### 1539

  i dont think moving off olde-v0 is the truth,  
  i think i do alot of cleanup in v1

  ##### 1603

  i have no clue what im doing wrong here  
  11ty vue just isnt compiling how i thought it would

  do i type it in by hand?  
  thats pretty much always a stupid move

  ##### 2218

  did most of the vue docs  
  still need to figure out 

  ##### 2227

  just talked to kels, lil of vanrych

  the vue lesson was very weird today,  
  im trying to do olde in vue  
  or olde 2 vue

  ##### 2307 

  so i dicked around this repo:
  https://github.com/wommy/olde-vue-11ty

    post which articles i followed


  

# 12-18 | blogpost - rambles

  ##### 1531

  so im super glad i fucked with sanity,  
  for a second there, i thought i was gonna regret passing on it

  im feelin big weird

  i do think that sanity is too much

  remapping a single thing like how the listitem displays is a bitch  
  you have to build that yourself  

  plus its all going to their server  
  huge no

  i instead think focus needs to fall on making strapi ez-pz

  if we could make a good component workflow,  
  then we could build our own sanity-like frontend

    build own sanity workflow

  ? buttercms  
  ^ HA! their pricing, still!

  ##### 1549

	we need to build the components

	##### 1601
	
	whats the move here  
	we need to build the components

	react is sweet and all,  
	but if you can create vanilla components, thats where the moneys at

	jesus

	i think mongos good too

	it cant be that hard to run

# 12-17 | 

### frontroom fr4nk3n

  ##### 1850

  #### rambles

  starting up i guess

  i think the real move is that 11ty starter,  
  i guess you can that jstl.11ty.js

  i gotta have the build 

# 12-14 | creating a basic theme 2

### jujuroom fr4nk3n

  ##### 1332 
  
  #### rambles

  didnt get anything materially done last time  
  wanna try out awesome  
  gotta figure out polybar and rofi  
  thatll take way too long

  guess im making this theme

  ##### 1336 

  #### whats the first step

    ? new technomad
    ? system links

  so im looking at minima, jekyll base theme

    ? list = page template

  ##### 1346

  new repo /technomad-theme from TMS

  ##### 1355

  am i really using parcel?

  ##### 1412

  i think im using parcel  

  just gonna try this new thing before i go back to 11ty

  probably should work on anna

  google sheets api

  maybe with parcel

  ##### 1421 

  im going thru like three waves:

  1. rofi / polybar
  2. parcel

  ##### 1733 ' i guess ive been doopin

	- [x] fucked with a bunch of WMs, rofi
	- [x] bookmark stuffs NTP

	- [ ] parcel  
  - [ ] strapi + 11ty

  ##### 2227 ' got mr kabob
  
  - [ ] how did i get into libreoffice base


# 12-12 | creating a basic theme

## jujuroom fr4nk3n

  ### 2249 

  still digging this new workflow  
  hopefully this never gets old

  already have some TODOS

  ## todo - shelfed - later

  - [ ] make blogpost from last rd post

  ^ this looks like shit, how do i fix?

  anyway,  
  if i want to splice off a chunk of the rd,
  i need to do diz: https://devblogs.microsoft.com/oldnewthing/20190919-00/?p=102904

  i dont think i have the balls to do that right now  
  how do i shelf? 

  hopefully that works

  whats the real focus

  ### 2253 ' sometimes im a g

  - https://github.com/wommy/technomad_blog/tree/feature/building_blogposts_with_11ty
  - https://github.com/wommy/technomad_blogposts

  first thing i noticed right away is that _blog is in a feature branch, which while progressive, the master is blank,  
  so lets fix that

    ? mv _blog/feature => _blog/master

  we are also going to do something with the old blogposts

    ? mv to rd

  lastly, 
  
    combine _blog & -blog
  
  dunno how to do this, gonna have to think on this for a bit

  ## 1841 ' later

  - [ ] cleanup projects_current

  ### 1851

  - [x] tm_blog feat => master

  ### 1854

  so what im seeing is  
  i have four repos open:
  - https://github.com/wommy/technomad-blog
  - https://github.com/wommy/technomad_blog
  - https://github.com/wommy/technomad_blogposts
  - https://github.com/wommy/rd

  how these are going to combine is  
  right now, _blogposts is a submodule of _blog  
  i need to move that to and replace it with rd

  -blog is mostly up to date, need to replace /content w/ /rd

  #### how does this really work:  

  -blog is newer _blog  
  rd is newer _blogposts, which is /content in -blog

  - [ ] _blogposts => rd
  - [ ] rd => -blog
  - [ ] -blog => _blog

  ### 1927 _blogposts => rd

  im struggling with this because its not really a normal operation  
  i need to break it down into simpler steps

  currently im referencing: https://github.community/t/adding-a-folder-from-one-repo-to-another/781/2
  
  ### 1949

  i think i instead want to use https://gist.github.com/smdabdoub/17065c348289158277b5

  ### 2117 ' IT WORKED








# 12-02

## 2243 ' workin at ky's

  did a few things
  - [x] i3 config
    - [x] reduced gaps
    - [x] reduced resize
    - [x] system linked
    - [x] dotfiles
  - [x] dracula theme
  - [x] removed extensions

  tryna figure out what to do next


# 11-24
  - [ ] lukesmith mail server

  ## hard rambles
  - [ ] raspi > roy spot
  - [ ] backup roy

  ## 1635 microcenter
  - [ ] raspi4 ' explaining computers FOR kit with cooler

  ## 1655 ' tasks were always right
  - [x] change i3-gaps scratchpad 
  
  ## 1707 ' sometimes its nice to write a quick note
  im really trying to come up with the right ways to use each medium, digital analog computer notebook, i feel like its hard

# 11-23 

  i spend all this fucking time doing nothing all the time

  ## 1630 some todos
  i just wanna type  
  am i writing too much?  
  shouldnt i just be writing all my blogshit in one file?  

    ? isnt that the whole point of rd
    
  - [x] write in one file ' im so confused

  - [ ] hotkeys

  ## 1700
  need to work on alot of stuffs

  ## 1711
  this is why we just learn how to type faster  
  this is supposed to be some type of idea board right?

    ? toml

  ## 1744 ' big nope to .toml
  - [ ] shift focus to the blog

  ## 1753
  - [ ] write a script to functionally process this
  - [ ] trackdown all my blogs

  ## 1840
  - [ ] setup netlify

# 09-30
  ## call
  - [x] joliet
  - [x] obriens
  
  ## errands
  - [x] bike <= stavi
  - [ ] 1TB @microcenter

# 09-25
  - [ ] write component for video embed, yt
  - [x] alias nvim

  - [x] hit up @renzo about xampp and php

  - [x] syslink nvim dotfiles

  - [x] cleanup repo /dotfiles master branch
  - [x] renamed old repo, created new
  
  - [ ] fixup old dotfiles repo, integrate new
