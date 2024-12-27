from fastapi import FastAPI, HTTPException, Query
from tronpy import Tron
from tronpy.providers import HTTPProvider
from database import WalletQuery, SessionLocal
from schemas import WalletRequest, WalletResponse
from config import API_KEY


app = FastAPI()
tron = Tron(provider=HTTPProvider(api_key=API_KEY))

@app.post("/wallet/", response_model=WalletResponse)
def get_wallet_info(wallet: WalletRequest):
    try:
        account_info = tron.get_account(wallet.address)
        balance = account_info.get("balance", 0) / 1_000_000
        bandwidth = tron.get_account_resource(wallet.address).get("freeNetUsed", 0)
        energy = tron.get_account_resource(wallet.address).get("EnergyUsed", 0)

        db = SessionLocal()
        db_query = WalletQuery(
            address=wallet.address,
            balance=balance,
            bandwidth=bandwidth,
            energy=energy
        )
        db.add(db_query)
        db.commit()
        db.refresh(db_query)
        db.close()

        return WalletResponse(
            address=wallet.address,
            balance=balance,
            bandwidth=bandwidth,
            energy=energy,
            queried_at=db_query.queried_at
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/wallet/queries/", response_model=list[WalletResponse])
def get_wallet_queries(skip: int = 0, limit: int = Query(10, le=100)):
    db = SessionLocal()
    queries = db.query(WalletQuery).order_by(WalletQuery.queried_at.desc()).offset(skip).limit(limit).all()
    db.close()
    return [
        WalletResponse(
            address=query.address,
            balance=query.balance,
            bandwidth=query.bandwidth,
            energy=query.energy,
            queried_at=query.queried_at
        ) for query in queries
    ]
