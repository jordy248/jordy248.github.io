Title: 2019-04-05 Riddler
Date: 2019-04-07 09:17
Category: Riddler
Tags: FiveThirtyEight, Riddler, R, probability, combinatorics, simulation
Slug: riddler-2019-04-05
Cover: theme/assets_images/karl-fredrickson-35017-unsplash.jpg
Cover_Credits: Karl Frederickson/Unsplash
Authors: Jordy Nelson
Summary: Are we out of free coffees?
Comments: True

This past weekend's [Riddler Classic](https://fivethirtyeight.com/features/does-your-gift-card-still-have-free-drinks-on-it/) is a neat little coffee combinatorics problem.

> From Michael Branicky, your card has been declined:

> Lucky you! You’ve won two gift cards, each loaded with 50 free drinks from your favorite coffee shop, Riddler Caffei-Nation. The cards look identical, and because you’re not one for record-keeping, you randomly pick one of the cards to pay with each time you get a drink. One day, the clerk tells you that he can’t accept the card you presented to him because it doesn’t have any drink credits left on it.

> What is the probability that the other card still has free drinks on it? How many free drinks can you expect are still available?

The probability that the other card still has free drinks on it is the complement of the probability that both cards are empty &ndash; which is easier to count, so we'll start here!

If both of the cards loaded with 50 drinks are empty when we make our coffee run, this means we've already ordered exactly 100 coffees. 50 of these orders occurred on the card we tried using, and 50 occurred on the other card. The probability of this scenario happening is `((1/2) ^ (100)) * choose(100, 50)` &dash; or just about 8%. **So the probability that that the card we didn't has at least one drink remaining (i.e., that it's not the case that both cards are empty when we order the 101st drink) is about 92%.**

Let's confirm with an R simulation.

First, a little housekeeping:

```R
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

# init cards
cards <- list(card1 = 50,
              card2 = 50)
```

We'll define a little helper function to randomly choose one of the cards as well as a recursive function to simulate buying coffee using our cards:

```R
### ------------------------------ ###
### funs to simulate buying coffee ### ----------------------------------------
### ------------------------------ ###

### --------------------------------------- ###
### fun to randomly choose card from wallet ###
### --------------------------------------- ###
choose_card <- function(wallet) {
        # randomly choose card from cards available in wallet
        card_chosen_idx <- sample(x       = length(wallet),
                                  size    = 1, 
                                  replace = F,
                                  prob    = NULL)
        
        # return
        return(card_chosen_idx)
}

### ----------------------------- ###
### fun to simulate buying coffee ###
### ----------------------------- ###
buy_coffee <- function(wallet) {
        # randomly choose a card from the wallet to use
        card_chosen_idx <- choose_card(wallet)
        
        # break case = chosen card is empty
        if(wallet[[card_chosen_idx]] == 0) {
                return(wallet)
        } else {
                wallet[[card_chosen_idx]] <- wallet[[card_chosen_idx]] - 1
                
                return(buy_coffee(wallet))
        }
}
```

Then we'll simulate a hundred thousand scenarios:

```R
### -------------------- ###
### simulate coffee runs ### --------------------------------------------------
### -------------------- ###

# init vector to hold number of drinks on other card
coffee_runs <- rep(NA,
                   1e5)

# init progress bar
pb <- progress_bar$new(
        format = paste0('simulating coffee runs',
                        '(:spin) [:bar] :percent eta: :eta'),
        total = length(coffee_runs), clear = FALSE, width= 80)

# simulate coffee runs
for(i in 1:length(coffee_runs)) {
        # simulate coffee run
        coffee_run <- buy_coffee(cards)
        
        # store number of drinks on other card
        coffee_runs[i] <- as.integer(coffee_run[which.max(coffee_run)])
        
        # increment progress
        pb$tick()
}
```
Let's what our simulation thinks the probability of the other card having drinks on it is:

```R
### ----------------- ###
### check sim results ### -----------------------------------------------------
### ----------------- ###

# prob other card still has drinks
1 - sum(coffee_runs == 0) / length(coffee_runs)

[1] 0.92041
```

Just over 92% probability that the other card has drinks on it!

And how many drinks can we expect that card to have on it?

```R
mean(coffee_runs)

[1] 7.03834
```
