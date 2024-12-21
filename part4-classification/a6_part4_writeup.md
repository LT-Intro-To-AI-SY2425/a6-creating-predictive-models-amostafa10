# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
With the StandardScaler the accuracy is 0.89 but without it, the accuracy drops to 0.83. I think they model becomes less accurate because some points of data are being represented more than others.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model is decently accurate with the StandardScaler (0.89 accuracy). I would say that the model is accurate enough to be used in this case as most of the time it will correctly estimate the purchase decision.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
Most of the predictions are accurate to the actual results. It's hard to tell, but perhaps certain estimated salaries (like low income) make the model lean one way that may sometimes be incorrect.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
The model returned a 0, so I think not.