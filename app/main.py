from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from app.schemas import Shipment, ShipmentStatus

app = FastAPI()



shipments = {
    12701: {"weight": 0.5, "content": "wooden table", "status": "in transit"},
    12702: {"weight": 1.2, "content": "laptop", "status": "delivered"},
    12703: {"weight": 2.8, "content": "bookshelf", "status": "in transit"},
    12704: {"weight": 0.3, "content": "phone", "status": "pending"},
    12705: {"weight": 5.5, "content": "furniture set", "status": "in transit"},
    12706: {"weight": 1.8, "content": "monitor", "status": "delivered"},
}


@app.get("/shipment", response_model=Shipment)
def get_shipment(id: int | None = None):
    if not id:
        maxId = max(shipments.keys())
        return shipments[maxId]
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id doesn't exist!"
        )

    return shipments[id]


@app.post("/shipment")
def submit_shipment(shipment: Shipment) -> dict:
    if shipment.weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Maximum weight is 25 kg"
        )
    new_id = max(shipments.keys())
    shipments[new_id] = {"content": shipment.content, "weight": shipment.weight, "status": "placed"}

    return {"id": new_id}


# @app.put("/shipment")
# def shipment_update(
#     id: int, content: str, weight: float, status: str
# ) -> dict[str, Any]:
#     shipments[id] = {
#         "content": content,
#         "weight": weight,
#         "status": status,
#     }
#     return shipments[id]


@app.patch("/shipment")
def patch_shipment(
    id: int,
    body: dict[str, Any]
):
    shipment = shipments[id]
    
    shipment.update(body)
    shipments[id] = shipment

    return shipment


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, Any]:
    shipments.pop(id)
    return {"detail": f"Shipment with id #{id} is deleted!"}

# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")
