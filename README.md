# Wharton RA Tasks
## Task 1: Earnings Announcements for European Firms
The code for Task 1 can be found in `Task1.py`, and the results for Task 1 can be found in `LiYang_1.csv`.  
*Notes:*  
For the duplicates, I dropped the duplicated rows after read in the data.  
For the observations where the announcement date is later than 04/01/2020, I marked the “trading_date” as -1, since these dates are out of the range of firm_quarters.  

## Task 2: Non-ESG News
The code for Task 2 can be found in 'Task2.py', and the results for Task 2 can be found in 'LiYang_2.csv'.  
*Notes:*  
For the events in the "Allnews" dataset, I decide whether each event is non-ESG event by 'GROUP'. Specifically,  
*{labor-issues, marketing, corporate-responsibility, industrial-accidents, government, regulatory, civil-unrest, security, war-conflict, employment, exploration, health}* are treated as ESG news, while the events with any other 'GROUP' name are treated as non-ESG events.

## Task 3: Inconsistent Disclosures
The code for Task 3 can be found in 
