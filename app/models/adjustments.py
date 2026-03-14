class Adjustment(Base):
    __tablename__ = "adjustments"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    amount = Column(Float)
    reason = Column(String)