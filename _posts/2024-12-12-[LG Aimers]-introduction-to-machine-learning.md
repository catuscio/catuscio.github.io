---
categories:
- Studies
date: '2024-12-12'
tags:
- LG Aimers
title: '[LG Aimers] Introduction to Machine Learning'
toc: true
---


### 서울대학교 김건희 교수


# Machine Learning(ML)

> A branch of artificial intelligence, concerned with the design and development of algorithms that allow computers to evolve behaviors based on empirical data


- Herbert Simon’s def.
> Learning is any process by which a system improves performance from experience

- Arthur Smuel’s definition
> Machine Learning is a field of study that gives computers the ability to learn without being explicitly programmed

- Tom Mitchell’s def.
> A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.

> 💡 Machine Learning improve task T, with respect to performance metric P, based on experience E.
- T : playing chess
- P : percentage of games won against an opponent
- E : playing practice games against itself

![](/assets/images/lg_aimers-introduction_to_machine_learning/image_20241212_034152_0957c699870546ae8452fc34ba5000d1.png)

>*Traditional programming VS. Machine Learning*


# Goal of ML: Generalization(일반화)


### Definition of learning

- A form of abstraction where common properties of specific instances are formulated as general concepts or claims.
- It extracts the essence of a concept based on its analysis of similarities from many discrete objects.

### Objective of learning

- Not to learn an exact representation of the training data itself
- To build a statistical model of the process that generates the data

# No Free Lunch Theorem for ML

- No machine learning algorithm is universally any better than any othe
- “NO ABSOLUTE BEST ALGORITHM”

# Types of Learning


## Supervised Learning

- Training data includes desired outputs
> 💡 Given $$(x_1, y_1), (x_2, y_2), …, (x_n, y_n)$$, learn a function $$f(x)$$ to predict $$y$$ given $$x$$.

- Classification: $$y$$ is categorical
- Regression: $$y$$ is continuous
- $$x$$ can be multi-dimensional
![](/assets/images/lg_aimers-introduction_to_machine_learning/image_20241212_034153_74f022fa978a419fbca250204d219f8f.png)


## Unsupervised Learning

Training data does not include desired outputs

> 💡 Given $$x_1, x_2, …, x_n$$, find a hidden structure(e.g., clusters)

- Classification: $$y$$ is categorical
- Clustering, anomaly detection, density estimation, … e.g., Genomics: group individuals by genetic similarity
![](/assets/images/lg_aimers-introduction_to_machine_learning/image_20241212_034154_151cc3101deb4fec8f1cd433cda6a8b2.png)


## Semi-supervised learning

Some of training data includes desired outputs

- One of the bottlenecks of learning is the labeling of examples.
- Often done manually and time consuming
- Can we label only a small number of examples and make use of a large number of unlabeled examples to learn? Possible in many cases!
Two scenarios

- LU learning: Learning with a small set of Labeled examples and a large set of Unlabeled examples
- PU learning: Learning with Positive and Unlabeled examples(no labeled negative examples)
(LU와는 다르게 PU는 모든 클래스에 대한 몇 개의 레이블 데이터를 주는 게 아니라, 특정 클래스에 한해서만 레이블 데이터를 제공)

![](/assets/images/lg_aimers-introduction_to_machine_learning/image_20241212_034155_ce588f25f524446e833b7a2f794c4dff.png)

Similar data points have similar labels; unlabeled data can help identify the boundary more accurately.


## Reinforcement Learning

No fixed dataset but an environment

Rewards from sequence of actions

- A feedback loop between the learning system and its environment
    - Does not experience a fixed dataset
    - No supervisor, but only rewards(Learning “fills in the details”)
    - Feedback could be delyed, not instantaneous
    - Agent’s actions affect the subsequent data it receives
![](/assets/images/lg_aimers-introduction_to_machine_learning/image_20241212_034157_f3df52ced49742b29ba7030cf07c70ec.png)

