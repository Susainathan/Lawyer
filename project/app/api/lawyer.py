from fastapi import APIRouter, status, HTTPException
from starlette import responses
from app.models.pydantic import Add_Firm, Update_Firm, UpdateHierarchy
from . import crud

router = APIRouter(tags=["Lawyer API"])


@router.post("/law", status_code=status.HTTP_201_CREATED)
async def Add_Law_Firm(payload: Add_Firm):
    await crud.add_law(payload)
    response = {
        "Law_Firm_Name": payload.Law_Firm_Name,
        "Law_Firm_Email_Address": payload.Law_Firm_Email_Address,
        "Loan_Range": payload.Load_Range,
        "Legal_Fee": payload.Legal_Fee,
        "Law_Firm_Priority": payload.Law_Firm_Priority,
        "Remarks": payload.Remarks,
        "Law_Firm_Status": payload.Law_Firm_Status,
        "Display_Hierarchy":payload.Display_Hierarchy
    }
    return response


@router.get("/law")
async def get_all():
    return await crud.get_all_firms()


@router.patch("/law/{id}/")
async def Update_Firm_Hierarchy(id: int, payload: UpdateHierarchy):
    firms = await crud.update_key(id, payload)
    if not firms:
        raise HTTPException(status_code=404, detail="Not found")

    response = {
        "Display_Hierarchy":payload.Display_Hierarchy
    }
    return response


@router.put("/law/{id}/")
async def Update_law(id: int, payload: Update_Firm):
    firms = await crud.update_law(id, payload)
    if not firms:
        raise HTTPException(status_code=404, detail="Not found")

    return firms


@router.delete("/law/{id}/")
async def delete_law(id: int):
    firm = await crud.delete_firm(id)
    if not firm:
        raise HTTPException(status_code=404, detail="Firm details not found")

    await crud.delete_firm(id)

    if firm:
        return {"Deleted"}