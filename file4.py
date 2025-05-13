from yfinance import Ticker

@app.on_event("startup")
async def startup_event():
    ticker = Ticker("EURUSD=X")
    data = ticker.history(period="1d")
    
    for index, row in data.iterrows():
        with SessionLocal() as session:
            session.add(Volume(date=index.date(), volume=row['Volume']))
            session.commit()