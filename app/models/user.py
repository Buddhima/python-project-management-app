class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)  # staff / manager
    password = Column(String)