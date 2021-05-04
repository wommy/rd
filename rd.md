# 5-4 | fr4nk3n kycp topOstairs



---

---

---

---

---

---

---

---

---

---

---

---

---

# 5-3 | fr4nk3n kycp topOstairs

### rambles , 1256
just starting up, i think im gonna do some wommy

### pomodoro , 1321
finished putting up the repo, tryna install tms now

### pomodoro , 1351
setting up _Pages.json

### pomodoro , 1416

- got _data/nav to work with _com/Header.html
- added _Pages/ [ resume, repos, blog ]

gonna dart on break

### pomodoro , 1456
making blog dir structure

### pomodoro , 1523
creating article border, focus state

### got `:target` to work, 1541

### think i got tailwind.config working , 1603
### jk, long break , 1621

### still cant get it, 1702

### fixed it, 11ty delay, tailwind after 11ty in script , 1807

### back from kungfu , 2055

11ty plugin navigation

### moving dirs , 2120

### at a fork , 2153

so i can either do 11ty plugin nav or pagination

### chose plugin nav , 2205

### stuck on ? calling it , 2231

### took it slow, got something working , 2257

### working on styling the nav , 2323

### finished nav as much as i want , 2343

### pagination , 025

### blog.11ty.js , 055

this sucks,  
but im growing and learning

### getting blog.11ty.js permalink , 121

### stuck on this fuckin js , 146

### got it , 213

---

# 4-30 | fr4nk3n kycp topOstairs

### rambles , 2105

starting a pomodoro  
gotta start using this more,  
the other day when i got lost in the json, that was not fun

using this first one to figure out what im gonna do,  
need to finish some tabs, its like half organized

found my two work panes

### checking in , 2129

so im working on some panes, watching videos

checking out some 11ty junk

gonna keep rollin

#### 11ty --incremental build, 2145

trying it meow

#### break , 2200

think i ran yarn run build from the parent, and fucked my work  
Q_Q

#### gonna try to fix it , 2205

#### never pushed new tomate , 2215

maybe pivot a second and do some project dependencies

#### break , 2235

emailing luke

#### texting keith, 2255

#### looking over 11ty docs , 2222

#### still going , 2231

#### break , 2357

#### what2do in next tomate , 005

#### reading davidkpianos state machine medium posts , 041

#### im so tired , 115

tasks ~> task

---

# 04-29 | fr4nk3n kycp topOstairs

### rambles , 1335

didnt really get much done yesterday,  
well i did but it was mostly configs or something  
got tms set up on wommy/resume  
still would like to split that out

maybe i should do that now

## split out wommy/resume

### , 1659

dicked around trying to get tasks out of phone  
fuck regex  
fuck their export

whats next

i was cleaning tabs

---

# 04-28 | fr4nk3n kycp topstairs

### rambles, starting , 1200

ok so i kinda wanna start with resume,  
i need to start working on wommy

gonna try to cleanup some taskwarrior shit first

### finished the tomas babej video , 1334

gonna try to hit the wommy resume rn

## wommy/resume 

first i need to open it up

### update , 1431

stuffs going well,  
i pushed old changes,  
updated tms,  

working on finalizing template changes

### finished template , 1508

what TODO now

### what TODO , 1704

just derped for like an hour

### some notes on resume , 1705

so i replaces the old nav with the resume-nav  
still need to style it correctly

i need to replace it section by section

  contact
  education
  experience
    design
    development
    deployment
    other
  hobbies
  
it seems like i just need to start from scratch  
Q_Q

like how i did with WestMenu

  contact
    portfolio
    email
    4yrGoal
  
  edu
    depaul
    columbia
  
  exp
    solution people
    branding
    clients
      ? github/repos
  
  skills
    design
      figma
    development
      frontend
        html
        css
        js
      backend
        node
          tms
            11ty
            tailwind
          lesser:
            webpack
        lesser:
          ruby
          php
          python
    database
      json, yaml
        mongo
      lesser:
        sql: mysql, pg
    deployment
      netlify + github
    other
      linux, unix
        vim
      psych
  
  hobbies
    cycling
    martial arts
    techno
  
  --- redo
  
  about <~ contact
    portfolio:
      wommy.io
      technomad.media
    email:
      tom@technomad.media
    education:
      depaul, columbia
        psych, interactive media
    hobbies
    goal: ?

  experience
    freelance full-time since 2013
    github/repos
  
  skills
    frontend
      design, ui/ux
    backend
      db
      build/deploy
    computing

