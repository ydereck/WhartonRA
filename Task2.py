import pandas as pd

# Step 1: read in ESGnews, then drop duplicates standardize the format of date
df_ESG = pd.read_csv('ESGnews.csv', usecols=['gvkey', 'eventdate'])
df_ESG.drop_duplicates(inplace=True)
df_ESG['eventdate'] = pd.to_datetime(df_ESG['eventdate'], format='%m/%d/%y').dt.strftime('%m/%d/%Y')
#df_ESG.to_excel('df_ESG.xlsx', index=False)

# Step 2: read in GROUP and dates from all news, then drop duplicates and change format of dates
df_all = pd.read_csv('allnews.csv', usecols=['GROUP', 'article_date', 'gvkey'])
df_all.drop_duplicates(inplace=True)
df_all['article_date'] = pd.to_datetime(df_all['article_date'], format='%d%b%Y').dt.strftime('%m/%d/%Y')
#df_all.to_excel('df_all.xlsx', index=False)

# Step 3: Starting from copying all the gvkey and article_dates
df_results = pd.DataFrame({'key': df_all['gvkey'], 'dates': df_all['article_date']})

# Step 4: Filter
df_results.drop_duplicates(inplace=True)
# Only keep the firms in ESGnews
df_results = df_results[df_results['key'].isin(df_ESG['gvkey'])]
# Delete the dates when there are ESG news
df_results = df_results[~((df_results['key'].isin(df_ESG['gvkey'])) & (df_results['dates'].isin(df_ESG['eventdate'])))]
# Delete the dates when there are certain ESG-related 'GROUP' of news
df_results = df_results.loc[~((df_all['GROUP'].isin(['industrial-accidents', 'government', 'regulatory', 'civil-unrest', 'security', 'war-conflict', 'employment', 'exploration', 'health'])) & (df_results['key'].isin(df_all['gvkey'])) & (df_results['dates'].isin(df_all['article_date'])))]

# Step 5: output
df_results.to_csv('LiYang_2.csv', index=False)
