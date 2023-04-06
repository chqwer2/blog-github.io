# Body Models Driving the Age of the Avatar 

### – with Michael J. Black



And, it turned out to be difficult to get computers to estimate the body when it didn’t really know anything about the body. 

thousands of vertices, thousands or tens  of thousands of triangles, and the idea that you would take an image and somehow get back all of these vertices and triangles are kind of crazy. 



#### Human interpretability 



animator uses the dead standard  technique in graphics called linear blend, skinny and linear blend skin  has all kinds of artifacts.

And so what an animator does is they go in and add correctives, that depend on a particular keyed pose that fix the artifacts. 



##### Why Accurate Human Model

And so there was a lot of interest from the psychology community and from the medical community. 

So in psychology, they were interested in, we had collaborators who were working on anorexia nervosa. And  there was a theory that anorexia was a disease of perception that people would look at their body and they would see it incorrectly.

They would see themselves as fatter  than they actually were. And if it were a perceptual problem, maybe you  could treat it by, by training people to perceive their body  differently. So, together with our collaborators, we did VR experiments  on how people looked, the patients looked at their bodies in 3D, and we  were able to show that they actually perceived their body shape  correctly, their body shape and the shapes of others.

And this was really useful for that community to move on from a hypothesis that didn’t really work out. 



**Medical**

Yeah. There’s another one which I really like.

And it’s also, this is in the medical  domain as well, and that’s our body models being used for the early  diagnosis of cerebral palsy in infants. So,infants, you know, they move  around in what looks kind of a random way, but it turns out that if you  are a trained observer, the kinds of motions that an infant makes reveal whether they have motor difficulties that could be a sign of cerebral  palsy.

And if it’s detected early enough,  that early intervention can really make a difference in the lives of  these people as they grow up. And, but there are very few people who are trained as experts in detecting these motor movements. And so we,  again, worked with a bunch of collaborators, who are experts in.

And developed a system with a child  body model called smile, S M I L, that tracks the babies using R G B D  so color and depth imagery, in 3D. And then we developed a system that  takes their motions and classifies whether they might be at risk for  cerebral palsy or not. And I think that’s another neat example that I  would never have come up with that on my own, but by making this kind of technology available, we get people coming to us and saying, I’ve got  an idea, and I know how I could maybe use this for solving my problem,  which is very exciting.



**How to model Baby**

eah. There’s another one which I really like.

And it’s also, this is in the medical  domain as well, and that’s our body models being used for the early  diagnosis of cerebral palsy in infants. So,infants, you know, they move  around in what looks kind of a random way, but it turns out that if you  are a trained observer, the kinds of motions that an infant makes reveal whether they have motor difficulties that could be a sign of cerebral  palsy.

And if it’s detected early enough,  that early intervention can really make a difference in the lives of  these people as they grow up. And, but there are very few people who are trained as experts in detecting these motor movements. And so we,  again, worked with a bunch of collaborators, who are experts in.

And developed a system with a child  body model called smile, S M I L, that tracks the babies using R G B D  so color and depth imagery, in 3D. And then we developed a system that  takes their motions and classifies whether they might be at risk for  cerebral palsy or not. And I think that’s another neat example that I  would never have come up with that on my own, but by making this kind of technology available, we get people coming to us and saying, I’ve got  an idea, and I know how I could maybe use this for solving my problem,  which is very exciting.



So he developed a method to learn a body model directly from R G B D data, not full 3D scans, but just the R G B D. 



 I think it’s like six of the top 10  NASDAQ companies. Have licensed it, it’s in wide use. And a lot of the interest there is in clothing design, for, clothing sizing and  applications in that space.



plug and play



We did all sorts of stuff until we just  went back to what is it that everyone is using in the graphics industry  today? And it was linear blend skinny with these post correctives that I was describing earlier and the problem with that was, that it was all  hand designed. 

**And so our insight was really to take such models and  say, how can we learn it from data?** 

you guys were trying to build a data driven version of these corrective blend shapes. 



So we wanted to learn the template shape of the body.

That would then be deformed. 

We added  these blend shapes for body shape to change the body. We wanted to learn the weights that you use in linear blend skinny. 

We learned the joint  locations because the body shapes change. 

Your joints are in a  different place than my joints. So your joints have to be a function of  your body shape.

### Problem Solved

And there, it turned out, oddly, that  the rotation matrices describing the part rotations, we could linearly  relate the shape deformation of the body, to the elements of the part  rotation matrices.

