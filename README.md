# TataMotors_Stock_Prediction
# Predicted Tata Motors stock using Auto Time Series AutoTS - Python
Here, in this project I have used Time Series for predicting the close price of Tata Motors.

# Loading Dataset
In this model, I have used TTM.csv which I found on Yahoo Finance. It was quite handy and the installation was at ease!

# Modules and Packages
I have used pandas to load in the dataset, plotly and matplotlib to visualize the output. I used plotly for Candlestick graph and matplotlib for the line graph.
And the main module AutoTS for training our model

# Predicting
This model will predict the closing price for the next 10 days after the latest date in the dataset.
This is what the `forecast_length=10` does.
And for `model.fit`, the first parameter will the `data` we are training. As AutoTS is a Time Series library `data_col` will be the data column of our dataset, which will be `Date`. This might vary from dataset to dataset. And finally the `value_col` will be the value which we like to predict from our model, which is none other than `Close`. And with those parameters being provided we will be rendering our prediction.

# Output
After a long console output finally you will be seeing the desired output of your code. As this is a Time Series model what it does is that it creates an average output based on the past performances. So, please don't expect it to be precise>
The Output log looks like this:
![Screenshot 2022-12-04 162808](https://user-images.githubusercontent.com/116950535/205487408-04c0f09b-a54c-43dd-9948-3b8b89a9753e.png)

