---
categories:
- Studies
date: '2024-12-12'
tags:
- LG Aimers
title: '[LG Aimers] SL Foundation'
toc: true
---


# SL pipeline

![](/assets/images/lg_aimers-sl_foundation/image_20241212_040345_1d6114c4b8884c1780b126ac92ea5989.png)



# Learning model

1. Goal: target function 
    - $f : X→Y$
1. Training set
    - $D = \{x_t, y_t\}_{t=1}^N$
1. Learning model
    1. Feature selection
        1. feature vector $$\mathbb{R}^d$$(a d-dimensional Euclidean space)
    1. Model selection
        1. Lineal model
        1. Neural network
        1. etc…
    1. Optimization
1. Hypothesis/Evaluation
    - $g \approx f$


# Model Generalization

- Learning is an ill-posed problem; data is limited to find a unique solution
- Generalization(Goal) : a model needs to perform well on unseen data
    - Generalization error $$E_{gen}$$ ; the goal is to minimize this error, but it is impractical to compute in the real world
    - Learning from data → Learning from error(supervision)
- Use training/validation/test set errors for the proxy


# Errors

- Pointwise error is measure on an each input sample: $$e(h(x), y)$$(모델의 출력, 정답)
- Examples:
    - Squared error : $$e(h(x_i), y_i) = (h(x_i)-y_i)^2$$
    - Binary error : $$e(h(x_i), y_i) = 1[h(x_i) ≠ y_i]$$
- From a pointwise error to overall errors (loss function or cost function)
    - $E[(h(x_i) - y_i)^2]$

## Training Error

- Measured on a training set, which may or may not represent $$E_{gen}$$
- Used for fitting a model

## Testing Error

- Not used in training, which can be used for a proxy of $$E_{gen}$$

## Methods

Goal in training: $$E_{test} \approx E_{gen} \approx 0$$

- Split into two objectives:
    1. $E_{test} \approx E_{train}$
    1. $E_{train} \approx 0$
- Objective 1: make $E_{test} \approx E_{train}$
    - Failure : Overfitting → high variance
    - Cure : Regualarization; more data
- Objective 2: make $$E_{train} \approx 0$$
    - Failure : Underfitting → high bias
    - Cure : Optimization; more complex model


# Bias and Variance

- Bias : Error because the model can not represent the concept
- Variance : Error because a model overreacts to small changes(noise) in the training data
- Total Loss = Bias + Variance (+ noise)

### Underfitting

- Caused by using too simpler model than actual data distribution(high bias)

### Overfitting

- Caused by using more complex model than actual data distribution(high variance)

## Bias-Variance trad-off

The two objects have trade-off between approximation and generalization w.r.t model complexity

![](/assets/images/lg_aimers-sl_foundation/image_20241212_040353_885f444005da4efa8f76e5660aed4462.png)



# Avoid Overfitting


### Problem

Nowadays, a complex model tends to be used to handle high-dimensional data(and relatively insufficient number of data); prone to an overfitting problem


### Curse of dimension

Increase the dimension of the data to improve the performance as well as maintain the density of the examples per bin

→ We need to increase the data exponentially


### Remedy

- Data augmentation
    - **Regularization** to penalize complex models(variance reduction); make a model not too sensitive to noise or outliers(e.g., drop0out, LASSO)
    - **Ensemble**: average over a number of models


# Cross-validation (CV)

![](/assets/images/lg_aimers-sl_foundation/image_20241212_040354_041d2ffac6d94ebebfd63643db445fc4.png)

- **Training data set** - used to train a model to fit data
- **Validation data set** - used to provide unbiased evaluation of the model’s fitness
- **Test data set** - never been used in the training
Cross-validation allows a better model to avoid overfitting(but more complexity)


