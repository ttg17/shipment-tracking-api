import random
from enum import Enum

from pydantic import BaseModel, Field


def random_destination():
    return random.randint(11000, 11999)


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class Shipment(BaseModel):
    content: str = Field(description="Content of the shipment", max_length=100)
    weight: float = Field(ge=1, le=25, description="Weight of the shipment in kg")
    destination: int = Field(
        default_factory=random_destination,
        description="Destination of the shipment",
    )
    status: ShipmentStatus


