import yfinance as yf
import pandas as pd

# Daftar saham yang akan di-screening (contoh: saham di IDX)
tickers = ["BBCA.JK", "BBRI.JK", "TLKM.JK", "ASII.JK", "UNVR.JK"]

# Fungsi untuk screening saham
def stock_screener(tickers):
    results = []
    
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Ambil data yang diperlukan
        name = info.get('longName', 'N/A')
        pe_ratio = info.get('trailingPE', 'N/A')
        dividend_yield = info.get('dividendYield', 'N/A')
        market_cap = info.get('marketCap', 'N/A')
        
        # Kriteria screening (contoh: P/E < 20, Dividend Yield > 2%, Market Cap > 10T)
        if pe_ratio != 'N/A' and dividend_yield != 'N/A' and market_cap != 'N/A':
            if pe_ratio < 20 and dividend_yield > 0.02 and market_cap > 10e12:
                results.append({
                    'Ticker': ticker,
                    'Nama Perusahaan': name,
                    'P/E Ratio': pe_ratio,
                    'Dividend Yield': dividend_yield,
                    'Market Cap': market_cap
                })
    
    # Konversi hasil ke DataFrame
    return pd.DataFrame(results)

# Jalankan screener
screened_stocks = stock_screener(tickers)

# Tampilkan hasil
if not screened_stocks.empty:
    print("Saham yang memenuhi kriteria:")
    print(screened_stocks)
else:
    print("Tidak ada saham yang memenuhi kriteria.")
