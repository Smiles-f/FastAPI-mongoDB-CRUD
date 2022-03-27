from fastapi import FastAPI
from Routes.student import student_router
import uvicorn

app = FastAPI()
#register your router
app.include_router(student_router)

if __name__ =='__main__':
    uvicorn.run(app)
