# Rossmann Sales Prediction

![](https://user-images.githubusercontent.com/77629603/155387474-3dd5c092-c0b5-4e58-a9ae-a5e5d06833c8.png)


# 1. Context

This project is based in a Kaggle Challenge wich simulates a business problem. Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. 

# 2. Challenge

## 2.1. Problem

The CFO wants to renovate the stores, but he wants to be sure how much he can spend based on the future sales.

## 2.2. Causes

* Current prediction proccess is inaccurate 

* Current prediction proccess isn't scientific and data-driven

* Current sales prediction is done manually by the 1,115 stores

* Sales visualization was limited to the computer

## 2.3. Business Assumptions
* The data contains historical data of 1115 stores;
* The data available are between 2013-01-01 and 2015-07-31;
* Null values of competition distance was replaced to 200.000 meters, assuming that there are no competitors
<details>
<summary>Features definition</summary>
  
| Feature                | Definition                                                                                               |
|------------------------|----------------------------------------------------------------------------------------------------------|
| id                     | unique id that represent store and date of sale                                                          |
| store                  | a unique Id for each store                                                                               |
| sales                  | the turnover for any given day (target variable)                                                         |
| customers              | the number of customers on a given day                                                                   |
| open                   | an indicator for whether the store was open (0/1)                                                        |
| state holiday          | indicates a state holiday (a = public holiday, b = Easter holiday, c = Christmas, 0 = None)              |
| school holiday         | indicates if the (Store, Date) was affected by the closure of public schools                             |
| store type             | differentiates between 4 different store models. (a, b, c, d)                                            |
| assortment             | describes an assortment level (a = basic, b = extra, c = extended)                                       |
| competition distance   | distance in meters to the nearest competitor store                                                       |
| competition open since | gives the approximate year and month of the time the nearest competitor was opened                       |
| promo                  | indicates whether a store is running a promo on that day                                                 |
| promo 2                | Promo2 is a continuing and consecutive promotion for some stores (0/1)                                   |
| promo 2 since          | describes the year and calendar week when the store started participating in Promo2                      |
| promo interval         | describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew.  |
  
 </details>
 
 

## 2.4. Solution

* Using Machine Learning model to make sales prediction of every store

* Sales prediction visualization may be made by Telegram request (API)

# 3. Solution Development

## 3.1. Data Description 

Checking the shape of the datase, nulls and filling the nulls values. 

## 3.2. Feature Engineering

Creating new attributes from the original data. 

<details>
<summary>Features created</summary>

| Feature           | Definition                                         |
|-------------------|----------------------------------------------------|
| year              | year extracted from date                           |
| month             | month extracted from date                          |
| day               | day extracted from date                            |
| week of year      | week of year extracted from date                   |
| year week         | year week extracted from date (Y-W)                |
| promo since       | date since promotion started (Y-W)                 |
| competition since | date since competition started (year, month, year) |

</details>



## 3.3. Exploratory Data Analysis

Trying to get insights by data analysis with graphs, histograms, plotlines and barplot. Also checking the correlation of the features and testing hypotesis.

## 3.4. Data Preparation

Using normalization, rescaling and encoding to prepare the data to the Machine Learning model. Sine and cossine transformations were used in cyclical features as month, day and week of year.

## 3.5. Feature Selection

Using the Boruta algorithm to select the most important features to get the best Machine Learning performance.

## 3.6. Machine Learning Model

Training different Machine Learning models and comparing errors. The choosen method was the XGBoost Regressor because of the speed and accuracy of the model.

![Performances without fine tuning](https://user-images.githubusercontent.com/77629603/155387296-541ac158-9c6c-44f5-913c-40b1aa2b02a4.png)

## 3.7. Error Translation

Giving business meaning to the project, translating accuracy in values to the business.

## 3.8. Deploy and Telegram BOT

Deploy in the Heroku Cloud and configurating Flask API request by a Telegram Bot. 
The user types /store_id and gets the sales prediction of this store for the next six weeks.


<img src="https://user-images.githubusercontent.com/77629603/162584257-c7783ef3-d434-4910-9878-c2bfb4057228.png" alt="" style="width:300px;"/>


# 4. Results and Conclusion

## 4.1. Main Hypotesis 

The main hypotesis confirmed in the EDA step:

### H1. Stores with larger assortments should sell more.
**False** <br />Stores with larger assortments should sell less.

![Sales sum by assortment](https://user-images.githubusercontent.com/77629603/155387884-6c33a7be-82e5-4c57-8648-28bf0f217aae.png)


### H2. Stores with closer competitors should sell less.
**False**  <br />Stores with closer competitors sell more.

![Sales by competition distance (bin = 0-1000)](https://user-images.githubusercontent.com/77629603/155381618-a59fdbc2-e4af-45dd-8458-3159ddc01eac.png)


### H3. Stores with longer active promotions should sell more.
**False** <br />We can see that sales increase in the standard promos and decreases in the extended promos.
(Negative promo duration is regular promo, positive promo duration is extanded promo)

![Regplot representing sales by promo duration](https://user-images.githubusercontent.com/77629603/155382386-6c6462ab-0820-4dae-a1ca-51ea9a0aad33.png)

## 4.2.Conclusion
The model generates a dataframe with the prediction of each store and the respectives worst and best scenarios. 
The CFO now can know the budget available to renovate the stores, with 90% accuracy.

![First 15 rows of the prediction dataset.](https://user-images.githubusercontent.com/77629603/155379600-1321b4d9-6db2-4941-80cf-96012798fe00.png)

The user can get the results by Telegram. Here is some [demonstration](https://www.linkedin.com/posts/heitor-felix_datascience-datadriven-business-activity-6902361790051606528-2Fjo)!

## 4.3. Machine Learning Performance

**Final model performance**
![image](https://user-images.githubusercontent.com/77629603/162584149-291cea37-819d-4f18-bd67-0aac45349557.png)

Here is the demonstration of the model prediction vs real sales by date

![Seaborn lineplot](https://user-images.githubusercontent.com/77629603/155380531-060fbf29-4f30-486f-b875-4d3b0ead5178.png)


# 5. Next Steps

* Collecting feedback of the users and improve the usability if necessary
* Improve the performance in the next CRISP cycle

# 6. References
* [Kaggle](https://www.kaggle.com/c/rossmann-store-sales)
* [Comunidade DS](https://www.comunidadedatascience.com/)
