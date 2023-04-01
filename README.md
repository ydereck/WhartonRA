# Wharton RA Tasks
## Task 1: Earnings Announcements for European Firms
The code for Task 1 can be found in `Task1.py`, and the results for Task 1 can be found in `LiYang_1.csv`.  

*Notes:*  
For the duplicates, I dropped the duplicated rows after reading in the data.  
For the observations where the announcement date is later than 04/01/2020, I marked the “trading_date” as -1, since these dates are out of the range of firm_quarters.  

## Task 2: Non-ESG News
The code for Task 2 can be found in `Task2.py`, and the results for Task 2 can be found in `LiYang_2.csv`.  

*Notes:*  
For the events in the "Allnews" dataset, I decide whether each event is non-ESG event by 'GROUP'. Specifically,  
*{labor-issues, marketing, corporate-responsibility, industrial-accidents, government, regulatory, civil-unrest, security, war-conflict, employment, exploration, health}* are treated as ESG news, while the events with any other 'GROUP' name are treated as non-ESG events.

## Task 3: Inconsistent Disclosures
The code for Task 3 can be found in `Task3.do`, and the results for Task 3 can be found in `LiYang_3.xlsx`, where 'Tab1' stores the two summary tables and 'Tab2' stores the OLS estimates.  

*Discussion:*  
My initial hypothesis was that the presence of inconsistent disclosures would have a negative correlation with fund performance. When Form ADV Part 1 and Part 2 are consistent, it may indicate that there is not much adverse news that needs to be concealed from investors, and in such a scenario, the fund is more likely to perform well.  

To test my hypothesis, I ran a regression analysis of fund performance against the indicator of inconsistency. I also incorporated fixed effects for each year, as overall fund performance varied from year to year. The results (stored in Tab2) show a slightly positive coefficient for inconsistency, which contradicts my initial assumption. However, the estimate is not statistically significant based on the t-stat or p-value. On the other hand, some of the year's indicators have statistically significant estimates.  

While the lack of regressors may have affected the accuracy of this result, it may be explained in this way: intentionally hiding bad news in Form ADV Part 2 would not deceive investors since such information must be disclosed in Part 1. This could potentially harm the fund's performance even more. In short, further studies are required before drawing any definitive conclusions regarding the relationship between inconsistent disclosures and fund performance.
