# Rossmann Sales Prediction

![](https://user-images.githubusercontent.com/77629603/155387474-3dd5c092-c0b5-4e58-a9ae-a5e5d06833c8.png)


# 1. Context

This project is based in a Kaggle Challenge wich simulates a business problem. Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. 

# 2. Challenge

## 2.1. Problem

The CFO wants to know the budget to renovate each store.

## 2.2. Causes

-Current prediction proccess is inaccurate 

-Current prediction proccess isn't scientific and data-driven

-Current sales prediction is done manually by the 1,115 stores

-Sales visualization was limited to the computer

## 2.3. Solution

-Using Machine Learning model to make sales prediction of every store

-Sales prediction visualization may be made by Telegram request (API)

#3. Solution Development

## 3.1. Data Description 

Checking the shape of the datase, nulls and filling the nulls values. 

## 3.2. Feature Engineering

Creating new attributes from the original data. 
(Ex: extract day, year, month from date)

## 3.3. Exploratory Data Analysis

Trying to get insights by data analysis with graphs, histograms, plotlines and barplot. Also checking the correlation of the features and testing hypotesis.

## 3.4. Data Preparation

Using normalization, rescaling and encoding to prepare the data to the Machine Learning model.

## 3.5. Feature Selection

Using the Boruta algorithm to select the most important features to get the best Machine Learning performance.

## 3.6. Machine Learning Model

Training different Machine Learning models and comparing errors. The choosen method was the XGBoost Regressor because of the speed and accuracy of the model. 

![Performances without fine tuning](https://user-images.githubusercontent.com/77629603/155387296-541ac158-9c6c-44f5-913c-40b1aa2b02a4.png)


## 3.7. Error Translation

Giving business meaning to the project, translating accuracy in values to the business.

## 3.8. Deploy and Telegram BOT

Deploy in the Heroku Cloud and configurating Flask API request by a Telegram Bot. 

Telegram bot username: @rossmann_salesp_bot

# 4. Results and Conclusion

## 4.1. Main Hypotesis 

The main hypotesis confirmed in the EDA step:

### H1. Stores with larger assortments should sell more.
False. Stores with larger assortments should sell less.

![Sales sum by assortment](https://user-images.githubusercontent.com/77629603/155387884-6c33a7be-82e5-4c57-8648-28bf0f217aae.png)


### H2. Stores with closer competitors should sell less.
False. Stores with closer competitors sell more.

![Sales by competition distance (bin = 0-1000)](https://user-images.githubusercontent.com/77629603/155381618-a59fdbc2-e4af-45dd-8458-3159ddc01eac.png)


### H3. Stores with longer active promotions should sell more.
False. We can see that sales increase in the standard promos and decreases in the extended promos.
(Negative promo duration is regular promo, positive promo duration is extanded promo)

![Regplot representing sales by promo duration](https://user-images.githubusercontent.com/77629603/155382386-6c6462ab-0820-4dae-a1ca-51ea9a0aad33.png)

## 4.2.Conclusion
The model generates a dataframe with the prediction of each store and the respectives worst and best scenarios. 
The CFO now can know the budget available to renovate the stores, with 90% accuracy.

![First 15 rows of the prediction dataset.](https://user-images.githubusercontent.com/77629603/155379600-1321b4d9-6db2-4941-80cf-96012798fe00.png)

The user can get the results by Telegram. Here is some demonstration(link)!

## 4.3. Machine Learning Performance

Here is the demonstration of the model prediction vs real sales by date

![Seaborn lineplot](https://user-images.githubusercontent.com/77629603/155380531-060fbf29-4f30-486f-b875-4d3b0ead5178.png)


# 5. Next Steps

*Collecting feedback of the users and improve the usability if necessary
*Improve the performance in the next CRISP cycle

# 6. References

The data is avaliable in this [page](https://www.kaggle.com/c/rossmann-store-sales)
