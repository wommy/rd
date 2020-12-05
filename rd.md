# 12-04

## 1807 ' workin @ky's

  diggin this new workflow

    ? todo = what
  
  - [ ] publish to netlify
  - [ ] create /rd

  ^ working on this

## 1817 ' first snag

  so im trying to set up this blog  
  ive already been tinkering with the whole setup  
  i believe that my previous snags with both _blog and -blog had to do with the correct nesting? subdirs, submodules?

  i think the solution i came up had to do with req'ing in rd instead of a sep /content

    lets try to set that up
  
## 1823 ' ? overwrite _blog or -blogs?

  so my THREE current repos are:
  - https://github.com/wommy/technomad-blog
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

## 1851

  - [x] tm_blog feat => master

## 1854

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

  ### how does this really work:  

  -blog is newer _blog  
  rd is newer _blogposts, which is /content in -blog

  - [ ] _blogposts => rd
  - [ ] rd => -blog
  - [ ] -blog => _blog

## 1927 _blogposts => rd

  im struggling with this because its not really a normal operation  
  i need to break it down into simpler steps

  currently im referencing: https://github.community/t/adding-a-folder-from-one-repo-to-another/781/2
  
## 1949

  i think i instead want to use https://gist.github.com/smdabdoub/17065c348289158277b5

## 2117 ' IT WORKED








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
