---
topic: megans-website-design-analysis-for-keith
time: 10-07 1739
place: 43
rambles: 
---

foreword:

  hey keith!

  thanks for putting up with me regarding this format: 
  this is something i've wanted to start doing for awhile now
  but never really had a lushious landscape to attempt it

  anyway, this document is going to be a little living,
  as i am fine tuning the format as i go

  anyway, onto the problem

introduction:

  i recently connected with this potential client from a year ago
  we discussed her current work and a few problems surrounding it
  
  im going to try to reimagine her issues here
  
her problems:

  her name is jegan mones, she produces art out of pittsburgh, pa
  
  a current money item for her are these [custom wrapped lighters](https://www.jeganmones.com/shop?Collection=Lighters)
  
  she said that the workflow for them is completely driving her nuts
  
  im going to do my best to detail that workflow:
    its biggest problem is that the problems tend to clump into 3 or 4 areas
    hopefully my solutions address them, if you have any thoughts please share
  
  lighter workflow:
    she has these lighters she buys in bulk
    she has wraps them in her art prints
    which she then protects under some laminate
    before she places them in a fancy bag
  
  she has more products, but my intention was to create some type of basic CMS
    so that shes in the driver seat of maintaining her own catalog
  i dont want any potentially sensitive data coming thru the to be created system
  anyway,
  
  another aspect thats giving her pains is around something like packaging
  if you look closely its the same problem as the first one
  
  order fulfillment, or everytime she gets an order
    she puts the product in a mailer, with an assortment of goodies:
      1	sticker A
      2	sticker B
      3 a mini print
      4 a business card
      5 a thank you card, completed, consisting of
	A thank you card
	B thank you envelope

  these mailers get sent out irregarless of product,
  when we talked it actually seemed like one of her biggest pains
    was keeping track of all these other items send out in orders
  
my solution:
  i wanted to design a system for her to use to keep a stock of her shop
  functionally it would operate alot like a CMS
  
  so from my assessment her needs are:
    basic crud:
      create a new material
	when she wants to add the material to her catalog
      update a material
	change the name? i doubt this is useful
	the real update is going to be the quantity
	  add for when she buys,
	  subtract for when she uses or breaks
      delete a material
	when she doesnt use it anymore
      
      for the view, 
	im actually going to get right back to this
  
  since i dont want to populate the catalog for her,
  out the gate, this needs to be self building
    she needs to be able to build this herself
  
  i want to build it in a blogpost walkhru editorial thing
    _not too far unlike this_
  
  ive already done this,
    i can show you my notes, but right now i want to get these thoughts out
  
  i have come to the conclusion that she actually needs some type of ledger
  
  when i built mine, the snag i kept getting caught in revolved around 
    the transition from material to product; ex:
      for the first round, i want to 
      
  she claims about her build process
    shes takes a lighter
    puts her art on it
    laminates it
    puts it in a bag
    
  that would be the first operation she does:
    produce a `lighter` from `[ blank, art, laminate, bag ]`
  
  this requires materials: [ blank, art laminate, bag ]
  
  as well as a product: [ lighter ]
  
  so to get to get the create a product to work, she needs to have
  
    lighter blanks
    art
    laminates
    bags
    
  each with a quantity property
  
  i envision this workflow as
  
    add new material:
      name?:
	lighter blank
  
    auto adds a quantity of 0
  
  ---

user experience / user interface:

  so she visits a website
  
  it asks for her username and password
  
  after login shes visited with a page with like 5 buttons arranged in a row or col, dunno yet
  
  this is going to model her state

    the default state, or the homepage, is her stock report
      by default this will say something like no items
  
  another one of those buttons is says 
  
  ---

her workflow

  she logs in
  
  she made 40 lighters and she wants to report it
  
  she clicks the produced button:
    gets a prompt with two fields:
      array from products:
	lighter, thank you card, mailer
      and a quantity field
    she hits okay:
  back to updated dashboard
  
    this function requires
      a password

  ---

her tables

  she has 3 primary tables
    materials
    products
    orders
  
  she needs to be able to add materials
    both in name, as in create them so that they exist
    and in quantity
  
  she needs to be able to produce products
    she needs to have a product array
      which each depend on a material array
    like materials, she needs to be able to create products
      which is composed of a name and an array of materials required
    each of the products need to have a current quantity attribute
  
  lastly, she needs to be able to remove stock from her products
    via order fulfillment
  
  ---

operations

  from this i count the following operations:
    -? indicated user input
    
    new material:
      -? name
    
    add material stock:
      -? name ( from material array )
      -? quantity
    
    new product:
      -? name
      -? material array
    
    produce product:
      -? name ( from product array )
      -? quantity
    
    new order:
      -? product array
  
    ---
  
  2 and 4's schema seems the same
    sub the category they act on
  
  adding requesting user inut for name
    another function that is shared by
      1, 3
      
    ---
    
  input types: 
    text:
      name: req 1 3
    one from many:
      name from array req 2 4
    number:
      quantity: req 2 4
    many from many:
      array from array: req 3 5
  
  ---

how i came to this

  she has three products she wants to keep track of,
    each consisting of materials
    
    lighter: 
      lighter-blank, art, laminate, bag
      
    thank_you: 
      ty_card, envelope
    
    mailer:
      [ array of number_of_lighters ] or { 3: [lighter, lighter, lighter] }
      thank_you, 
      mailer_empty, stickerA, stickerB, miniprint, business_card
  
  she needs ablility to:
    see totals of materials, products
    create, delete materials, products by name
      created materials come with a quantity of 0
      created products require an array of required materials
    add, subtrack quantity of materials by name
    produce product:
      product name from existing product list
      quantity produced:
	subtracks each material by X
  
  ---
  
ledger
