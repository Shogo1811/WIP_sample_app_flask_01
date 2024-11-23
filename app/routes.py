from flask import Blueprint, render_template, request, jsonify
from .database import db
from .models import Employee
from .schemas import employee_schema, employees_schema

app = Blueprint("main", __name__, url_prefix="/")

# 社員一覧（HTML表示）
@app.route("/", methods=["GET"])
def employee_index():
    employees = Employee.query.all()
    return render_template("index.html", employees=employees)

# 社員一覧（API形式）
@app.route("/api/", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    return employees_schema.jsonify(employees)

# 社員詳細（API形式）
@app.route("/api/<int:id>", methods=["GET"])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return employee_schema.jsonify(employee)

# 新しい社員の作成（API形式）
@app.route("/api/", methods=["POST"])
def create_employee():
    data = request.json
    new_employee = Employee(
        name=data["name"],
        email=data["email"],
        department=data["department"]
    )
    db.session.add(new_employee)
    db.session.commit()
    return employee_schema.jsonify(new_employee), 201

# 社員情報の削除
@app.route("/api/<int:id>", methods=["DELETE"])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted"})

# 社員情報の更新
@app.route('/api/<int:id>', methods=["PUT"])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # データを更新
    if "name" in data:
        employee.name = data["name"]
    if "email" in data:
        employee.email = data["email"]
    if "department" in data:
        employee.department = data["department"]

    db.session.commit()
    return employee_schema.jsonify(employee)
