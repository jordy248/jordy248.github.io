Title: 2019-10-04 Riddler
Date: 2019-10-06 19:36
Category: Riddler
Tags: FiveThirtyEight, Riddler, R, probability, conditional probability, bayes
Slug: riddler-2019-10-04
Cover: theme/assets_images/NeONBRAND-dollar-unsplash.jpg
Cover_Credits: Gary NeONBRAND/Unsplash
Authors: Jordy Nelson
Summary: Should we lock in our answer for $1MM?
Comments: True

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
 "HTML-CSS": { linebreaks: { automatic: true } },
         SVG: { linebreaks: { automatic: true } }
});
</script>

The most recent [Riddler Express](https://fivethirtyeight.com/features/who-wants-to-be-a-riddler-millionaire/) puts you in the hot seat for a gameshow-themed conditional probability adventure -- all without even mentioning Monty Hall or goats!

> From Thomas Sneller comes a puzzle that brings us back to the game show to end all game shows, “Who Wants to Be a Riddler Millionaire?” As you’ll remember, for each question you must pick the correct option from four choices.

> You’ve made it to the $1 million question, but it’s a tough one. Out of the four choices, A, B, C and D, you’re 70 percent sure the answer is B, and none of the remaining choices looks more plausible than another. You decide to use your final lifeline, the 50:50, which leaves you with two possible answers, one of them correct. Lo and behold, B remains an option! How confident are you now that B is the correct answer?

Let's first summarize the probabilities and values of success (as success is in the eye of the batter) for each team:

If we begin by allocating 70% of our credibility to B and evenly distribute the remaining 30% among the remaining 3 answers (A, C, and D), it's tempting to believe that elimating two of the remaining 3 options means that their share of the 30% of our credibility all flows to answer B, bumping it to 90%.

But is there a better way to reallocate our credibility in light of our 50:50?

There is if we apply Bayes' Theorem! It gives us a mechanism for updating our prior beliefs (expressed in terms of probabilities or credibilities) in light of additional information.

Bayes' Theorem takes the general form: $P(A|B)=\frac{P(B|A)P(A)}{P(B)}$

In other words, the conditional probability of event A given event B is equal to the conditional probability of event B given event A multiplied by the independent (or marginal) probability of event A all divided by the marginal probability of event B.

In our case, this means: 

<div class="mathjax-scale">$$P(\text{B is the answer}|\text{50:50 returns B})=$$</div>
<div class="mathjax-scale">$$\frac{P(\text{50:50 returns B}|\text{B is the answer})P(\text{B is the answer})}{P(\text{50:50 returns B})}$$</div>

Let's break this down a bit:

* <div class="mathjax-scale">$P(\text{B is the answer}|\text{50:50 returns B})$</div> -- or <div class="mathjax-scale">$P(A|B)$</div> -- is the unknown conditional probability we are trying to solve for.
* <div class="mathjax-scale">$P(\text{50:50 returns B}|\text{B is the answer})$</div> -- or <div class="mathjax-scale">$P(B|A)$</div> -- is equal to 100% because if B is the answer, 50:50 necessarily leaves it (as well as one other answer that we don't care about specifically).
* <div class="mathjax-scale">$P(\text{B is the answer})$</div> -- or <div class="mathjax-scale">$P(A)$</div> -- is the event we assign 70% marginal credibility to from the outset.
* <div class="mathjax-scale">$P(\text{50:50 returns B})$</div> -- or <div class="mathjax-scale">$P(B)$</div> -- can be assigned 79% credibility.
    * There are two cases in which B can remain after the 50:50, and we need to account for both of them:
        * B can remain after the 50:50 **if B is correct**:
            + The probability of this is the probability that B is correct ($P(A)=70\%$) times the probability that B remains after the 50:50 given that B is correct ($P(B|A)=100\%$)
        * B can remain after the 50:50 **if B is incorrect and it happens to be returned by 50:50 along with the correct answer**:
            + The probability of this is the joint probability that B is incorrect (or 30%) and that B remains after the 50:50. If we assume that the answer is, say, A (though this holds regardless of which non-B answer we assume is correct), possible tuples resulting from the 50:50 are $\{A,B\}$, $\{A,C\}$, and $\{A,D\}$. We notice that B appears in 1 out of 3, or 30%.
        * Thus, the probability that B remains after the 50:50 is $(0.7 * 1)+(0.3 * 0.3)=0.79$

Now we can just plug in these quantities and solve:

$P(A|B)=\frac{1 * 0.7}{0.79}$

Which gives us $P(A|B)=\frac{0.7}{0.79}=0.8860759$

So if we originally assign 70% credibility to answer B and it remains after our 50:50, we can then reasonably assign 88.6% credibility to answer B, according to Bayes' Theorem.
