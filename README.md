# Email Classifier using Logistic Regression
This model classifies my emails into 5 categories: 
- Important
- General knowledge
- Account
- Career
- Ad

The model was trained using some of my own emails (650 emails, sample in emails.csv) obtained by the `email_scrapper` script through the gmail API. 

Different classification algorithms were evaluated, such as `K-Nearest Neighbors` and `Naive Bayes`, but `logistic regression` performed best.

## Enhancements
The model's accuracy is slightly above 70% which is not that bad, but it's not that great either. The following is to be done to overcome the limitations of the model, and to improve the project as a whole:
    
- Use more training data
- Include more email attributes (features) to train the model (not merely the email sender and the subject)
- The original idea of the project is a browser extension to classify emails:
    - Emails classified into categories using a web driver (e.g., Selenium web driver)
    - User specifies their own email categories and determines the time range of the emails to be classified (if not all emails)
    - Model trained using each user's emails 