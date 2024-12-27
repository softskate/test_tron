from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class WalletQuery(Base):
    __tablename__ = "wallet_queries"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True, nullable=False)
    balance = Column(Float, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    queried_at = Column(DateTime, default=datetime.now)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