And this was the best thing we came up with. We had many different formulations, but this was dead simple.  Remarkably, when we trained it, even though it sounds more restrictive  in many ways than SCAPE, it was more accurate than SCAPE. So it ticked  off all the boxes that we needed. Accuracy, speed, compactness, and full compatibility.



you guys had the foresight, especially back then to connect this to standard tools like blender and unreal, and even Unity. And the other super impressive part from my perspective is trying really, really hard to create something simple.

### Be simple

And of course the common filter beat my  fancy nonlinear, crazy particle filter. And so I’ve had to learn that  lesson again and again, start with the simple solution. And then when it breaks, then develop  something fancier. But yes, you’re absolutely right. It’s a disease in  academia to overcomplicate. But if you want people to adopt your stuff,  if you want it to have an impact in the world, then if it’s compatible,  you have a much higher chance of it actually working out.

### Human Body

one of the reasons I was interested in 3D body models for computer vision in the first place is because humans  interact with the world. They touch things to manipulate it. 

We need surface model

Hands: MANO

Head: SMPL H



### SMPL

SMPL X, X stands for expressive here

But

##### Help Amputees

It can’t represent people who are amputees. It can’t represent little people. It can’t represent people with scoliosis.

And if you have a specific case and I’ve  had populations come to me that say, look, our population is different  from what your model represents, can you help us build a model like  this? And indeed you’ve gotta collect the data and then you can turn the crank and you can build these specialized models.

So I think if a company is really going  to push this at scale and really wanna cover the whole world, they  should, you know, go to that. I mean, in academia, you can’t really  afford to do this, but a big company could do this and generate a  broader model. 

### Expression

getting computers to understand us, to  understand our emotions feels like a critical step to making computers  full partners with us.

### Research

And even though I was young, it was a  great learning experience working in a big company like that. And I  learned a lot about how to manage research and how not to manage  research. It’s a tough thing in a corporate environment to really do  basic science. But I managed to make the case for creating a new group  because Xerox had branded itself or rebranded itself, the document  company.

##### Why go back to be in Academia

I had a lot of fun at Xerox until I  didn’t. So, it’s almost a tautology that great research labs happen in  industry when that industry has something close to a monopoly, you know, whether it’s bell labs or Xerox or Microsoft, you know, when they’re  just really flush with money, they really start thinking about, well,  what, how can I do something for the public?

### Work

How do you keep up this velocity of innovation? Also, how do you kind of structure the workforce that you’re in charge of

**Need software engineers**

what we do for the Institute as a whole  is in addition to scientists, we hire software engineers. We have  something called a software workshop where we hire professionals. They  can become permanent staff members and their job is to help take science and make it real, make it something we can distribute, make it robust,  licensable. 

Use what you build..

**How it works**

It’s just a little one off. And today the problems we wanna solve in computer vision and AI, they’re bigger than  that. You can’t afford little one off solutions**. You have to have things that build on each other and that you can then support and maintain so  that every next generation of students has a bigger foundation to play  with.**

Data team..

And so, I think the reason is that we’re  so productive. So I have amazingly talented students and postdocs, but  they’re also supported by the data team and the software team. And that  lets them just do much, much more.



### CTO

we have similar roles on our side.

Doing infrastructure, creating  different code bases that we can build off of helping our algorithms,  engineers that are focused on deep learning aspects of the different  capabilities that we’re creating, the environment that they need in  order to work productively. And then of course, in order to create the  ability to generate data at scale, as you know, we need also people that don’t only come from an engineering background, we have amazing 3D  artists as an integral part of our team.

**Company**

Though, we also spin off companies. We’ve spun off two companies. we’ve licensed a bunch of technology and I  think that’s really important, you know, as I said, I feel very  fortunate to have the position I have and to have the research funding, I have the German taxpayer pays for me to do this crazy research I do,  and they get out of my way and they trust me to do it. 

And I feel with that kind of freedom  comes some responsibility to make sure that what I do has some impact  and it comes back to society in some way.



There’s a tremendous amount of talent in  Germany, particularly in the area of AI. and what’s been missing is a  sort of a venture backed startup mentality for deep tech. And we’re  trying to make that happen. 

**Fund**

So there’s a ton of funding for deep  tech, and it’s really the specialty here. Next time you’re in Israel.  I’d love to connect you with some of the relevant folks from the  industry.

### Patent

And so when I started working with the 3D body models, we had our first success of estimating a 3D body model  from images. I thought, okay, this is the next thing. This could really  be big.

And so together with my collaborators, we wrote a big patent, on the whole suite of things we were developing at the time. 

**Work or not?**

We actually had a system at Brown where we had women shopping, locally taking pictures of themselves and they had 3D body scans.

