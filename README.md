# Hyperpartisan Headline Generation with Reinforcement Learning Draft


This is the code implemented for the paper:

**Hyperpartisan Headline Generation with Reinforcement Learning**. Charlotte Ji, Ivanna Peña, Paolla Bruno Dutra 

This code has been written using python3 and is built on top of https://github.com/HLTCHKUST/sensational_headline and https://github.com/HLTCHKUST/hyperpartisan-news-detection

## Repo Description
dataset - contains the train and val set(headline and article) and their labels (hyperpartisan [t/f], bias [left,center,right])  [[/dataset]](https://drive.google.com/drive/folders/1R-Gj1f_ytqEHq98-lRUE7XROxuSzuwrp?usp=sharing)  
/utils/data_utils.py - reading the xml file from dataset and cleaning the text  
/utils/preprocessing.py - loading and cleaning data  
/hyperpartisan_generation.py - hyperpartisan headline generation (modifying /HLTCHKUST/sensational_headline/sensation_generation.py)  
/hyperpartisan_save.py - hyperpartisan headline generation (modifying /HLTCHKUST/sensational_headline/sensation_save.py)  
/train_hyperpartisan_scorer.py - training hyperpartisan scorer (modifying /HLTCHKUST/sensational_headlinetrain_sensational_scorer.py)


## Working on
-Complete Modifying code from /HLTCHKUST/sensational_headline, and /HLTCHKUST/hyperpartisan-news-detection to leverage for our own implementation  
-Complete reading and processing data from SemEval 2019 Task 4  
-Implementing Model  
   -Hyperpartisan scorer  
   -Hyperpartisan headline generator

## Abstract
Discrediting misinformation has shown itself to be a challenging approach in combating the dissemination of different types of yellow journalism. Nudging readers in the direction of better information sources has been an alternative being explored in the data science field. Given how successful biased headlines are in drawing engagement, we decided to  explore hyper partisan title generation as an alternative to technical approaches in combating the spread of misinformation.


## Data
**Data for PAN at SemEval 2019 Task 4: Hyperpartisan News Detection (Version Training and validation v1) [Data set]**. Johannes Kiesel, Maria Mestre, Rishabh Shukla, Emmanuel Vincent, David Corney, Payam Adineh, … Martin Potthast ***2018*** [[Dataset]](http://doi.org/10.5281/zenodo.1489920)

The dataset is labeled by the overall bias of the publisher according to publisher bias lists compiled by BuzzFeed news and Media Bias Fact Check. It is a balanced dataset containing 750,000 articles with headlines, half of which (375,000) are hyperpartisan and half are not. Among the hyperpartisan articles, half(187,500) are biased on the left side of the political spectrum, and the other half are on the right. 


## Dependency
Check the packages needed or simply run the command
```console
❱❱❱ pip install -r requirements.txt
```
