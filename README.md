# AlexDS
This repository will give examples of DS work. Specifically, we will predict the stock price of Apple using regression.

1. Use Python to predict Apple stock price from live data feed.
  - Apple's closing price is being tracked from Jan 1, 2010, through the most recent trading day's closing price to use for predictions. Updated daily!
  - Work was done in Pred2.ipynb, continue testing in this. If needed, can later convert jupyter notebook to .py file
  - Currently have my functions in Pred2.py
  - Using Pred2Server.py to wrap my Pred2.py functions with Flask
  - running Pred2Server.py in my terminal and pasting URL into browser
2. Using EC2, serve the model in a flask app.
  - for basic flask, navigate to this repo folder in terminal, then enter "python MyServer2.py", then copy and paste link into browser
  - Next: learn how to push my output through flask when it is run
3. Chron job to automate input, preprocessing, and prediction.
  - Airflow suggested, but that may be too strong for constant inputs and $
  - Aws Lambda and Aws Batch sound like possibilities
  - AWS Lambda is serverless, likely cheapest for infrequent and low memory runs
    - Lambda fxn is established first
    - Python script is uploaded to S3, then uploaded to Lambda
      - Believe this actually needs to be done before configuring fxn
    - Establish a trigger for Lambda fxn (such as Cloudwatch event based on daily timing)
    - test function to run as expected
    - "deploy" by publishing a new version of the fxn
    
    - Cloudwatch event set up successfully
    - Lambda seems quickest and least expensive, except Python packages need to be loaded in
    
      - trouble with the following way 
      - Follow aws guidance to upload code and dependencies: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
      - Create new directory
      - Navigate into it
      - Copy .py script into here
      - Install libraries into "package" directory within new directory
      - Zip "package" directory
      - Upload into lambda together and they should run
      
  - try this method again
    - Download libraries from Python package index
      pypi.org/project/pandas/#files
      pypi.org/project/pytz/#files
      pypi/org/project/numpy/#files
    - Create custom package
    - Create Lambda layer
