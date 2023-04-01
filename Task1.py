import pandas as pd
import datetime

# Read and clean Europefirmquarters.csv
df_fq = pd.read_csv('Europefirmquarters.csv')
df_fq = df_fq.drop_duplicates()
df_fq['fqenddt'] = pd.to_datetime(df_fq['fqenddt'], format='%d-%b-%y')
df_fq['FQPENDS'] = (df_fq['fqenddt'] - pd.DateOffset(months=3)).dt.strftime('%b-%Y')
df_fq['CUSIP2'] = df_fq['sedol'].str[-6:]
df_fq.to_csv("df_fq.csv", index=False)

# Read and clean EuropeEAs.csv
df_ea = pd.read_csv('EuropeEAs.csv')
df_ea = df_ea.drop_duplicates()
df_ea['PENDS'] = pd.to_datetime(df_ea['PENDS'], format='%d-%b-%y')
df_ea['PENDS2'] = df_ea['PENDS'].dt.strftime('%b-%Y')
df_ea['ANNDATS'] = pd.to_datetime(df_ea['ANNDATS'], format='%d-%b-%y')
df_ea['CUSIP2'] = df_ea['CUSIP'].str[-6:]
df_ea.to_csv("df_ea.csv", index=False)

# Merge the two datasets on sedol=CUSIP2 and FQPENDS=PENDS
merged_df = pd.merge(df_fq, df_ea, how='inner', left_on=['sedol', 'FQPENDS'], right_on=['CUSIP2', 'PENDS2'])
merged_df.to_csv("merged_df.csv", index=False)
# Read in the file
df3 = pd.read_csv("tradingdates.csv", header=None)

# Convert the trading dates to datetime format
df3[0] = pd.to_datetime(df3[0], format="%m/%d/%y")

# Create a list of trading dates
trading_dates = list(df3[0])

# Convert ANNDATS and ANNTIMS to datetime format
merged_df["ANNDATS"] = pd.to_datetime(merged_df["ANNDATS"], format="%d-%b-%y")
merged_df["ANNTIMS"] = pd.to_datetime(merged_df["ANNTIMS"], format="%H:%M:%S").dt.time

# Initialize a list to store the result
result = []

# Loop over every row
for index, row in merged_df.iterrows():
    # Generate trade_day variable
    trade_day = row['ANNDATS'].date()
    
    # Check if ANNTIMS is later than 16:30:00 or trade_day is not a trading date
    if row['ANNTIMS'] > datetime.time(16, 30, 0) or pd.Timestamp(trade_day) not in trading_dates:
        while True:
            trade_day += datetime.timedelta(days=1)
            if pd.Timestamp(trade_day) in trading_dates:
                break
            if row['ANNDATS'].date() > datetime.date(2020,4,1):
                trade_day = -1
                break
        
        # Add the result to the list
        result.append((row['sedol'], row['fqenddt'], row['ANNDATS'], row['ANNTIMS'], trade_day))
    
    else:
        result.append((row['sedol'], row['fqenddt'], row['ANNDATS'], row['ANNTIMS'], trade_day))

# Convert the result list to a DataFrame, then Export to csv
result_df = pd.DataFrame(result, columns=['firm_ID', 'quarter', 'ann_date', 'ann_time', 'trading_date'])
result_df[["firm_ID","quarter","trading_date"]].to_csv("LiYang_1.csv", index=False)
