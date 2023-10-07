from datetime import datetime, timezone

from sqlalchemy import MetaData, Column, Integer, func
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

Base = declarative_base(metadata=metadata)


def utc_now():
    return datetime.now(tz=timezone.utc)


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(postgresql.TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        postgresql.TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
