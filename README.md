# plantshelf

Day 1
started on the backend
made plants
made locations - used generics for this

Day 2
had troubles formatting the database of plants I had generated... took an unexpectedly long time to sort. Had forgotten to put brackets after the text box in bio in the model... this meant that it cuoldnt add my data which contained a bio

decided on adding the ability to sign in with username or email - which required some research to get to work

added seeding files

created my plants - saved till last because it relied on all the others, had a lot of relationships

Day 3
Added authentication and authorization to routes. 
Created custom IsOwner permission view to ensure that users can only view their own my_plants and not anyone else's
added more errors to exceptions
in my_plants, populated the GET routes for index and show with the extra info
