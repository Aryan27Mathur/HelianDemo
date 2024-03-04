import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("C:/Users/am943/Downloads/etfs_details_type_fund_flow.csv", header=0)

    esg_data = df[["Symbol", "ETF Name", "ESG Score"]]
    esg_data_sorted = esg_data.sort_values(by="ESG Score", ascending=False)
    print(esg_data_sorted.head())