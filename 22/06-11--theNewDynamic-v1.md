- wtf is a static site #highdive
  - "Sat, May 14, 2022 at 1:25am"
	- I guess I'm doing this talk for Ian in AA at SEM.js
	- the history of websites
		- static html uploaded
		- served
		- http
		- tim berners Lee
		- serving documents
		- sometime we starting servers serving dynamic documents
		- we split the document into a shell and content
			- php tags
	- name:
		- the new dynamic, thanks budparr
	- ssg history
		- Jekyll, mixture, ruby
		- GitHub rails
		- JavaScript node npm
		- react gatsby
		- spike, dato - API
	- talk length
		- introduction - who I am, my story
	- 11ty presentation as practice
		- topic: fetching
	- the future
		- next, vue, serverless, edge, deno, vite
		- PWA, service worker, SSR
	- what ssgs do
		- setting up express
		- templating
		- routing: [Page]
		- jade/pug liquid, haml, mustache, erb, ejs
		- go hugo
	- my past
		- static IP world of Warcraft Warcraft 3
		- film editing, music composition, psych, UI/UX

#semjsTalk

"the new dynamic "

- > #Ian
  - #done
    - title
      "the New Dynamic :: #womRant "
  - #tudo
    - bio
  - #doing
    "description / explanation"
    - theNewDynamic.org
      "2014's only source for static tips n tricks - 
      drastic facelift
      "
    - -
      "but what was it "
    - a nyc meetup / blog about static sites
    - homage to #budParr
    - 
- ---
  "#content"
- wtf is a static site #highdive
  "Sat, May 14, 2022 at 1:25am 
  "
  - I guess I'm doing this talk for Ian in AA at SEM.js
  - the history of websites
    - static html uploaded
    - served
    - http
    - tim berners Lee
    - serving documents
    - sometime we starting servers serving dynamic documents
    - we split the document into a shell and content
      - php tags
  - name:
    - the new dynamic, thanks budparr
  - ssg history
    - Jekyll, mixture, ruby
    - GitHub rails
    - JavaScript node npm
    - react gatsby
    - spike, dato - API
  - talk length
    - introduction - who I am, my story
  - 11ty presentation as practice
    - topic: fetching
  - the future
    - next, vue, serverless, edge, deno, vite
    - PWA, service worker, SSR
  - what ssgs do
    - setting up express
    - templating
    - routing: [Page]
    - jade/pug liquid, haml, mustache, erb, ejs
    - go hugo
  - my past
    - static IP world of Warcraft Warcraft 3
    - film editing, music composition, psych, UI/UX
- #via talk 
  "some thoughts on Astro
  "
  - Islands architecture
  - Slinkity
  - vite
- #marx #search
  "island guy #website, #blogpost
  "
- 11ty the #javascript #framework
- __ - % #search #marx
  "markdown slides - mirian suzanne"
- ---
  "inbox
  "
  - https://thenewstack.io/the-state-of-application-modernization-2022/
  - zachleat.com
    "image post about size with squoosh"
  - PWA, offline, workbox
- toOrganize
  - tND
    - future of websites
      - deno
      - typescript
      - edge / serverless
      - rust => wasm
      - env vars
    - it might be easier to spin a full server
      "in a weird way,"
    - ? so - I'd really rather not learn docker
      "proxmox and cockpit are just docker boxes"
    - PWA
      - Service worker - workbox
      - remote db / SQLite
  - tND
    - webpack 
    - browserify
    - slinkity 
    - laravel
    - tailwind
      - twin macro
      - window
      - uno
    - PWA
    - vite awesome
  - tND
    - monorepo
    - module federation
    - pnpm
    - components vs architecture
  - tND
    "beats of the talk"
    - bud parr
    - static
    - my story
    - spike
    - 11ty
    - serverless
    - node
    - react n vue
    - snowpack
    - Astro
    - islands
    - Gatsby
    - that talk at vice
    - service workers and workbox
    - vite awesome
    - PWA 
      "notifications "
    - slinkity
    - SSR
      "fastify "
    - tailwind
      "antfu"
    - appshell
      "Harry roberts"
    - graphql
      "first netlify"
- #tND #research
  "Thu, Jun 2, 2022 at 2:49pm "
  - kent - shipping to the edge
    "& notes
    "
    - the server - CDN ( the edge)
    - remix
  - swizec serverless
    "Thu, Jun 2, 2022 at 7:54pm "
- #tND
  - numbers on websites
  - with react
  - marketing
  - wom.dev
- #rambles
  "- Sat, Jun 4, 2022 at 2:19am "
  - so i think i need an apps folder
  - i think specific functions are packages
    "AKA eleventy, sanity fetch"
- #rambles 
  "- Sun, Jun 5, 2022 at 6:33pm 
  "
  - primeagen & ryan carniato
    - server - stateless
      "mvc makes sense"
      - hook model data up to view data
      - managed by
      - singleton controller
    - client - long sessions
      - mvc -> mvvm 
      - controller isnt singleton
        "per instance"
      - ?
        "what should you tie state data to"
      - view-model
        "doesnt need to be sent to server
        "
    - state belongs with view
      - dont wrap models with view-models
      - view + model = component
  - eleventy w12
    "- Sun, Jun 5, 2022 at 8:43pm "
    - is-land
      "eleventy client components"
      - how/when load client-side components
        "&& hydration / initialized
        "
        - island control for partial hydration
          "nest inside web component"
          - purple - hydrated / initialized
          - green - island
          - eager - vanilla
          - ---
          - petite-vue
          - on:visible
          - works with details!
          - ---
          - nested groups
          - on:idle
          - on:interaction
            "touchstart, click ;; and more"
          - on:media, reduced motion, on:save-data
        - relies on web-components
          - fallback content
            "big perk
            "
          - different fallback/interaction behaviors
            "progressive enhancement"
  - tND
    - optimistic rendering
    - people i listen to
    - PICKS
      - zachleat's youtube?
    - #CSS - go thru olde tabs!
      "twin, twind, tailwind, windi"
    - ntl graph
    - ?
      "pivot talk towards picks? ppl 2 follow?"
    - 3 talks ? 
      - ssg
      - tailwind
      - serverless|edge / island hydration
      - marx
    - marx
      "100% static?
      "
      - 11ty
      - netlify cache
      - serverless 2x /day
      - island
        - petite vue
      - vite
        - pwa
      - 0 client-side js
  - edge wordle
    "benmeyers - Sun, Jun 5, 2022 at 10:05pm "
    - edge is middleware?
      - ? pwa & service-workers
      - ? edge = cdns service-worker middleware 👀
    - use the edge's service-worker
      "ala serverless "
    - deno packages
  - blogrocket w zach
    "- Sun, Jun 5, 2022 at 10:23pm "
    - 11ty w/ components & interactivity
    - vite
    - web components
      "hydration for free"
      - progressive enhancement, not server render
  - ! 
    "apply to web marketing jobs"
  - images for marx
    "w/ 11ty image plugin
    "
- fireship quote lazy dev
  "#tnd - Sun, Jun 5, 2022 at 11:25pm "
- disability #tND
- cube Hank Andy Bell #tND
- cahoots
  "#tND - Tue, Jun 7, 2022 at 7:07pm "
  - do a dummy run
    "see how long it is"
  - ask Ian how long I have
  - I gotta think about my slides
  - I just need to start the slides
  - big mouse
  - strapi -> mongo
  - I make marketing websites
  - list the NPM packages
  - Where you been lars
    "show all my pictures"
  - show some JS off
    "be proud of my code"










































