# From Deep Learning of Disentangled Representations to Higher-level Cognition

Yoshua Bengio

2018 Report



But I think we would be all very much more productive if we coordinated those efforts if we prioritized what could help people the most if we talked, if we invested in talking to the people in those say poor countries who could benefit most from this to understand better what could have the greatest impact. 



And if we didn't just do that, that science, but also made sure that the grad students in those poor countries also learn the machine learning that goes with it, and maybe come for internships in our big labs and go back with the state of the art knowledge to their country to bring that future wealth there instead of us trying to save them. 



 will in the long run and help all of us



And we're starting to use the same kinds of mechanisms as evolution is used, like meta learning and all that stuff. 







questions about what makes something part of question cautiousness prior



Yeah, is this what things come into our consciousness or? No, like,

there is these packs in the world or the observation, right, right. Is it just another layer of abstraction you're thinking about to make the computation easier, or we'll have some special properties like being shared across agents learning across different domains kind of this belonging to the common sense belonging to these and sharing in terms of acting in the world like this can be these special properties in your mind shared across applications and agents.



So I think first of all, there is a lot of knowledge that we have, and that we are consciously aware of, but is still hard to communicate. But a lot of what comes to our consciousness is precisely the stuff that we tend to communicate. And it's interesting to ask, What about animals which don't have language? Do they have something cool, I think some primitive versions of that, yeah. And we have probably a stronger type of consciousness because it's enhanced through our learning to communicate with with others using God. But a lot of the common sense knowledge isn't something we even were even aware of consciously. I think that's why the classical AI program failed because we were trying to build like the roof of the house, and we didn't have the scaffold, and the scaffold is perception and the low level understanding of the world. So this is sort of near the top of the house that I'm talking about, and it's not built yet either, right. And it's connected to reasoning and symbolic stuff, and All



right, so just sticking to one example, early everything mentioned the first half of the talk like in the feature space. So that mean, like somehow, maybe imposing linearity like towards the end of the neural network can help us to resolve some of the robustness issues about



Yeah, so that's precisely what consciousness Breyer is doing. I mean, we didn't talk about linearity. But if you think about what this equation means it says that, we take the data we bring into this sort of consciousness level, this representation level and in that space, I'm going to have a predictor that's very sparse because I just take a few variables. And it's also very simple. So the neural net that makes the predicts this guy but this guy is sitting on top here and hopefully is very, very simple. It's just a simple linear logic or you know, when MLP right, very, very simple. Doesn't need to be linear. It can be whatever you want. But But, but the point is, by constraining the capacity of this level, we are forcing the representation to somehow come up with those those factors or those representations, those features that have this property that we can now do very simple operations. In order to predict stuff from other stuff.



Earlier, you had a picture that shows interpolation. So you should are in pixel space, interpolate images doesn't give you anything that makes sense.



So So assuming you're trying to say that, you know, we've been operating the effects. But another thing that will give you the same interpolation is, for example, you interpolate over what buffer statistics, they'll also give you something like the top instead of something in the bottom,



so I'm just saying even by interpolating the worst, there's a well defined meaning of every scenario. So I mean, define a metric that has the Wasserstein distance,



You mark the way the West long distance is the distance between distribution so it doesn't make sense what you're saying.



I don't know what the right thing but hopefully it's something simple that can be learned quickly. That's the most important thing, right doesn't mean many parameters. That's, I think, what, for example, allows us to do one shot learning. Once you've represented things in this abstract space, because relations are simple and sparse. Then a single example or a few examples are enough to sort of introduce relationships that you didn't know before. That's the main characteristic of trees.





conditional decoding. But before before I do that, I want to challenge the first and you said that humans are very good at learning in an unsupervised way. So let's take the concept of convexity. Did you learn convexity from the physical world from your interaction? No. Where did you learn



You wrote it in school? And I think that's that's important because the we learned things gradually, right. And I'm going to claim that to progress. Deep learning is that the hypothesis space is fixed. And the way human learns is that they grow the hypothesis space gradually. They grow it would help.



I don't see why you're saying that deep learning has that **limitation**. I wrote a paper in 2009 called curriculum learning.

This is all in line with that. There's no contradiction with lymphocytes. Well, so. So one of the early ideas was that we gradually build new concepts, thanks to the concepts we've already learned. And I don't see so here you think of it, like I'm showing a snapshot, but in the evolution of the learner, presumably this space would get richer and more abstract.



This gradual growth of the hypothesis space is where we need to focus. And I think this is the very interesting things to model but it requires but it's not



on that note, it comes to the idea of of theory revision, right? And so, as opposed to gradually growing things, you talked about children having causal theories, they often have causal theories that are wrong, and it completely changes the theory right, that a gradual change is not a repeated exposure. How does that fit into this notion of just massive revisions of what the underlying representation looks



