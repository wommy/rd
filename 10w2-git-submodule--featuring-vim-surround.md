---
topic: git-submodule--featuring-vim-surround
time: 10-07 1946
place: 43
rambles: working on git surround, noticed my submodule documentation sucks
---

so how do we add a submodule?

go to my [dotfiles repo](//github.com/wommy/dotfiles#readme)


open up these pages

  https://shapeshed.com/vim-packages/#adding-a-package
  
  the submodule you want to add, 
    in this case, [vim-surround](https://github.com/tpope/vim-surround)

realize you dont need shapeshed's directions at all
because thats what this file is for

write a script:

  from pasting in the url the script should be able to resolve a name
  
  the url in this case is

    https://github.com/tpope/vim-surround
  
  the https clone is
  
    https://github.com/tpope/vim-surround.git
    
  the code is:
  
    git submodule add
      `github_url` + .git
      .config/nvim/pack/w0m/start/ + `github repo name`
      `NO trailing /`
    
  in my case:
  
    git submodule add https://github.com/tpope/vim-surround.git .config/nvim/pack/w0m/start/vim-surround
    
    git add .gitmodules .config/nvim/pack/w0m/start/
  
finished in ~/project_current/dotfiles/readme.md
  
