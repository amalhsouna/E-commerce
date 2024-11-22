import uuid

from sqlalchemy import (
    DECIMAL,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core import database as db


class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    is_active = Column(Boolean, default=False, server_default=text("false"))
    parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)

    # Relation pour la hiérarchie des catégories
    parent = relationship("Category", remote_side=[id], backref="subcategories")

    def __repr__(self):
        return f"<Category(name={self.name})>"


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    pid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String(200), unique=True, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    is_digital = Column(Boolean, default=False, server_default=text("false"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=False, server_default=text("false"))
    stock_status = Column(
        String(100), default="OUT_OF_STOCK", server_default=text("'OUT_OF_STOCK'")
    )
    category_id = Column(Integer, ForeignKey("category.id"))
    seasonal_event_id = Column(Integer, ForeignKey("seasonal_event.id"))

    # Relations
    category = relationship("Category", backref="products")
    seasonal_event = relationship("SeasonalEvent", backref="products")

    def __repr__(self):
        return f"<Product(name={self.name}, stock_status={self.stock_status})>"


class SeasonalEvent(db.Model):
    __tablename__ = "seasonal_event"

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    name = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<SeasonalEvent(name={self.name})>"


class ProductImage(db.Model):
    __tablename__ = "product_image"

    id = Column(Integer, primary_key=True)
    alternative_text = Column(String(200), nullable=True)
    url = Column(String, nullable=False)
    order = Column(Integer, default=0)
    product_line_id = Column(Integer, ForeignKey("product_line.id"))

    # Relation
    product_line = relationship("ProductLine", backref="images")

    def __repr__(self):
        return f"<ProductImage(id={self.id}, url={self.url})>"


class ProductLine(db.Model):
    __tablename__ = "product_line"

    id = Column(Integer, primary_key=True)
    price = Column(DECIMAL(10, 2), nullable=False)  # Taille ajustée
    sku = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    stock_qty = Column(Integer, default=0, server_default=text("0"))
    is_active = Column(Boolean, default=False, server_default=text("false"))
    order = Column(Integer, default=0)
    weight = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    product_id = Column(Integer, ForeignKey("product.id"))

    # Relation
    product = relationship("Product", backref="product_lines")

    def __repr__(self):
        return f"<ProductLine(id={self.id}, price={self.price}, stock_qty={self.stock_qty})>"
