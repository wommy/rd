














## how i came across it

a month or so after the new `dev-server` release
a few weeks ago, i was working on a new personal fork of `eleventy-base-blog`, 

i wanted to
originally it started as a little trial for me to see if i could update to the new dev server, and then the vite plugin version

i recently set up a little development home server raspberry pi that ive been SSHing into. its really nice, as i can just pick up from another computer in my house, also alot tougher on data loss, because it rarely restarts.

on my client browser, i just hit IP:8080/path and hit it, without needing the flag to show that in the output

while on the point of flags, i found the domdiff / reload one, i even hard enabled the refresh with that other flag

i noticed that the vite wasnt live-reloading, after flipping a few lines in the config, i down-graded back to the normal new dev-server and noticed it was either

i even played with the debug output:
what i noticed was that everything was running fine, but that last line that marks the GET or whatever, wasnt being triggered over network somehow.

i even tried to repeat that bug where it wouldnt work without a head, but i believe that was fixed with the dev-server

## TLDR
- stock `eleventy-base-blog`
- upgraded to use `dev-server`
- upgraded that to `plugin-vite`

> noticed `live-reload` wasnt working, thought it was vite

- tried `ntl dev`, that wasnt working
- neither `ntl dev --live`
- downgraded back to `dev-server`, that wasnt working
- even found the `--flags`, no dice
  - toggled domdiff
  - hard enabled / disabled it 
     - ***i'd investigate the function behind this flag***
- installed/followed the `re-install browsync` guide

> live-reload finally works even on `ntl dev --live`

## takeaways

- check the `DEBUG=* npx @11ty/eleventy --serve` or whatever debug output, i noticed that on the `dev-server` everything was working, but that last line that triggers the refresh didnt work until i refreshed it. 
- i believe browser-sync did this correctly



















