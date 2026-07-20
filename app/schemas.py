from pydantic import BaseModel, Field

from app.database.models import ShipmentStatus


class BaseShipment(BaseModel):
    content: str = Field(max_length=100)
    weight: float = Field(ge=1, le=25)
    # destination: int | None = None

class ShipmentRead(BaseShipment):
    status: ShipmentStatus

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    content: str | None = Field(max_length=100, default=None)
    weight: float | None = Field(default=None, le=25)
    # destination: int | None = Field(default=None)
    status: ShipmentStatus





