Creating a full pipeline from scratch
1. Scrape / pull data using API
2. Store it locally in a DB
3. Exctract data and analyze basic stats
4. Make some plots
5. Make some maps

These are actually going to be plotted using HTML and JS with the Google Charts library
- calc and organize all data in Python, then plot it using Google Charts and call using HTML
    - this should allow it to be well organized in full website

6. Train random forest or log reg other model
7. K-means cross validation to check results
(FastAPI mixed in there?)
8. Display results using R Shiny -- SKIP
9. Use R shiny to change inputs so users can view plots and maps differently -- SKIP

- let's do basic historical weather into DB 
- gather basic weather data from DB
- plot in line plot using Google charts and display using HTML on my site


Two main products within one webapp:
- pretty rmd / qmd output, posted as HTML within a page
- Google plots using React, which allow for user input 
    - would love some predictions on this
    - even just logistic regression for probability of school closure, using different snowfall percents
        - sortable by state 