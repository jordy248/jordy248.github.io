Title: 2019-03-29 Riddler
Date: 2019-04-01 08:22
Category: Riddler
Tags: FiveThirtyEight, Riddler, R, probability, simulation
Slug: riddler-2019-03-29
Cover: theme/assets_images/jack-anstey-383370-unsplash.jpg
Cover_Credits: Jack Anstey/Unsplash
Authors: Jordy Nelson
Summary: Have we already seen these cards?
Comments: True

Last weekend's [Riddler Express](https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/) combines two super fun things: board games and probability!

> From Tom Hanrahan, a probability puzzle; or, a mini-lesson in surprising results:

> You are playing your first ever game of “Ticket to Ride,” a board game in which players compete to lay down railroad while getting so competitive they risk ruining their marriages. At the start of the game, you are randomly dealt a set of three Destination Tickets out of a deck of 30 different tickets. Each reveals the two terminals you must connect with a railroad to receive points. During the game, you eventually pick up another set of three Destination Tickets, so you have now seen six of the 30 tickets in the game.

> Later, because you enjoyed it so much, you and your friends play a second game. The ticket cards are all returned and reshuffled. Again, you are dealt a set of three tickets to begin play. Which is more likely: that you had seen at least one of these three tickets before, or that they were all new to you?

Let's decompose this into some steps:

* In the first game, we're originally dealt three Destination Tickets at the beginning of the game and subsequently pick up another three Destination Tickets for a total of six Destination Tickets out of 30 unique options.  

* In the second game, we're originally dealt three Destination Tickets and then ask: "Is it more likely that one of these three cards was in my hand during the first game or that none of these cards were in my hand during the first game?  

If we saw six out of 30 unique cards in the first game, that means that we start the second game with 24 out of the 30 cards that we weren't dealt. So in the second game, the first card we're dealt has (30-6-0/30) probability of being new to us, the second card has a (30-6-1)/(30-1) probability of being new to us, and the third card has a (30-6-2)/(30-2) probability of being new to us. So the probability of all three cards being new to us is 24/30 * 23/29 * 22/28 = 0.4985222. In other words, there's a ~49.85% chance we haven't seen any of the three cards we're dealt in the second game &ndash; or a ~50.15% chance we have seen at least one, making it ever-so-slightly more likely that we've already seen at least one of the first three cards we're dealt in the second game.

With such razor-thin odds in favor of the first three cards we're dealt in the second game being unseen, I was curious to see whether a simulation coded up in R would confirm this result.

```R
# riddler
# 2019-03-29

##### ------- #####
##### ------- #####
##### EXPRESS ##### -----------------------------------------------------------
##### ------- #####
##### ------- #####

if(F) {
        '
        Riddler Express
        From Tom Hanrahan, a probability puzzle; or, a mini-lesson in 
        surprising results:
        
        You are playing your first ever game of "Ticket to Ride," 
        a board game in which players compete to lay down railroad
        while getting so competitive they risk ruining their marriages.
        At the start of the game, you are randomly dealt a set of three D
        estination Tickets out of a deck of 30 different tickets. Each reveals
        the two terminals you must connect with a railroad to receive points. 
        During the game, you eventually pick up another set of three 
        Destination Tickets, so you have now seen six of the 30 tickets in the 
        game.
        
        Later, because you enjoyed it so much, you and your friends play a 
        second game. The ticket cards are all returned and reshuffled. Again,
        you are dealt a set of three tickets to begin play. Which is more 
        likely: that you had seen at least one of these three tickets before, 
        or that they were all new to you?
        '
}

### ---- ###
### init ### ------------------------------------------------------------------
### ---- ###
rm(list=ls())
gc()

### --------- ###
### load libs ###
### --------- ###
library(progress)
library(tidyverse)

### ------ ###
### params ###
### ------ ###
set.seed <- 42
terminals <- 1:30

### ----------------------- ###
### fun to simulate dealing ### -----------------------------------------------
### ----------------------- ###
deal <- function(deck,
                 n_cards) {
        
        hand <- sample(x       = deck,
                       size    = n_cards,
                       replace = F)
        
        deck <- deck[-hand]
        
        # return
        res <- list(hand = hand,
                    deck = deck)
        return(res)
}

### ----------------------------- ###
### simulate ticket to ride games ### -----------------------------------------
### ----------------------------- ###

# init vector to hold flags for games with dupe terminals
dupe_terminals <- rep(0L,
                      1e6)

# init progress bar
pb <- progress_bar$new(
        format = paste0('simulating hands',
                        '(:spin) [:bar] :percent eta: :eta'),
        total = length(dupe_terminals), clear = FALSE, width= 80)

# simulate two games and update dupe_terminals for matches
for(i in 1:length(dupe_terminals)) {
        
        # simulate games
        game_1 <- deal(deck      = terminals, 
                       n_cards = 6)
        
        game_2 <- deal(deck      = terminals, 
                       n_cards = 3)
        
        # get hands from simulated games
        hand_game_1 <- game_1$hand
        
        hand_game_2 <- game_2$hand
        
        # check for dupes and update dupe_terminals
        if(sum(hand_game_1 %in% hand_game_2) > 0) {
                dupe_terminals[i] <- 1L
        }
        
        # init progress
        pb$tick()
        
}

### -------- ###
### calc res ### --------------------------------------------------------------
### -------- ###

# second games that included at least one card that was seen in game 1
sum(dupe_terminals)/length(dupe_terminals)
```

```R
[1] 0.501665
```

Over the course of a million simulations, we roughly match our computed result above. And we can watch the simulations converge on this result:

```R
### -------- ###
### plot res ### --------------------------------------------------------------
### -------- ###
df <- data.frame(samples = 1:length(dupe_terminals),
                 dat     = dupe_terminals) %>%
        mutate(running_rate = cumsum(dat) / samples)

df %>%
        ggplot() +
        geom_line(aes(x = log(samples),
                      y = running_rate))

```

![Riddler Express 2019-03-29 Plot](../../theme/assets_images/riddler_express_2019-03-29.png "Riddler Express 2019-03-29 Plot")
