class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))

    amount = Column(Float)
    status = Column(String)

    created_by = Column(Integer)
    approved_by = Column(Integer, nullable=True)

    created_at = Column(DateTime)