### pushd popd , 2118

---
    
# 04-26 | fr4nk3n kycp topstairs

### rambles, cleaning up tabs , 1812

got back from the doctor, got antibiotics  
not feeling so hot

i have so many things to do, per usual

just watching youtube vids because its low brain power

i want to improve the west menu,  
i do think i need to create a paired shortcode

## DONE , 1900
- [x] west-menu TODO s ~> issues

### TODO , 1908
- [ ] west-menu

### stuck in WestMenu, changing gears , 2032

dunno really what to do

---

# 04-21 | fr4nk3n kycp topstairs

### WoN menu rambles , 1605

yup so im just jotting some notes about the won menu

- [x] fix header , ? west image
- [x] icons for maps , phone
- [x] 2 cols for menu
- [x] menu section, top section for food notes
- [x] addons
- [x] west friends
- [x] specials
- [x] flex layout for menuItem , $ , price
  
---

# 04-06 | frontroom fr4nk3n

### rambles , 1253

so keith asked me to spin up a quick page for that automotive  
which got me working on TMS

i think i know what i need to do, it all has to do with versioning,  
i think i want to rebase from root  
which is the scariest sentence, lowkey

if i did that how would i do it?

### rebase --root , 1255

fork , total commits: 45

01 - git init  
  readme  
  yarn add 11ty,  
    package.json  
    yarn.lock  
    gitignore  
  index  

02 - html ~> pug  
  index .html ~>  
    _blank  
    _template  
    index.pug  

03 - ver bump, -D ~> -S

04 - 0.0.1  
  package.json

05 -  
  readme  
  package.json

06 -  
  .eleventy.js  
  _includes/  
    _blank  
    _template  
  index  
  init.sh  
  package.json  
  views/  
    _includes/  
      _critical.css

07 - 0.0.2  
  package.json

08 - technomad-cms

09 - 0.1.0  
  package.json  
    yarn.lock  
  views/_inc/_template  

10 - netlifycms core  
  gitignore  
  admin/  
    config.yml  
    index.html  
  package.json  
    yarn.lock  

11 - basic 11ty  
  eleventy.js  
    .gitignore  
    package.json  
      yarn.lock
  admin/  
    config.yml
    index  
  views/  
    index

12 -  
  eleventy.js  
  admin/  
    config.yml  
  views/  
    index.md  
    _inc/  
      _template

13 - 
  .eleventy.js  
    package.json  
      yarn.lock
  views/  
    _includes/  
      _template  
      post  
    index  
    tm_blogposts/

14 - 0.2.0
  package.json  
  views/  
    _includes/  
      __critical.css  
      _header.liquid  
      _template.liquid  
    index.md

15 - 
  11ty.js  
  init.sh  
  package.json  
    yarn.lock  
  postcss.config.js
  src/
    11ty/  
      _includes/  
        _base.njk
        header.njk
      css/tailwind.css
      index.njk  
    tailwind.css  

16 - 0.3.1  
  package.json  
    yarn.lock
    
17 - 0.3.2
  src/11ty/_includes/_base.njk

18 - 1.0.0
  11ty.js  
  README  
  package.json  
    yarn.lock  
  postcss.config.js  
  src/  
    _includes/_base.njk  
    style.css

19 - 1.0.1
  src/11ty/css

20 - 1.1.0
  11ty.js  
  package.json  
  src/11ty/ ~> 11ty/

21 - 1.1.1
  11ty/_includes/  
    _base.njk  
    header.njk

22 - 2.0.0
  .11ty.js  
  11ty/  
    _includes/  
      _base .njk ~> .html  
    css/ style.css  
  README  
  package.json  
    yarn.lock

23 - 2.0.1
  .11ty.js
  .gitignore
  package.json
  11ty/css/style.css

