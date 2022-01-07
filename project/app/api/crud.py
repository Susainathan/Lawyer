from typing import Union
from app.models.tortoise import Lawyer
from app.models.pydantic import Add_Firm, Update_Firm, UpdateHierarchy


async def add_law(payload: Add_Firm):
    firm = Lawyer(
        Law_Firm_Name=payload.Law_Firm_Name,
        Law_Firm_Email_Address=payload.Law_Firm_Email_Address,
        Loan_Range=payload.Load_Range,
        Legal_Fee=payload.Legal_Fee,
        Law_Firm_Priority=payload.Law_Firm_Priority,
        Remarks=payload.Remarks,
        Law_Firm_Status=payload.Law_Firm_Status,
        Display_Hierarchy=payload. Display_Hierarchy
    )
    await firm.save()


async def update_law(id: int, payload: Update_Firm) -> Union[dict, None]:
    update_firm = await Lawyer.filter(id=id).update(
        Law_Firm_Name=payload.Law_Firm_Name, Law_Firm_Email_Address=payload.Law_Firm_Email_Address, Loan_Range=payload.Load_Range, Legal_Fee=payload.Legal_Fee, Law_Firm_Priority=payload.Law_Firm_Priority, Remarks=payload.Remarks, Law_Firm_Status=payload.Law_Firm_Status, Display_Hierarchy=payload.Display_Hierarchy
    )
    if update_firm:
        updated_summary = await Lawyer.filter(id=id).first().values()
        return updated_summary
    return None


async def update_key(id: int, payload: UpdateHierarchy) -> Union[dict, None]:
    key = await Lawyer.filter(id=id).update(
        Display_Hierarchy=payload.Display_Hierarchy
    )
    if key:
        updated_summary = await Lawyer.filter(id=id).first().values()
        return updated_summary
    return None

async def get_all_firms():
    bankers = await Lawyer.all().values()
    return bankers



async def delete_firm(id: int):
    del_firm = await Lawyer.filter(id=id).first().delete()
    return del_firm