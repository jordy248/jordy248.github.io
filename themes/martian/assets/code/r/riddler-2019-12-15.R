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



























