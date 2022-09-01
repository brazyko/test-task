from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, scoped_session, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///tasks.sql")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    password = Column(String(30))

    def __repr__(self):
        return "%s" % self.username


class Expenses(Base):
    __tablename__ = "expenses"
    expense_id = Column(Integer, primary_key=True)
    expense_sum = Column(Integer)
    user = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    category = Column(Integer, ForeignKey("categories.category_id", ondelete="CASCADE"))
    date = Column(String(50))

    def __repr__(self):
        return "%s " % self.expense_sum


class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    expenses = relationship("Expenses")

    def __repr__(self):
        return "%s" % self.category_name


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
