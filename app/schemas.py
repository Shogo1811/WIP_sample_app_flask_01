from flask_marshmallow import Marshmallow

ma = Marshmallow()

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "department")

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
