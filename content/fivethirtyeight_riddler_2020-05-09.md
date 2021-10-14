Title: 2020-05-09 Riddler
Date: 2020-05-09 14:42
Category: Riddler
Tags: FiveThirtyEight, Riddler, R, probability, simulation, conditional probability, joint probability
Slug: riddler-2020-05-09
Cover: theme/assets_images/tatiana-rodriguez-XEn-Pvif5Q0-unsplash.jpg
Cover_Credits: Tatiana Rodriguez/Unsplash
Authors: Jordy Nelson
Summary: Six marks the dot. 
Comments: True

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
 "HTML-CSS": { linebreaks: { automatic: true } },
         SVG: { linebreaks: { automatic: true } }
});
</script>

The newest [Riddler Express](https://fivethirtyeight.com/features/can-you-eat-an-apple-like-a-toddler/) is a simple probability problem duo:

> From Dee Harley comes a devilish matter of dominos:

> In a set of dominos, each tile has two sides with a number of dots on each side: zero, one, two, three, four, five or six. There are 28 total tiles, with each number of dots appearing alongside each other number (including itself) on a single tile.

> Question 1: What is the probability of drawing a "double" from a set of dominoes &ndash; that is, a tile with the same number on both sides?

> Question 2: Now you pick a random tile from the set and uncover only one side, revealing that it has six dots. What’s the probability that this tile is a double, with six on both sides?

With 7 dot options for each face (each half) of each domino tile, there are $\frac{{7 \choose 1}}{{7 \choose 1} + {7 \choose 2}}$ ways of drawing a double &ndash; or 25%, which intuitively makes sense given that there are 7 doubles out of 28 total tiles. 

For fun, let's simulate:

```{python}
import numpy as np
from random import choice, seed
from scipy.stats import binom
from scipy.special import comb
from itertools import combinations, chain
from collections import Counter

seed(42)

class Dominoes:
    """
    Initiates a Dominoes() class 
    with range(0, n) dots per tile side
    and r sides per domino tile.
    
    gen_dominoes() generates the tiles.
    
    draw_domino() draws a random tile and removes it from the pool.
    """
    def __init__(self, faces: list, sides: int):
        self.faces = faces
        self.sides = sides
    
    def gen_dominoes(self):
        dominoes = list(itertools.combinations(iterable = self.faces, 
                                               r        = self.sides))
        for face in self.faces:
            ditto_domino = tuple(np.repeat(face, self.sides))
            dominoes.append(ditto_domino)
        self.dominoes = dominoes
        
    def draw_domino(self):
        domino = choice(self.dominoes)
        self.dominoes.remove(domino)
        return domino

# Q1
dupe_draws = 0
n = 100000
for i in range(0, n):
    d = Dominoes(faces = range(0, 7),
             sides = 2)
    d.gen_dominoes()
    draw = d.draw_domino()
    if draw[0] == draw[1]:
        dupe_draws += 1

dupe_draws / n
```
Which gives us `0.25144`.

If we first peek at one of the sides and notice a 6 after drawing a domino, things get a bit trickier. 

Conditional probability tells us how to find the probability of some event of interest (that we don't know the probability of) given some other event (that we do know the probability of):

$$P(A | B) = \frac{P(A \cap B)}{P(B)}$$

Or:

$$P({drawing \enspace a \enspace (6,6)} | {seeing \enspace a \enspace 6}) = \frac{P({drawing \enspace a \enspace (6,6)} \cap {seeing \enspace a \enspace 6})}{P({seeing \enspace a \enspace 6})}$$

But how much information does peeking and seeing a six really give us?

Let's quickly investigate the probability of looking at a random face and seeing a six.

```{python}
d = Dominoes(faces = range(0, 7),
             sides = 2)
d.gen_dominoes()

# tally up frequencies of dot counts on faces (tile halves)
#face_counts = Counter(y for x in d.dominoes for y in x)
face_counts = Counter(chain(*d.dominoes))

# faces with six dots
six_dot_faces = face_counts[6]

# proability of seeing a six
six_dot_faces / sum([v for v in face_counts.values()])
```
Which gives us `0.14285714285714285` &ndash; or 1/7.

Peeking and seeing a six doesn't give us any important information (other than knowing that we're looking at a valid domino face).

Intuitively, this immediately means that the probability of the other side of our tile also being a six (i.e., our tile being a double) is the same as the probability of drawing *any* double: 1/4. 

We can confirm this by computing the joint probability $$P({drawing \enspace a \enspace (6,6)} \cap {seeing \enspace a \enspace 6})$$ and plugging and chugging in our conditional probability formulation.

$$P({drawing \enspace a \enspace (6,6)} \cap {seeing \enspace a \enspace 6})$$ is simply the probability of drawing the (6,6) tile &ndash; which is 1/28.

So we end up with:

$$P({drawing \enspace a \enspace (6,6)} | {seeing \enspace a \enspace 6}) = \frac{1/28}{P(1/7)} = 1/4$$

