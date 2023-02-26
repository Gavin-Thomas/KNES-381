# <p align="center">My Foray into Machine Learning (DRAFT)</p>

### <p align="center"> A KNES 381 Final Project</p>
#### <p align="center">By Gavin Thomas</p>

### Prologue

  _On the day I stepped into the kinesiology computer lab at the University of Calgary, little did I know that the class I was about to begin would have a profound impact on my personal and professional development, and inspire me to integrate technology with my career. Over the past few months this course has reinvigorated my love for learning, as I have found something I am passionate about. That is... learning to code and applying it to real world settings._
  
  Disclaimer: I am a complete beginner and am in no stretch of the imagination technically proficient in machine learning or data science (yet). However, through many hours of banging my head against my keyboard, I have actually figured out a few things and have found this process of applying code to real-world problems to be very fruitful.
  
### Project Background & Preparation

As a kinesiology student with an interest for healthcare, I have chosen to complete and build a machine learning model to predict wait times for priority medical procedures in Canada. The reason I chose this project is two-fold:

1. The current healthcare system in Canada is faced with a significant backlog, which results in extended wait times for patients, sometimes up to a year or two for priority procedures. I understand that policy changes at the government level are required to address the current state of the healthcare system. However, I believe that machine learning can play a crucial role in improving the efficiency of the healthcare system and also can play a role in providing the public with easy to access insights on their expected wait time.

2. The Canadian Institute for Health Information (CIHI) has made their data tables publicly available for analysis. This is a privilege, and I have chosen to leverage this opportunity to explore the potential of machine learning in healthcare. By building a machine learning model, I aim to supplement my analysis of the CIHI data and gain a better understanding of the capabilities of this technology. 

How did I prepare for this project?
* The KNES 381 Class material (Majority of my learning)
* 100 Days of Code (UDEMY) Course
* Hands-On Machine Learning with Scikit-Learn & Tensorflow (great book)
* Kaggle Microcourses
  
### The Dataset
1. Canadian Institute for Health Information. _Wait Times for Priority Procedures in Canada — Data Tables._ Ottawa, ON: CIHI; 2022.

This dataset describes wait times for priority based off province of residence, Region, indicator (procedure required), Metric (Wait time Percentile), Data Year, and Indicator Result (Time to Treatment).

**How did I modify/clean the dataset to improve my analysis clarity?**
- Province (Territories not included)
- Indicator (Not all priority procedures were included in this dataset; emphasis on joint replacements, a select few cancer surgeries, and a few other miscellaneous procedures)
- Region (I did not include this in the data analysis or model)
- Metric (I only included the 50th percentile of waiting times)
- Data Year (I excluded all dates after 2019 due to COVID-19; only. 2008-2019 data included in my analysis)
- Unit of Measurement (I did not include this column)
- Indicator Result (The WAITING TIME IN DAYS - My target variable)

### Data Cleaning

### Data Analysis and Insights

### Predictive Model (Random Forest Regressor)

### Limitations of the Model


