---
time: 1411
place: lloyd bedroom 43
topic: publish workflow
ramble: 
---
  yup, what am i writing here

  1. RD / DATE {MM-DD} / TOPIC / index.md
  2. frontmatter:
    ---
    time:
    place:
    topic:
    ramble:
    ---

  3. get this to play with 11ty

### todo - step out 11ty

  whats the todo in here

    11ty build jekyll, minima
    cleanup TM\_blogposts
      git submodule

### 1436
-
  i made some pushes to TM\_jekyll
  - renamed dev to feat/submodule-attempt
  - rolled dev back to master
  - created a new branch from dev feat/submodule

-
  what i need to do here
    
    combine the files into _content
      
      tm\_jekyll
	_content/
	  _posts/
	  _pages/
	    todo.html <<== _data 
	    olde.html
	    olde2nueue.html
	    nueue.html <<== _data 
	    nueu3.html <<== _data 
	  .gitignore
	  404.html
	  _config.yml
	  Gemfile
	  Gemfile.lock
	  index.md
	  readme.md

- 
  1452 - ^ this is nice
-
  1514 - installing jekyll via AUR
-
  1609 - that took forever
-
  1626
    -
      ``` .zshrc    
	# rubygems
	export RUBYGEMS="$HOME/.gem/ruby/2.7.0"
	export PATH="$RUBYGEMS/bin:$PATH"
	alias jekyll="bundle exec jekyll"
      ```
    -
      gem install bundler jekyll
      bundle install
    -
-
  1915 - still have no clue what im doing
  -
    jekyll such a blackhole
