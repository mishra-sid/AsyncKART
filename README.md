# AsyncKART : LEARNING TO PLAY MARIO KART WITH DEEP REINFORCEMENT LEARNING USING ASYNCHRONOUS ACTOR CRITIC METHOD 

## OBJECTIVE

The goal of the project is to train Mario Kart ( A racing game )'s character to be able to maintain itself along a track from just the visual feedback that we see during playing the game and use game's inbuilt reward parameters to train a model using RL with Asynchronous actor critic method to stabilize each other(agents) . 

## PROPOSED METHODOLOGY

The following is our step-by-step plan:

* Use a game engine with python interface compatibility to extract visual feedback information available here [[3]](#bookmark=id.mqubqm87xx17).

* Add appropriate lua scripts to have cross-platform keyboard support for start/exit or manual mode.

* Implement Reinforcement learning using Asynchronous actor critic (A3C agents) using Tensorflow.

* Process the visual feedback received from the gameâs display to get location information of racer and surroundings.

* Provide an interface with a python script to train this model from the processed visual feedback using the learning model designed at 3rd step. 

* Test the trained model by letting it race on a new track in which it hadnât been trained before and evaluate its performance. 

## CONTRIBUTION

* This training of model being asynchronous uses comparatively far less resources and hence can be used in training self driving cars online effectively.

* The existing approaches have been using Imitation learning methods like offline search, DAGGER etc. 

    * They are effective provided large data but they are upper bounded by expertâs ability.

    * Also experts rarely makes an error, so the error recovery probability is low, in contrast RL learns from its mistakes and trains to get a better reward each time, so it has richer practical applications in real time risk sensitive self driving scenarios.

* It can also act as an reinforcement layer in already existing imitation based methods to get the best of both worlds and hopefully get a optimal performance.  

## DATASET 

The processed visual feedback extracted acts like a dataset for training the required  model.

## EXPERIMENTS AND PERFORMANCE METRICS TO BE EVALUATED

#### Resource computation : Comparison of resource required by a general RL method and A3C. 

#### Expected results 

General RL method would need GPU clusters to be able to train in a feasible amount of time whereas A3C would hardly need a normal multicore CPU to do the same in half the time as mentioned in [[1] ](#bookmark=id.7ldpn4gg9uty).

* Comparison with imitation based methods: 

Comparison with the published metrics by imitation based methods in [[2] . ](#bookmark=id.dtj1kpq7kj31) 

* Expected results : 

Imitation based methods given large data should have higher accuracy, but it will be bounded by expert's way of playing and will not generalize well.

The error recovery from dead ends should be better in case of RL A3C method. 

REFERENCES:

[1] [https://arxiv.org/abs/1602.01783](https://arxiv.org/abs/1602.01783) ( Paper for comparison of A3C against other methods for  performing RL )

[2] [http://cs231n.stanford.edu/reports/2017/pdfs/624.pdf](http://cs231n.stanford.edu/reports/2017/pdfs/624.pdf) : CNNs, Offline Search using Monte Carlo methods and DAGGER ( Imitation based approaches already used before for performance metric comparisons )

[3] [https://github.com/kevinhughes27/TensorKart](https://github.com/kevinhughes27/TensorKart) : Used just for the game engine and python interface compatibility. 

