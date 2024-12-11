---
categories:
- Studies
date: '2024-12-12'
tags:
- LG Aimers
title: '[LG Aimers] Recent Progress of Large Language Models'
toc: true
---


# GPT-3?

- OpenAI’s third-generation Generative Pretrained Transformer
    - A general-purpose algorithm for language understanding and generation(e.g., question answering, translation, or any text writing)
    - 175B parameters(vs 17B of Microsoft’s Turing NLP)
    - Learned from training set of 500B tokens
- The first commercial product of OpenAI
    - The source code remains private
    - Licensed exclusively to Microsoft in September 2020
    - Users can access only via black-box API


# InstructGPT

- Self-supervised language models does not necessrily follow a user’s intent
    - Due to misaligned objectives
    - e.g., predicting the next token on text ~= follow the user’s instructions helpfully
    - Generate untruthful, toxic, or not helpful outputs to the user
- Key idea: fine-tune GPT-3 using human feedback
    - Reinforcement Learning from Human Feedback(RLHF)
    - Uses human preferences as a reward signal to fine-tune models
    - On prompts submitted by customers to the GPT-3 API, labelers provide demonstrations of the desired model behavior, and rank severlal outputs from our models
![](/assets/images/lg_aimers-recent_progress_of_large_language_models/image_20241212_040325_78bbeb5b0c6a45748c3f174e8fb5c6f6.png)


### How?

![](/assets/images/lg_aimers-recent_progress_of_large_language_models/image_20241212_040326_685efe89621e4ef2944e42e744ec1afb.png)

>*1, Supervised fine-tuning(SFT)<br>2. Reward model(RM) training<br>3. Reinforcement learnig via PPO(OpenAI에서 만든 강화학습 알고리즘)*



# Other LLMs


## Anthropic Claude

- Anthropic AI
    - Founded by Ex-researchers of OpenAI in 2021
    - Invested $400M(+10% stake) by Google in 2022
    - A formal partnership with Google Cloud
- Claude(early access only)
    - Carry out similar tasks to ChatGPT
    - Claimed less likely to produce harmful outputs, and more steerable
    - Constitutional AI: Letting AI respond using a simple set of principles as a guid(started with around 10)

### Google Bard

- Google issued ‘Code Red’ over ChatGPT(Nov 2022)
    - Could ChatGPT(partly) replace Google’s search engine?
- Bard is public as of May 2023

### Google PaLM

- Efficient scaling based on Google’s Pathways system
    - A new ML architecture enables training a single model across thousands or tens of thousands of accelerator chips
    - With Pathways, train a 540B model on 6144TPU V4 chips
    - PaLM2 API is available
- Great scaling and breakthrough reasoning capabilities
    - e.g., Multi-hop reasoning, code generation, and joke explanation
    - Multilingual understanding: few-shot demonstration with 540B model
    - Not publicly available

### Meta OPT & LLaMA

- Open Pretrained Transformer(OPT-175B)
    - A series of large causal language models by Meta
    - Decoder-only pre-trained transformers raning from 125M to 175B parameters
    - Similar performance to GPT3 while requiring only 1/7th the carbon footprint to develop
- **L**are **La**nguage Model **M**eta **A**I
    - Available at several sizes(7B, 13B, 33B, and 65B)
    - Trained only on publicly available data

### Self-Instruct Tuning on LLaMA

~~~

