# <p align="center">🏪💊 ROSSMANN STORE SALES PREDICTION 💊🏪</p> 
<p align="center"><img src="https://github.com/leassis91/rossmann_store/blob/master/img/rossmann-store.jpg?raw=true"></p>
<br>

## 📖 Background

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied.

<br>


## 📌 Problem Statement

*Forecasting the sales' income of the next 6 weeks.*

Since the recent results's accuracy are quite noisy, our work here is to give an assertive prediction of the sales of each store, up to 6 weeks in advance. This task has been assined to the whole team of Data Scientists, who are given a historical database in order to generate the desired forecasting. To catch up all details of the request, the team had a business meeting with company's CFO, who explained the need to establish a budget to carry out a general repair in each store.

<br>

## 💾 Data Understanding

### - Code Used:

* Python Version : 3.8
* Packages : Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn among others (please, check full list [here](https://github.com/leassis91/rossmann_store/blob/master/requirements.txt))

### - Importing Dataset:

* Kaggle: https://www.kaggle.com/competitions/rossmann-store-sales/data

### - Data Dictionary

| Variable                       | Descriptions                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| Id                               | An id that represents a (store, date) duple within the test set|
| Store                            | A unique id for each store                                   |
| Sales                            | The turnover for any given day                          |
| Customers                        | The number of customers on a given day                       |
| Open                             | An indicator for whether the store was open: 0 = closed, 1 = open |
| Stateholiday                     | Indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. A = public holiday, b = easter holiday, c = christmas, 0 = none |
| Schoolholiday                    | Indicates if the (store, date) was affected by the closure of public schools |
| Storetype                        | Differentiates between 4 different store models: a, b, c, d  |
| Assortment                       | Describes an assortment level: a = basic, b = extra, c = extended |
| Competitiondistance              |Distance in meters to the nearest competitor store           |
| Competitionopensince[month/year] | Gives the approximate year and month of the time the nearest competitor was opened |
| Promo                            | Indicates whether a store is running a promo on that day        |
| Promo2                           | Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating |
| Promo2since[year/week]           | Describes the year and calendar week when the store started participating in promo2 |
| Promointerval                    | Describes the consecutive intervals promo2 is started, naming the months the promotion is started anew. E.G. "Feb,may,aug,nov" means each round starts in february, may, august, november of any given year for that store |
 
<!--  ### - Data Exploration
 
   1. The train data is contains large number of categorical features that should be treated. For the 1º cicle run, we tried Ordinal Encoding, then proceed with LabelEncoding, and OneHotEncoding.
   2. The numeric columns are not normally distributed, which need to be standardized. 
   3. The target variable is kind of imbalanced (14% for 1-class), it might have to be treated.
   4. The outliers of the numeric column should be treated. -->

### - Business Assumptions

  * Stores with sales equal 0 were discarded.
  * Days when stores were closed were discarded.
  * Stores missing information about "Competition Distance" will be set a value of '200000' distance.
  * Analysis will be made one week after last date record.
 
 <br>
 
## 🧾 Evaluation Metric
 
 The model evaluation metric for this competition was the "Mean F1-Score". The F1-Score can be interpreted as a harmonic average of "precision" and "recall".

 The F1 metric weights recall and accuracy equally, and a good ranking algorithm will maximize accuracy and recall simultaneously.

<br>



<br>

## 🔬 Solution Approach

The approach was divided in the following parts:

1. **Data Description:** understanding of the status of the database and dealing with missing values properly. Basic statistics metrics furnish an overview of the data.  
2. **Feature Engineering:** derivation of new attributes based on the original variables aiming to better describe the phenomenon that will be modeled, and to supply interesting attributes for the Exploratory Data Analysis.
3. **Data Filtering:** filtering of records and selection of attributes that do not contain information for modeling or that do not match the scope of the business problem.
4. **Exploratory Data Analysis (EDA):** exploration of the data searching for insights and seeking to understand the impact of each variable on the upcoming machine learning modeling.
5. **Data Preparation:** preprocessing stage required prior to the machine learning modeling step.
6. **Feature Selection:** selection of the most significant attributes for training the model.
7. **Machine Learning Modeling:** implementation of a few algorithms appropriate to the task at hand. In this case, models befitting the *regression* assignment - *i.e.*, forecasting a continuous value, namely sales.
8. **Hyperparameter Fine Tuning:** search for the best values for each of the parameters of the best performing model(s) selected from the previous step.
9. **Translation and Interpretation of the Model Performance:** conversion of the performance metrics of the Machine Learning model to a more tangible business result.
10. **Deployment of Model to Production:** publication of the model in a cloud environment so that the interested people can access its results to improve business decisions.


## 🚀 Deployment

Try yourself - [Telegram Bot SalesPredictor](http://t.me/rossmannleassis_bot)


## 🔗 References

- Owen Zhang - [Open Source Tools & Data Science Competitions](https://www.slideshare.net/odsc/owen-zhangopen-sourcetoolsanddscompetitions1)
- Statstest - [Cramer's V](https://www.statstest.com/cramers-v-2/)

<br>

If you have any other suggestion or question, feel free to contact me via [LinkedIn](https://linkedin.com/in/leandrodestefani).


***

## 💪 How to contribute

1. Fork the project.
2. Create a new branch with your changes: `git checkout -b my-feature`
3. Save your changes and create a commit message telling you what you did: `git commit -m" feature: My new feature "`
4. Submit your changes: `git push origin my-feature`
