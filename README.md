# Watson

DISCLAIMER: This project is a Work in Progress.

Collaborative filtering using SVD.

## Goals

1. Recommendation for items for a single user based on its buying history
2. Recommendation for items, not previously bought, for a single user based on its buying history and other simular users (Item-Item Collaborative Filtering)
3. Other users bought X also bought Y (Item-Item Collaborative Filtering)
4. Recommend similar (categorical) product (Content-Based)

## Scoring
Items can be ranked based on the frequency on which items are bought. An item that was bought 10 times has a 10 times higher score as a product that has been bought only once.
Feature scaling must be applied to normalise the scores.

## Sources
1. [Recommender Systems: An Introduction](https://www.amazon.com/Recommender-Systems-Introduction-Dietmar-Jannach/dp/0521493366) by Dietmar Jannach by Dietmar Jannach, Markus Zanker, Alexander Felfernig, Gerhard Friedrich.
2. Cambridge Spark - [Implementing your own recommender systems in Python](https://cambridgespark.com/content/tutorials/implementing-your-own-recommender-systems-in-Python/index.html)