24 - 
  .11ty.js  
  package.json  
  11ty/
    _includes ~> _components

25 - tms-index

26 - tailwindcss/jit  
  postcss.config.js
  package.json  
    yarn.lock
  11ty/static/css/style.css

27 - 11ty/_components/_base
  
28 - 11ty/index.md

29 - 11ty/_components/_base ~> _Base
  index.md
    
30 - 11ty/_components/header ~> Header
  _Base

31 - 11ty/_components/Header

32 - tailwind ~> post.css

33 - init 2.1

34 - 11ty njk ~> html

35 - rm njk

36 - package.json / scripts

37 - rm yarn.lock

38 - _base/header.njk~>.html

39 - static passthru

40 - tailwind jit

41 - _inc ~> _components

42 - content

43 - 36

44 - 37

45 - 38

### recap , 1411

ok so,

first of all, theres alot of hidden branches  
way too much to tackle now

it seems like if i follow the SEMVER correctly, there wont be much rework  
i do need to redo v0 and v1, let alone v2,  
but it seems like most of my majors can be minors; and my minors, patches  
which is super good news

i think imma just do a weird fork branch to get keith up

### TMST_update , 1420

- [x] mkdir
- [x] git init
- [x] gh repo create
- [x] echo '# tmst update | 04-06' > README.md
- [x] yarn init
  - [x] echo 'node_modules' >> .gitignore
  - [x] echo 'yarn.lock' >> .gitignore
- [x] yarn add -D postcss postcss-cli postcss-import autoprefixer santize.css tailwindcss
  - [x] postcss.config.js, post.css
  - [x] echo 'static/style.css' >> .gitignore
- [x] yarn add -D @11ty/eleventy
  - [x] .eleventy.js
    - [x] passthruCopy
    - [x] input
    - [x] includes
    - [x] htmlTemplateEngine
  - [x] mkdir -p 11ty/_components static
  - [x] vim 11ty/_components/_html5.html
    - [x] !, meta:vp, meta:compat, link:style, njk
  - [x] vim 11ty/index.html
    - [x] layout, title, h1=title
  - [x] echo '_site' >> .gitignore
- [x] package.json
  - [x] scripts: clean, css, build, dev

## TODO , 1625 , release commit

### keith tmst up , 1811

---

# 03-26 | frontroom fr4nk3n

### rambles , 1038

so what am i getting into rn?  
i would like to put some wommy stuff up,  
perhaps blog, todo, or even goals

or maybe some kyle stuff now that he hit me up

### kyChi clean data , 1110

so right now the data is split between  
kyle chicagoroots and keith py-pandas

## TODO , 1112

- [ ] unify kyChi and pyPanda

do you know what i really need to do,  
list my repos

## TODO , 1115

- [ ] repos

### , 1152

these dependabot alerts are actually fucking me  
need to find a fix for these

- [x] made rd-todo

this is interesting because it isnt bound by time

so whats does repos need?

first of all, there are two repos,

how to combine two repos?

### , 1346 , xp5

- [x] configure wifi
- [x] dock to top
- [x] keyboard, esc and caps, l ctrl and l alt
- [x] sleep settings
- [x] refresh mirrorlist
- [x] sudo pacman -Syu

### 1510 , ?Q?

- ? [ ] ? is tms a global, a cli?

### 1515 ,

- [ ] write recipe for new boy spin-up  
  ? [ ] alias
  - [x] tmst
    - [ ] new branch

### 1525 , tms , versioning , oneflow

master is dev  
release is master  
hotfix on master

i need to juggle multiple releases

### 1553 , 

i thought i always got oneflow,  
the shared naming convention, master, messed me up  

i think i learned this before, yet unlearned it

### smerge TMS , 1622

i think i just need to talk this thru

- [ ] , ? , .gitignore , tailwind output

#### 2.0
- [x] readme
- [x] .11ty.js
  - [x] .njk~>.html: 
    - [x] header, index, base

#### 2.1
- [ ] tailwind , bump up folder
  - [ ] package.json
    - [ ] yarn.lock

