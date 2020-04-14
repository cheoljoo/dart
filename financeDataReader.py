import FinanceDataReader as fdr
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)


sp500 = fdr.StockListing('S&P500')
sp500.head(10)