We had a recommendation system that  would recommend clothing and sizes to people based on their body shape.  And the whole thing worked until we said, okay, now take this camera  home, take pictures of yourself and we’ll build your body model from  that. Okay. Disaster. So we had the ideas and when we had an accurate 3D scan, everything worked, but the computer vision part didn’t work,  people took terrible pictures.

You know, the exposures were bad, the  lighting was terrible, the clothing was wrong. We **couldn’t get an  accurate body** model in somebody’s home. 

### Hard to change

And to really change the fashion  industry in the ways it needs to change, you have to attack many pieces  of the problem simultaneously all the way through, from design to the  point of sale and a little startup – it’s like poking an elephant.

You can’t really affect much change in an industry like that. But fortunately deep learning came along and  things like Snapchat filters came along and everybody got very  interested. How you could analyze 3D bodies from a cell phone and do fun things with it. And so we pivoted a bit in that direction and generated a lot of interest.



Go find yourself some business people, build an actual team, build this thing up and then come back and talk to us.

And so I was delighted that it  actually all worked out in the end. I went and found a CEO. We built a  team, we got some funding, we built the company and then they did, they  did actually buy us. 



**MPI spinoff**, licensing the SMPL model out and doing a lot of amazing work around productized, various aspects of body models.

She was an author on the original paper  and many other papers that followed. So that’s kind of the nature of  these software engineering positions. People get directly involved in  research, do they contribute to it, they publish papers and then she  spun out to lead this company.

### Avatar 

And in fact, many avatars that you use  for different things. You’re gonna have an avatar for shopping, for  clothing and avatar for being in virtual meetings and avatar for, going  to a concert, an avatar for playing a game. 



Are they going to be like you in some  way? i.e., Will they have your facial expressions? You know, if I see  you from a distance, I would recognize you because I know you. It should be the same with your **avatar,** whether it’s a Lego character, Roblox or  something, or it’s physically like you, it should **embody** you.



And so your emotions, your expressions  coming out through all of your avatars, I think is the future we want.  And what this will allow is, you know, I think the vision of  meta-commerce. Or eCommerce in the metaverse right now, it all sounds  like it’s NFTs and digital clothing and digital sneakers or something,  but more people buy real clothing in the real world and that’s a real  need and we haven’t yet blended these things.



I think we need a unifying, avatar  technology that can support your animated avatar can support you in your video game, whatever it happens to be. And could support you doing  e-commerce when you’re shopping for clothing or bicycles or whatever  else it is. 



Meshcapade is really to provide a  platform that enables the age of avatars that enables easy creation. So like I say, there are many friction points today. Why we don’t have this age of avatar creation is a big one. 

**How to make avatar**

So they can’t, you know, meta-humans is  super cool avatars, but you’ve gotta really know what you’re doing to  create one. So most avatar creation methods are like, you goofy things where you, you know,  pick your hair color and you pick some makeup and things like that. And it, you know, it makes an avatar, but it’s not really embodying you.

**Connect it with Meta-verse**

That’s an incredible vision, and I  definitely connect with it on many different levels. I get asked a lot  of times, you know, when is this metaverse happening? What is the main  killer app in the metaverse and why will people be interested in the  metaverse for example, and from my perspective, the day that we choose  not to talk through zoom, but we prefer to talk through a VR device and  talk between our embodied selves or our avatar by itself.



#### Career Tips 

It’s a super question, you know, right  now everybody is super focused on deep learning and it’s great. It  works. And it’s, you know, it’s an effort just to keep up with that, but I would really encourage people beginning in this field to **not just do that.**



Learning linear, algebra probability,  physics, whatever it happens to be. These skills that you get in these  other disciplines, really ground and inform your ideas and can be  incorporated in. So there are many properties of the world. For example, machines don’t have to learn. They just are there.

And if you understand mathematics or  physics, you can exploit them as a training machine. So one of the great things about Datagen is, you know, providing synthetic data to people,  to train machines, but there are other ways there are some generic, in  addition to that, there are **generic priors that we know things about the world.**

#### **know about the physics of the  world**

We know about the physics of the  world, and it doesn’t necessarily have to be learned. So I would not  just be very narrowly focused on deep learning. I would just look a  little bit more broadly, learn some geometry. The 3D world is important. And even if your networks are going to learn about the geometry for  you, if you don’t have intuitions about prospective cameras and  occlusion and or properties of light, you know, if you can’t, if you  don’t know about illumination and how it interacts with surfaces, then  you may not really understand what your method is doing and why it’s not doing the right things.

And you won’t know how to choose the  right data to actually solve that problem. So having physical intuitions about the world I think is really critical. 



