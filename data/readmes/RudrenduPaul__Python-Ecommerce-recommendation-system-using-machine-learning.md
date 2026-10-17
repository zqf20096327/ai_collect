# E-commerce Recommendation System (Python, Amazon & Home Depot datasets)

Open `Recommendation System - Paul.ipynb` for the full analysis and code.

A well-designed recommendation system helps businesses improve the shopping experience on their site, which in turn improves customer acquisition and retention. This project builds one in three parts, following a new customer's actual journey: from their first visit with no purchase history, through their first purchase, to repeat visits once ratings and purchase history exist.

## Datasets

1. Amazon product ratings from multiple users: [Kaggle: Amazon Ratings](https://www.kaggle.com/skillsmuggler/amazon-ratings)
2. Home Depot product descriptions: [Kaggle: Home Depot Product Search Relevance](https://www.kaggle.com/c/home-depot-product-search-relevance/data)

## Strategy

### 1. Popularity-based recommendations for new customers

A new customer with no purchase history is shown the most popular products on the site. This is a simple, effective way to cold-start a recommendation engine before any personal signal exists.

### 2. Model-based collaborative filtering

Once a customer has purchase history, recommendations switch to items based on that history and the ratings of other users who bought similar items. A model-based collaborative filtering approach was chosen here because it predicts products for a specific user by learning patterns across many users' preferences at once.

### 3. Item-item collaborative filtering (cold start for a new business)

For a business with no user-item purchase history at all, recommendations can instead come from a search-engine-style system based on textual clustering of product descriptions: predictions are drawn from other products in the same cluster for a given set of search terms.

---

## Part I: Popularity-based recommendations for new customers

![Most popular products by sales, descending](https://user-images.githubusercontent.com/38769913/51401953-27a90a00-1b1a-11e9-9dca-c18c9d592121.png)

**Analysis:** The chart above ranks products by sales, descending. For example, product ID `B001MA0QY2` has sales of over 7,000, followed by `B0009V1YR8` at around 3,000, and so on.

## Part II: Model-based collaborative filtering

Recommends the top 10 highly correlated products, in sequence, based on a customer's purchase history and the ratings of other customers who bought similar items.

![Top correlated products recommended to a customer based on purchase history](https://user-images.githubusercontent.com/38769913/51402144-a8680600-1b1a-11e9-8c45-3f8177516a48.png)

**Result:** the products shown are the top 10 the recommendation system would surface to this customer, based on the purchase history of other customers on the site.

## Part III: Item-item collaborative filtering (cold start for a new business)

For a business with no purchase or rating history yet, recommendations can be built from textual clustering of product descriptions instead.

**Product clusters (subset of data):**

![Product clusters from text analysis of product descriptions](https://user-images.githubusercontent.com/38769913/51402355-393ee180-1b1b-11e9-9f98-8af45733d496.png)

**Top terms per cluster:**

| Cluster 1 | Cluster 2 | Cluster 3 |
| --- | --- | --- |
| light | painted | water |
| watt | wood | concrete |
| volt | insulation | use |
| led | ft | ft |
| power | primed | metal |
| fan | proposition | used |
| bulb | nbsp | provides |
| bulbs | residents | designed |
| lighting | california | high |
| home | | fiberglass |

Once a cluster is identified from a customer's search terms, the recommendation system displays items from the matching product cluster based on product descriptions.

## Summary

This approach works best when a business is setting up an e-commerce site for the first time and has no user-item purchase or rating history yet: it gives new visitors a reasonable starting recommendation. Once real purchase history accumulates, the system switches to model-based collaborative filtering for more personalized results.

## License

No license file is currently attached to this repository; all rights reserved by default. Open an issue if you'd like to use this code and need clarification on terms.
