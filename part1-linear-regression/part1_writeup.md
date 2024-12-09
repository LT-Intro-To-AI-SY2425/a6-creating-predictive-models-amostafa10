# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?
The r squared value represents how closely the two variables are correlated. An r squared value closer to 1 or -1 means that the linear regression model is more likely to accurately represent the pattern present in the data.

2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?
136.52

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?

For the dataset provided, the model is fairly accurate in its predictions. However, in reality, I dont think the model would be able to reliably predict someone's blood pressure. This is because the training data we used is too small to properly account for the patterns there might be. Also, because we're simply performing linear regression, there could be patterns that can't be entirely accounted for with just a straight line. To improve the model, we could use more data and consider using a different regression method.