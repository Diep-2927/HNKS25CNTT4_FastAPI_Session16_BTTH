from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "mysql+pymysql://root:29012007@localhost:3306/student_magement"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine,
    expire_on_commit=False
)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()