from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


URI = 'postgresql://h4cktivist:UvgB5SPt3lAR@ep-black-glitter-a26rfy11.eu-central-1.aws.neon.tech/dataset?sslmode=require'
engine = create_engine(URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
