# https://nbviewer.jupyter.org/gist/FinanceData/35a1b0d5248bc9b09513e53be437ac42
import FinanceDataReader as fdr
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)


sp500 = fdr.StockListing('S&P500')
sp500.head(10)

