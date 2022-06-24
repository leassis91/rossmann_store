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
* Packages : Jupyter, Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn among others (please, check full list [here](https://github.com/leassis91/rossmann_store/blob/master/requirements.txt))
* Frontend API: Telegram Bot
* Backend: Heroku

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
 
 We used many error metrics during the project. Main model metric for evaluation was the Root Mean Squared Error (RMSE). The RMSE is calculated as  
<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/67332395/175569005-2bd2789e-85bc-44d8-8378-faa3e03f019c.png" alt="RMSE">
</p>

where *y_hat* is the predicted value, *y* is the ground truth value, and *n* is the number of stores in the dataset.

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

According to our forecasting model, we achieved an efficiency improvement of 48.37% compared to previous forecasts (Average Model had 1354.8 for MAE and our new model has 699.43).
Translating into business terms, we calculate the sum of worst and best revenue scenarios, and the respective forecasts made.

| Scenario | Values |
|-----------|---------|
| Predictions | R$285,934,117.20 |
| Worst Scenario | R$285,150,484.70 |
| Best Scenario | R$286,717,749.69 |

As we can see, our **best scenario** and **worst scenario** only diverge from **predictions** by 0.27%: certainly more assertive than previous one.

<br>

## 💡 Conclusions

 - XGBoostRegressor model had the best performance when it comes to **Results/Time * Accuracy**, and thus gave us a more assertive prediction, helping our CFO on taking futures decisions about budget and repairing the stores.

<br>

## 👣 Next steps

DS team establish to start another cycle to analyze the problem, seeking different approaches, creating another hypothesis, reconsidering the ones not chosen, and reanalysing stores with behavior that were tough to do the forecast. Some approachs in mind to be made:

 - Collect more data;
 - We treat as an aggregate parameter the "sum" of all stores for the assortment hypothesis. Un the 2nd cycle, we could see how it would behave if we used the average;
 - Refine the feature engineering, like trying to find anoher good features;
 - Work with GridSearchCV, as we have more time to tune our model, since its already in production;
 and many more.

<br>

## 🚀 Deployment

Go say 'Hi!' to our bot! Check it out at:

[<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](http://t.me/rossmannleassis_bot)

 - Sign up in Telegram;
 - Submit one number at a time and wait for prediction!
 - or just look for 'rossmannleassis_bot' in Telegram's search!

![send](https://github.com/leassis91/rossmann_store/blob/master/img/gif_rossmann.gif)

<br>

## 🔗 References

1. Data Science Process Alliance - [What is CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/)
2. Owen Zhang - [Open Source Tools & Data Science Competitions](https://www.slideshare.net/odsc/owen-zhangopen-sourcetoolsanddscompetitions1)
3. Statstest  - [Cramer's V](https://www.statstest.com/cramers-v-2/)

<br>

If you have any other suggestion or question, feel free to contact me via [LinkedIn](https://linkedin.com/in/leandrodestefani).

<br>

## ✍🏽 Author

- [Leandro Destefani](https://github.com/leassis91)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandrodestefani) [![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:leassis.destefani@gmail.com) [![kaggle](https://img.shields.io/badge/Kaggle-3776AB?style=for-the-badge&logo=&logoColor=white)](https://kaggle.com/leandrodestefani)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

***

## 💪 How to contribute

1. Fork the project.
2. Create a new branch with your changes: `git checkout -b my-feature`
3. Save your changes and create a commit message telling you what you did: `git commit -m" feature: My new feature "`
4. Submit your changes: `git push origin my-feature`
