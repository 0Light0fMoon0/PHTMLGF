# Python HTML Game Framework
A kit of code files, which can be integrated  or used as a base project for the development of video games for HTML.

# Introduction:
The idea behind PHTMLGF (Python HTML Game Framework) emerge because as a fan of videogames and a junior programmer I was interested in starting to develop my own videogames in Python. With the illusion of being able to create a video game that could run from the browser without having to download it to play with my friends and family, I began to investigate until I found the Django Framework, I found the fact that very few people proposed the development of a video game using the said Framework, and the games I found were too simple, in addition to the fact that I couldn't find any tools for developing games for the browser with Python. After finding myself a little discouraged by the low amount of developments of the orientation I was looking for, I decided not to give up, I began to develop my own games for the browser using the tools that I had at my disposal Python, Django, HTML, CSS, Bootstrap and a bit of JS. One year after starting to develop my own amateur, improvised and rustic video games, I can say that after all this journey the result has been PHTMLGF and I want to share it, so that those people who are in the same position can start from a point of reference.

Having given the introduction, I would like to comment that PHTMLGF is a kit of code files, which can be integrated into their projects or used as a base project for the development of video games using the technologies previously mentioned in the introduction. I have to emphasize that I am just starting out in the world of programming, so probably a more experienced programmer will be able to find possible bugs or errors in the code that, in my opinion, are not perceptible to the naked eye, so future developers may They can optimize the code a lot. It goes without saying that any contribution you want to make is more than welcome, be it code optimizations, (constructive) criticism or opinions.
My main clarification is that my intention or idea is that PHTMLGF is free for anyone who wants to use it, so I am looking for permissive licenses to ensure that this purpose is fulfilled.
I hope the community grows and together we can achieve something great, thank you very much for your attention.

# How to get started with PHTMLGF?

• First step, install PHTMLGF, for this it will be enough to install Python and Django Framework on our computer and download the files from the PHTMLGF repository.

• Second step, we move our project files to our project root directory.

• Third step, we adjust our project settings according to our needs in settings.py.

• Fourth step, in the root directory we create a "static" directory where the textures and animations of our game will be stored.
Ready! Our PHTMLGF kit is ready to start creating video games.

Do you want to start creating games?
Visit our community on discord where you will find all the information, you can also contact me, I will be answering all your questions. Remember that the idea is that PHTMLGF is free and open for everyone to use and build it together, so any opinions and ideas are welcome. https://discord.gg/4RVR8eQUDP

What features does PHTMLGF provide?
• Being able to work with classes of previously created entities, with their attributes and methods created to facilitate the work when developing the game logic, some of these classes are: player entity, place entity, decoration entity, portal entity.
• Work on a previously created graphical interface to be used as a base or template and easily modified.
• Work with and easily modify the attributes of previously named entities with the use of methods.

# How does it work?
Entities exist both in the database and in memory when they are instantiated (these are loaded into the Chargers section of the view.py file in the mainApp application directory). They can be modified according to the developer's needs, that is, they can be worked on by adding more attributes or methods. The latter can be done from the engineClass.py file of the engineApp application, but remember that any attributes that are added or modified here must also be added or modified in the Chargers as well as in the models.py of the loginApp application.
All entities are loaded from the database (by default) only when starting the server, with the exception of players, which will load its players from the database every time a user enters or exits the game.


Here is a description of the entities, their attributes and methods:

-----------------------------------------------------------------------------------------------------------------------------

EntityPlayer:

nickname: Name of the player.

password: Player password.

creds: Money or player score.

posx: Position on the x-axis of the player.

posy: Position on the y-axis of the player.

place: Place where the player is.

imgup: Image or texture of the player up.

imgdown: Image or texture of the player down.

imgright: Image or texture of the player to the right.

imgleft: Image or texture of the player to the left.

animup: Animation or texture of the player up.

animdown: Animation or texture of the player down.

animleft: Animation or texture of the player to the left.

animright: Animation or texture of the player to the right.

texture: The texture, animation, or image that is currently printing to the player on the screen.

funcShowing(self,imganim): Change texture to imganim.

moveUp(self): Moves the player up. -2.2222% of the screen.

moveDown(self): Moves the player up. +2.2222% of the screen.

moveLeft(self): Moves the player to the left. -1.25% of the screen.

moveRight(self): Moves the player to the right. -1.25% of the screen.

joinPlace(self,newPosx,newPosy,newPlace): Changes the position and place of the player.

-----------------------------------------------------------------------------------------------------------------------------

EntityPlace:

place: Name of the place.

texture: Texture or background animation of the place.

txtExt: Texture or animation of the exterior of the place.

log: Message history of the place.

owner: Owner of the place.

posx: Position on the x axis of the place.

posy: Position on the y-axis of the locus.

location: Place where this place is located, if it is not within any, set it to None from the Django administration panel.

sendMessage(self,player,message): Adds the name and message sent by a player to the log.

-----------------------------------------------------------------------------------------------------------------------------

EntityPortal:

portal: Name of the portal.

texture: Texture or animation of the portal.

owner: Owner of the portal.

posx: Position on the x axis of the portal.

posy: Position on the y-axis of the portal.

toPosx: Position on the x axis to which the portal redirects.

toPosy: Position on the y-axis to which the portal redirects.

toPlace: Place to which the portal redirects.

extSize: Portal action size or scope.

place: Place where is it.

maxWidth: Portal action size or scope.

maxHeight: Size or scope of the portal action.

playerJoin(self,psx,psy): Evaluates if a player's position is within the range of the portal.

-----------------------------------------------------------------------------------------------------------------------------

EntityWater: No applications at the moment.

-----------------------------------------------------------------------------------------------------------------------------

EntityDecoration:

decoration: Name of the decoration.

texture: Texture or decoration animation.

posx: Position on the x axis of the decoration.

posy: Position on the y-axis of the decoration.

place: Place where the decoration is located.

-----------------------------------------------------------------------------------------------------------------------------
EntityWindow:

nameWindow: Name of the window.

title: Title of the window.
