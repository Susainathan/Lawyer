from tortoise import fields, models


class Lawyer(models.Model):
    id = fields.IntField(pk=True)
    Law_Firm_Name = fields.CharField(max_length=50)
    Law_Firm_Email_Address = fields.CharField(max_length=50)
    Loan_Range = fields.BigIntField()
    Legal_Fee = fields.BigIntField()
    Law_Firm_Priority = fields.CharField(max_length=50)
    Remarks = fields.TextField()
    Law_Firm_Status = fields.CharField(max_length=15)
    Display_Hierarchy = fields.IntField()

