class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    client_id = Column(Integer, ForeignKey("clients.id"))