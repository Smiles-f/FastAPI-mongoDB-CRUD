#imoport statement
from fastapi import APIRouter
from Models.student import Student
from Config.database import connection
from Schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

@student_router.get('/hello')
async def hell0_world():
    return 'hello world'

#getting all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

#finding a student with a matching id
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({'_id': ObjectId(studentId)}))

#creating a student
@student_router.post('/students')
async def create_students(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

#update a student
@student_router.put('/students/{studentId}')
async def update_students(studentId, student:Student):
    #find the student and then update it with new student data
    connection.local.student.find_one_and_update(
        {'_id': ObjectId(studentId)},
        {'$set': dict(student)}
    )
    return studentEntity(connection.local.student.find_one({'_id':ObjectId(studentId)}))

#delete a student

@student_router.delete('/students/{studentId}')

async def delete_student(studentId):
    #find the student to delete
    return studentEntity(connection.local.student.find_one_and_delete({'_id': ObjectId(studentId)}))