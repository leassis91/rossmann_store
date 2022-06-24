# <p align="center">🏪💊 ROSSMANN STORE SALES PREDICTION 💊🏪</p> 
<p align="center"><img src="https://github.com/leassis91/rossmann_store/blob/master/img/rossmann-store.jpg?raw=true"></p>
<br>

## 📖 Background

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied.

<br>


## 📌 Problem Statement

*Forecasting the sales' income of the next 6 weeks.*

Since the recent results's accuracy are quite noisy, our work here is to give an **assertive prediction** of the sales of each store, up to 6 weeks in advance. This task has been assined to the whole team of Data Scientists, who are given a historical database in order to generate the desired forecasting. To catch up all details of the request, the team had a business meeting with company's CFO, who explained the need to establish a budget to carry out a general repair in each store.

<br>

## 💾 Data Understanding

 ### - Code Used:

* Python Version : 3.8
* Packages : Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn among others (please, check full list [here](https://github.com/leassis91/rossmann_store/blob/master/requirements.txt))

<br>

 ### - Importing Dataset:

* Kaggle: https://www.kaggle.com/competitions/rossmann-store-sales/data

<br>

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

<br>

 ### - Business Assumptions

  * Stores with sales equal 0 were discarded.
  * Days when stores were closed were discarded.
  * Stores missing information about "Competition Distance" will be set a value of '200000' distance.
  * Analysis will be made one week after last date record.
 
 <br>
 
## 🧾 Evaluation Metric
 
 We used many error metrics during the project. Main model metric for evaluation was the Root Mean Square Percentage Error (RMSPE). The RMSPE is calculated as  
<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/67332395/175408080-447ca43e-48db-429a-a0ef-9336ec87fce9.png" alt="RMSPE">
</p>

where y_i denotes the sales of a single store on a single day and yhat_i denotes the corresponding prediction. Any day and store with 0 sales is ignored in scoring.

<br>

## 🔬 Solution Approach

The approach used to solve this task was done by applying CRISP-DM¹ methodology, which was divided in the following parts:

1. **Data Description:** understanding of the status of the database and dealing with missing values properly. Basic statistics metrics furnish an overview of the data.  
2. **Feature Engineering:** derivation of new attributes based on the original variables aiming to better describe the phenomenon that will be modeled, and to supply interesting attributes for the Exploratory Data Analysis.
3. **Feature Filtering:** filtering of records and selection of attributes that do not contain information for modeling or that do not match the scope of the business problem.
4. **Exploratory Data Analysis (EDA):** exploration of the data searching for insights and seeking to understand the impact of each variable on the upcoming machine learning modeling.
5. **Data Preparation:** preprocessing stage required prior to the machine learning modeling step.
6. **Feature Selection:** selection of the most significant attributes for training the model.
7. **Machine Learning Modeling:** implementation of a few algorithms appropriate to the task at hand. In this case, models befitting the *regression* assignment - *i.e.*, forecasting a continuous value, namely sales.
8. **Hyperparameter Fine Tuning:** search for the best values for each of the parameters of the best performing model(s) selected from the previous step.
9. **Statistical Error Analysis:** conversion of the performance metrics of the Machine Learning model to a more tangible business result.
10. **Production Deployment:** deployment of the model in a cloud environment (Heroku), using Flask connected to our model in a pickle file.
11. **Telegram Bot:** deployment of Telegram Bot API, here used as our user receiver. Check out at "Deployment" section.

<br>

## 🕵🏽‍♂️Exploratory Data Analysis & Main Insights

### - Numerical Attributes Correlation

![image](https://user-images.githubusercontent.com/67332395/175460617-43a48c17-d3e0-4d05-9c86-b7d7be891572.png)

### - Categorical Attributes Correlation

![image](https://user-images.githubusercontent.com/67332395/175460670-83e08358-dd8f-432a-ad87-51037abe5fad.png)

### - Main Hypothesis Chosen

Here, the criterion used to choose the main hypotheses was in the sense of how shocking and impacting the result would be for the business team's beliefs.

- **Hypothesis 1 (H2 in notebook):** Stores with closer competitors should sell less. 
   ***False:*** Data showed us that, actually, they sell MORE.
   
   Business team's belief revealed us their thoughts on lower sales while drugstores are closer to the competitors. This hypothesis proves the opposite The correlation analysis of "competition distance" and "sales" shows a small correlation, indicating that sales do not increase when competitors are closer.
   
   ![image](https://user-images.githubusercontent.com/67332395/175464452-7d3ae44c-9e38-435a-9029-e5c95f4c55ba.png)


- **Hypothesis 2 (H4 in notebook):** Stores with longer active offers should sell more.
   ***False:*** Data showed us that, stores that kept products on sale for a long time performed worse than before.
   
   Again, we shocked business team's belief and common sense that. Here are the visualizations.
   
   ![image](https://user-images.githubusercontent.com/67332395/175464762-d1ba1d94-3e8f-4372-a435-f8e5c4603740.png) 
   
   
- **Hypothesis 3:** Stores should sell more after the 10th day of each month.  
   ***True:*** the average performance is better after 10 days of the month.
   
   ![image](https://user-images.githubusercontent.com/67332395/175465319-f058885e-1deb-45f2-b401-d6515bb71727.png)

<br>

## 💻 Machine Learning Modeling & Evaluation

 * Cross Validation
 
  *Performance on 5 K-Fold CV.*

| Model Name | MAE CV   | MAPE CV      | RMSE CV |
|-----------|---------|-----------|---------|
|  Random Forest Regressor  | 837.68 +/- 218.74| 0.12 +/- 0.02  | 1256.08 +/- 320.36 |
|  XGBoost Regressor	  | 1039.91 +/- 167.19 | 0.14 +/- 0.02   | 1478.26 +/- 258.52 |
|  Linear Regression	  | 2081.73 +/- 295.63 | 0.3 +/- 0.02   | 2952.52 +/- 468.37 |
|  Linear Regression - Lasso	  | 2116.38 +/- 341.50 | 0.29 +/- 0.01	   | 3057.75 +/- 504.26 |


Although the Random Forest model has proven to be superior to the others, in some cases this model ends up requiring a lot of space to be published, resulting in an extra cost for the company to keep it running. Therefore, the chosen algorithm was the **XGBoost Regressor** which in sequence passed to the Hyperparameter Fine Tunning step.

<br>

 * Final Model (after Hyperparameter Fine-Tuning)

| Model Name | Mean Absolute Error | Mean Absolute Percentage Error | Root Mean Squared Error |
| ---- | :----: | :----: | :----: |
| XGBoost Regressor | 699.43 | 0.1037 | 1005.6039 |

<br>

## Business Performance

It is now possible to analyze the metrics and compare the difference in performance between the current model used by the company (**Average Model**) and the model proposed by the data scientist (**XGBoost Regressor**)

*under construction*

<br>

## 💡 Conclusions

 - The XGBoost Model for the first cycle (CRISP-DM Methodology) presented a result within the acceptable range, although some stores were difficult to have the expected behavior presenting the MAPE (Mean Absolute Percentage Error) between 0.30 to 0.56, this first result it will be presented to the company, to inform the project status and what is already available as a solution.

*under construction*

<br>

## 👣 Next steps

DS team establish to start another cycle to analyze the problem, seeking different approaches, especially considering stores with behavior that is difficult to predict. In these stores the Data scientist ought gain plenty of experience.

*under construction*

<!-- Possible points to be addressed in the second cycle:

-**Work with NA data differently**

-**Rescaling and Encoding of data with different methodologies**

-**Work with new features for forecasting**

-**Work with a more robust method to find the best Hyper parameters for the model** -->

<br>

## 🚀 Deployment

Go say 'Hi!' to our bot! Check it out at:

[<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](http://t.me/rossmannleassis_bot)

<br>

## 🔗 References

1. Data Science Process Alliance - [What is CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/)
2. Owen Zhang - [Open Source Tools & Data Science Competitions](https://www.slideshare.net/odsc/owen-zhangopen-sourcetoolsanddscompetitions1)
3. Statstest  - [Cramer's V](https://www.statstest.com/cramers-v-2/)

<br>

If you have any other suggestion or question, feel free to contact me via [LinkedIn](https://linkedin.com/in/leandrodestefani).

***

## 💪 How to contribute

1. Fork the project.
2. Create a new branch with your changes: `git checkout -b my-feature`
3. Save your changes and create a commit message telling you what you did: `git commit -m" feature: My new feature "`
4. Submit your changes: `git push origin my-feature`