like? Well, I like that question because I don't have the answer. Right. So, so the good news, so here, there, I mean, knowledge is is at different locations here, but in particular, there's the the mapping to representations. Then there's this very compact representation of how the things are related in that in that space and sort of corresponding to the set of rules if you want, right. And the good news is that the set of rules is very easy to change. That's where you can do one shot learning this is where you can completely change your view on something without having to rewire everything so that's that's connected to classical AI with the idea that oh, I can keep all my rules except the change this one. And now my conclusion is gonna be completely different. Where that means is irrelevant. So by factorizing, because invasion from facts and rules to make things a little bit of a gross sketch, I think makes it much easier to do what you're talking about. Whereas if it's sort of hidden in the machine, have one big neural net that does everything. It's kind of difficult now, to change your mind about something specific. And the representation is never wrong. It's just it might be insufficient to generalize, but it's, it's never wrong. It's just a representation. The actual facts are represented in this top little set of rules if you want. So I think it's facilitates your thanks for asking you haven't thought about it.



If you want to make a drastic change. Now with a few example, you keep very low capacity. If you have hundreds That's



right. That's what I said the top thing has very low capacity. It's sparse. It only uses very few variables. And hopefully something's triggered like in here.



So how's low capacity fit with deep learning?



Oh, no, but the deep learning part is the representation right? I mean, everything is deep learning, but, but the part here that's traditional deep learning is the mapping from nothing from say images, or image sequences to that representation space, and that's where most of the capacity is, and that's where it's hard to learn. And that's where we don't do a good job here because I think we're not putting as much pressure as we should on the representation to be abstract and have these. Well, easy that we can make predictions in that space very easily. That's what this is saying.



Yeah, we have unconsciously goes through consciously to make the concepts sort of unconsciously encode all the



information or the one on one information, or is it world information, different colors? So pretty much everything that you can name right so even low level stuff, if you ask me like, What is the color of that pixel I can like pay attention to it and tell you but from different domains. It's very rich, this unconscious state, but mostly, it's interesting, not because it has the pixels, but because it has the higher levels.



This distinction that we can only keep maybe some things in our memory that's sort of interesting that you see this as a good prior not yes, it's one of our brains, right? But there's a bunch of other things where we're kind of irrational or we're not good. We're not going to end in like vastly different skills and where we act and kind of irrational ways. I wonder if any of those would also be interesting priors for dealing with the real world as opposed to seeing them as kind of failures of our



well, maybe, but I think we have to try to think of how they could be useful from a machine learning point of view. And then you could use this it's a meaningful thing to add and not just oh, it's shoot ourselves in the legs because humans have that failure as well.



But it's I think it can be useful that the world is really complicated and we need to be able to as soon as acting that in our world, and we're trying to reproduce that right and so some of these things might be necessary sort of priors just to be able to learn quickly enough, right? You need to assume or act as if you're never gonna have to deal with things that are in 10 orders of magnitude different scale the same time.



But we have also to be careful not to try to reproduce everything that we know about humans and the brain because some of these things might be side effects of our particular hardware or, you know, evolution is imperfect and you know, we like to understand what we're doing. Last question.



So I'm curious about the, what you're saying about about using the low capacity representation of the world for for causal for causal reasoning. And reconciling that with the fact that Well, I mean, yes, we often have a very abstract approximate reasoning about the world we know birds can fly, for example, but then oftentimes when you're trying to really think through a specific situation, the devils in the details how do you think that that a good model would only use a single layer of a book pass information or do you think there'd be some range of



so I don't think that the this abstract, low dimensional thing is the only space that matters for reasoning at each time. we project ourselves in the future when we think about something. All the low level stuff is there hidden and influencing what's going on? So I think that's one reason why traditional rule based systems fail because they are an incomplete description of what's really going on. Whereas we're able to use our intuition along the way, which is hard to do with with pure symbolic Ruby systems. So by connecting the low level stuff with the high level stuff and keeping them connected, and I think we can avoid that trap Thank you



What can we really do? You know, what are the research directions that we could possibly pursue? Especially I would say you need a turn. I certainly believe that that we have some amazing opportunities the term towards understanding for example, that being the result of ml machine learning should not be just a set of classifiers. One for you should ask for the robust AI agent that continues to learn skills knowledge, you know, by practicing and by exploring in the rest of my talk The perfect light in the figure eight here, and you have all those sample points in a perfectly sampled from those three representations to play for the practice you often see have some noises, and the lighting in B you see some noise, and the impact is you also see some kind of outliers, which is even more annoying. And in this case if you can see you have those red points, you know, showing that you know that's the thing. So they are really three related. The example on the right hand side it's just it's just not the right I just don't really get it and then the AI on the computer So time is now, you know, forced to move to, to really focus on, you know, merely to create research in terms of you know, understanding, we should move to deep understanding from deep learning. In a way, you know what we're trying to do is actually you know we are working towards the robust AI, so that we can statistically geometrically understand something semantically really explain, you know, what AI is really doing. So I'm going to stop here.





![image-20220724225104542](https://ik.imagekit.io/haochen/Typora/image-20220724225104542.png)

![image-20220724225244192](https://ik.imagekit.io/haochen/Typora/image-20220724225244192.png)

How can we separate each factors from each other

![image-20220724225454897](https://ik.imagekit.io/haochen/Typora/image-20220724225454897.png)

![image-20220724225657261](https://ik.imagekit.io/haochen/Typora/image-20220724225657261.png)

### Deep Understanding

Abstract Rrepresentation

![image-20220724230140060](https://ik.imagekit.io/haochen/Typora/image-20220724230140060.png)

Start with some assumption



Not for controliability



