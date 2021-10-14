Title: 2019-12-15 Riddler
Date: 2019-12-15 16:33
Category: Riddler
Tags: FiveThirtyEight, Riddler, R, probability, simulation, binomial
Slug: riddler-2019-12-15
Cover: theme/assets_images/randy-fath-dELtyCFlNG0-unsplash.jpg
Cover_Credits: Randy Fath/Unsplash
Authors: Jordy Nelson
Summary: Choose 'K' (Karpov or Kasparov)
Comments: True

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
 "HTML-CSS": { linebreaks: { automatic: true } },
         SVG: { linebreaks: { automatic: true } }
});
</script>

The newest [Riddler Express](https://fivethirtyeight.com/features/can-you-solve-a-particularly-prismatic-puzzle/) is a probability puzzler that asks us to "choose K" (Karpov or Kasparov!) in one of chess's great matches.

> From Anna Engelsone comes a riddle about a historic chess battle:

> The infamous 1984 World Chess Championship match between the reigning world champion Anatoly Karpov and 21-year-old Garry Kasparov was supposed to have been played until either player had won six games. Instead, it went on for 48 games: Karpov won five, Kasparov won 3, and the other 40 games each ended in a draw. Alas, the match was controversially terminated without a winner.

> We can deduce from the games Karpov and Kasparov played that, independently of other games, Karpov’s chances of winning each game were 5/48, Kasparov’s chances were 3/48, and the chances of a draw were 40/48. Had the match been allowed to continue indefinitely, what would have been Kasparov’s chances of eventually winning the match?

Draws don't give us any additional information on the slog to a winner, so let's go ahead and ignore them, leaving us with these new probabilities:

Karpov: $\frac{5}{8}$
<br />
Kasparov: $\frac{3}{8}$

And because Karpov has already won five games on his way to six, Kasparov needs to win 3 in a row (before Karpov wins one more) to claim his own victory. 

This then becomes a question for the binomial distribution. The binomial distribution takes the parameters $n$ and $p$ and the form $X \sim Bin(n,p) = {n \choose k} * p^k * (1-p)^{(n-k)}$ (where $n$ is the number of trials, $p$ is the probability of the event occurring, and $k$ is the number of times we want the event to occur).

In Kasparov's case, this becomes: ${3 \choose 3} * (\frac{3}{8})^3 * (1-\frac{3}{8})^{(3-3)}$. This is the same as $\frac{3}{8}^3 = \frac{27}{512}$. Or 0.05273438.

And as always, we can simulate with R:

```{R}
##### ----------------- #####
##### ----------------- #####
##### clean environment #####
##### ----------------- #####
##### ----------------- #####
rm(list=ls())
gc()

##### ------------- #####
##### ------------- #####
##### load packages #####
##### ------------- #####
##### ------------- #####
library(progress)

##### ------- #####
##### ------- #####
##### configs #####
##### ------- #####
##### ------- #####
set.seed(42)

n_sim   <- 1e5

matchup <- list('karpov'   = list('prob' = 5/48,
                                  'outs' = 5),
                'kasparov' = list('prob' = 3/48,
                                  'outs' = 3),
                'draw'     = list('prob' = 40/48,
                                  'outs' = 0))

##### -------- #####
##### -------- #####
##### def funs #####
##### -------- #####
##### -------- #####

### -------------------------------------- ###
### def game() fun to simulate single game ###
### -------------------------------------- ###
game <- function(matchup) {
    res <- sample(x       = names(matchup),
                  size    = 1,
                  replace = F,
                  prob    = unlist(matchup)[grepl('prob', names(unlist(matchup)))])
    
    return(res)
}

### ------------------------------------------- ###
### def match() fun to simulate match to 6 wins ###
### ------------------------------------------- ###
match <- function(matchup) {
    curr_matchup <- matchup
    
    while(sum(unlist(curr_matchup)[grepl('(karpov|kasparov)\\.outs', names(unlist(curr_matchup)))] == 6) == 0) {
        game_out <- game(curr_matchup)
        
        curr_matchup[[game_out]][['outs']] <- curr_matchup[[game_out]][['outs']] + 1
    }
    return(curr_matchup)
}

##### ---------------- #####
##### ---------------- #####
##### simulate matches #####
##### ---------------- #####
##### ---------------- #####

### ----------------- ###
### init progress bar ###
### ----------------- ###
pb <- progress_bar$new(
    format = paste0('simulating matches...', 
                    '(:spin) [:bar] :percent eta: :eta'),
    total = n_sim, clear = FALSE, width = 100)

### ------------------------ ###
### init vec to hold winners ###
### ------------------------ ###
winner       <- vector()
games_played <- vector()

### -------- ###
### simulate ###
### -------- ###
for(i in 1:n_sim) {
    match_out <- match(matchup)
    
    karpov_out   <- match_out[['karpov']][['outs']]
    kasparov_out <- match_out[['kasparov']][['outs']] 
    draws_out    <- match_out[['draw']][['outs']]
    
    n_games      <- karpov_out + kasparov_out + draws_out
    
    if(karpov_out > kasparov_out) {
        winner <- c(winner, 'karpov')
    } else {
        winner <- c(winner, 'kasparov')
    }
    
    games_played <- c(games_played, n_games)
    
    pb$tick()
}

### ------------------------ ###
### prob of kasparov winning ###
### ------------------------ ###
length(winner[winner == 'kasparov']) / length(winner)
```

Which gives us: 0.05315