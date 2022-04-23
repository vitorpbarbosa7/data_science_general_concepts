# LightGBM Parameters in my words

- objective: 
  - multiclass
  - binary
  - regression
  - ... among other examples

- boosting_type:
  - dart: Dropouts meet Multiple Additive Regression Trees
  - gbdt
  - rf
  - ...

- tree_learner:


- bagging_fraction:
    -  Randomly select part of your data to train the model
    -  Must enable baggint_freq to nonzero value too 

- pos_bagging_fraction:
    -  Used only in binary classification
    -  Used for imbalanced binary classification
    -  Randomly sample positive samples in bagging
  
- neg_bagging_fraction:
    - Used in conjuction with pos_bagging_fraction


- feature_fraction:
    - Randomly select a subset of features on each iteration

- feature_fraction_by_node
    - Fraction of feature to consider at each node to split