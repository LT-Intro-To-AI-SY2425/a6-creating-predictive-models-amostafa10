# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
0.85
This means that the model has a relatively high correlation with the data.

2. Is your model accurate? Why or why not?
The model seems somewhat accurate. Considering this data set is less prone to unknown factors magically altering the results so the linear model can more accurately represent the pattern.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
9122.78839501 and 1095.20497434 respectively.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
Because the linear model is predicting a negative correlation in the variables, its not like its placing a floor on the predictions so if the variables keep getting higher then the prediction will keep going down until it's negative.