#### 2.1.1
- [ ] .11ty/: rm .njk
- [ ] rm yarn.lock
- [ ] pkg.json/scripts

- [ ] _inc ~> _compo
- [ ] _static
- [ ] 

# 03-24 | frontroom fr4nk3n

### DONE , 1201
- [x] [wommy-rewrite](github.com/wommy/wommy-rewrite)

### DONE , 1434
- [x] [index.html ~> index.md](github.com/wommy/wommy-rewrite)
- [x] [header tweaks](github.com/wommy/wommy-rewrite)

whats next

## TODO , 1443 
- [ ] make analysis of wommy

### DONE , 1523 
- [x] [todo page](github.com/wommy-www/dev-11ty/todo.md)

## IDEA symlink , 1541 

i need to symLink content somehow

so what i was thinking, is i could either  
symlink the 11ty folder up to content, or  
move it up as part of the init, and then symlink it back down

one of these has to work

### DONE , 1600
- [x] create a new folder  
```
mkdir tms-symlink_test; cd tms-symlink_test;
git init;
```
- [x] redo above as `tms/dev/feat/`
- [x] [index.md](https://github.com/wommy/technomad-stack/commit/4ac247d0a8dda7fe46faafe148a5fe5f8b981b35)
- [x] [_Base.html](https://github.com/wommy/technomad-stack/commit/701136897502b40541b45096b46566483a782d11)
- [x] [Header.html](https://github.com/wommy/technomad-stack/commit/9e20bdbfe6c4be423c7e2542feba829955192382)
- [x] [cleaned up loop in header](https://github.com/wommy/technomad-stack/commit/5b498d61ec37238b8f903ccf8ef4e8d6574af15e)

## TODO , 1641

- [ ] wommy-rewrite

originally was a TMST, dont think thats gonna work  
think i need to write submodule instruction

- [ ] TMST dev
- [ ] push tms/dev to master

how do i do this again? [oneflow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow)  
so i have a dev branch, with it i need to create a release  
releases have tags

### rambles , 1731

so i think the key to maintaining TMS lies in the branches

the default branch needs to be dev  
master just holds the releases  

so i create a repo, and its dev, i make 1, 2, 3, 4, 5 commits  
i think i want to create a merge commit into master 

i guess i need to cleanup my branching

## TODO , 1742
- [ ] cleanup branches

is the naming important?

## TODO , 1824
- [ ] wommy/goals  
      daily / weekly
- [ ] wommy/todo  
      byProj
- [ ] wommy/blog

what do i want to write about?

### 1902 ,
this fucked me up last time, its why i abandoned, was it tmst?

### DONE , 2326 
- [ ] installed manjaro on 1m4c

# 03-22 | frontroom fr4nk3n

### 1839 , some details about the last few days

so kyle hit me up about this chicago roots website  
it was super fun to mash that data, i might hit that again a lil bit

so ive been thinking of trying react on some simple SPAs,  
and i think i have a few repos that fit the bill  
the first of which is my repos repo

## 1905 , TODO , repos needs to be a page on wommy

### 1906 , wommy nav needs a redo hard

i think i did super well with yung seamus, in the commit area  
that means i can do it well

# 03-18 | frontroom fr4nk3n

### 1850 , tabs cleanup

- [ ] keepassxc
- [ ] netlify-todo
- [x] buku
- [ ] nb
- [ ] rofi
- [ ] polybar

### 2053 , i do need some todo

i need something to look back on

### 2147 , tnMBlog

i should be able to submodule the content  
it should be in the jekyll build

the stuff i did in chicago in december, technomad-blog &_blog, its real good  
what i planned on doing with 11ty starter was jekyll

### 2212 , 

- [x] first post ~> published false
- [x] published on netlify

### 2310 , on a roll

### 2331 , kyle hit me up with the csv

### keith , 2351 , py-pandas

# 03-16 | frontroom fr4nk3n

### 1400 ,

just off the phone with kyle  
talked with brenda  
talking with keith  
about to hop back into kyle project

### 1616 , did so much

working on kyles

so whats the move

require in tms

### 1653 ,

need to put something up in the kyle repo

### 1753 ,

lots of incremental, still need to do alot more

- [ ] TMS , upgrade tailwind
- [ ] products ~> brands
- [ ] 

# 03-15 | frontroom fr4nk3n

### 1241 , rambles, cont css

### 1311 , DONE , scss ~> css

## TODO , redo css

things i notice right away

1. -screen
2. .min
3. .v#

the easiest is the version

- moved the scss to style
- noticed screen2 is a feature
- noticed im only using mins

i need to get rid of the versions

### 1417 , actually got rid of min w pretter,

### unify the css

thats such a ridiculous statement

they look like three separate files, but its just one

need to git merge them together

### 1509 , DONE , feat/merge-style

more things i did wrong

- [ ] mobile first
- [ ] two headers

### 1609 , theres so much wrong

i dunno even where to start

i gotta get this shit out a pug  
even tho pug is alot closer to react

### 1621 , mobile first

i should move these  
some to data, some to their own page

### 1810 , kyle-chicagoRoots

this is so crazy

### 1831 , making technomad stack template

---

# 03-13 | frontroom fr4nk3n

### 1136 , starting up , gonna swing vanrych somewhere

### 1436 , back, tryna code before runty appt

### 1441 , wommy.io ? css ? header

it seems like theres alot i need todo

## todo , header component

## todo , css consolidation

### css , 1452

- app.scss ~> app.css  

  units? 1 rem and 1.5 and .75?

# 03-11 | frontroom fr4nk3n

### rambles , tough start, hungover from brenda date , ~1200

### 1715 , tryna kill all these backed up yts

://youtu.be/watch?v=T5zJ8Q4R8tI
nb , hexdsl

between this and the bookmarker, buku

### 1927 , did a whole bunch

gotta replace smerge with gitqlient  
gotta figure out the icon sizing issue

half did polybar

# 03-04 | kycp fr4nk3n

### rambles , 1136

just starting up, tryna nCMS

### cleaning up some youtube , 1308

### 1440 , having trouble focusing

should i set up a headless wordpress?

### 1503 , comments

should i use netlifyCMS?

maybe fauna?

new table from posts?

## wommy.io , 1615

guess im gonna bust into this

#### 1622

so do i want to import the technomad-stack?  
nah, make a new branch first

i dont think i want to do the submodule just yet,  
i think i need to do the symlink first

i also want to start from scratch,  
this is so hard

so i want to use tms

### 1702 , tms version push

## 1811 , blogpost , oneflow

i have these oneflow tweaks i need to document

### 2022 , finished tms 3.0.1 , starting wommy.io

### 2137 , got the submodule working, working on olde wommy.io content meow

# 02-27 | kycp fr4nk3n

## technomad-netlifyCMS , 1202

Q.Q , a bunch of shit got deleted, ive been working for hours 

ok soooooo

technomad-netlifyCMS needs to be a submodule  
this is going to be a pain to configure but its needed

think im going to start with jegan, because thats what im most familiar with

### 1530 , i3 alacritty

### 1602 , tmux sessions

so im writing this readme?

so i have to build two things at once,  
building 1 thing is hard enough 

gonna rip 

i think its actually 3

# 02-26 | kycp fr4nk3n

## 1118 , rambles, cleanup, organization

## 1233 , finished up some jegan, hour of work

## 1930 , kys , back from juju/dillon , gonna hit some jegan? netlifyCMS

## 2010

so whats the problemo

i need to spin up a netlifyCMS  
but everything relies on it

i kinda want to start with anna  
? is that weird?  
thats going to bring in a whole bunch of new problems with components and cloudinary

maybe i should just work on another branch of jegan's etsy

just how i spin up a new TMS, i want to spin a technomad-netlifyCMS from a template repo  
i want to then submodule in the TMS so i can keep components

so whats the workflow,

repo from template , tm-nCMS  
? guess i should make that

## making technomad-netlifyCMS , 2024

turns out i already made that 10 days ago

maybe i need to pen and paper for a second

## back from mlskn , 2046

i think i need to write a how to pull in the submodule

## HOWTO submodule , 2047

submodule sucks, its always such a bitch to setup

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
