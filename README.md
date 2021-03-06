# Hyperpartisan Headline Generation with Reinforcement Learning


This is the code implemented for the paper:

**Hyperpartisan Headline Generation with Reinforcement Learning**. Charlotte Ji, Ivanna Peña, Paolla Bruno Dutra 

This code has been written using python3 and is built on top of https://github.com/HLTCHKUST/sensational_headline , https://github.com/HLTCHKUST/hyperpartisan-news-detection and https://github.com/udibr/headlines

## Repo Description


## Abstract
Discrediting misinformation has shown itself to be a challenging approach in combating the dissemination of yellow journalism.  Nudging readers in the direction of better sources of information has been an alternative explored in the data science field.   Given how successful biased headlines are in drawing engagement,we explore hyper partisan title generation as an alternative to common approaches - that rely on informing bias levels - in  combating the spread of misinformation.

## Data
**Data for PAN at SemEval 2019 Task 4: Hyperpartisan News Detection (Version Training and validation v1) [Data set]**. Johannes Kiesel, Maria Mestre, Rishabh Shukla, Emmanuel Vincent, David Corney, Payam Adineh, … Martin Potthast ***2018*** [[Dataset]](http://doi.org/10.5281/zenodo.1489920)

The dataset is labeled by the overall bias of the publisher according to publisher bias lists compiled by BuzzFeed news and Media Bias Fact Check. It is a balanced dataset containing 750,000 articles with headlines, half of which (375,000) are hyperpartisan and half are not. Among the hyperpartisan articles, half(187,500) are biased on the left side of the political spectrum, and the other half are on the right. 

## Resources Needed
The dataset used for this project can be found[[/here]](https://drive.google.com/open?id=1JgxOrtXKKhwj1hNRHnUDQoWCJXXP9NDx)  

The code is running with jupyter notebook and could be viewed on Google Colab [[/here]](https://drive.google.com/drive/folders/1R-Gj1f_ytqEHq98-lRUE7XROxuSzuwrp?usp=sharing)  

Results of training the hyperpartisan scorer and headline generator can also be found at the link above.

## Dependency
Check the packages needed or simply run the command
```console
❱❱❱ pip install -r requirements.txt
```
