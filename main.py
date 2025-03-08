from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import UserStory, TestCase
from schemas import UserStoryCreate, UserStoryResponse, TestCaseCreate, TestCaseResponse
from typing import List
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Fetch all user stories
@app.get("/userstories", response_model=List[UserStoryResponse])
def get_userstories(db: Session = Depends(get_db)):
    userstories = db.query(UserStory).all()
    return userstories

# Fetch a user story by id
@app.get("/userstories/{userstory_id}", response_model=UserStoryResponse)
def get_userstory(userstory_id: int, db: Session = Depends(get_db)):
    userstory = db.query(UserStory).filter(UserStory.id == userstory_id).first()
    if userstory is None:
        raise HTTPException(status_code=404, detail="UserStory not found")
    return userstory

# Create a user story
@app.post("/userstories", response_model=UserStoryResponse)
def create_userstory(userstory: UserStoryCreate, db: Session = Depends(get_db)):
    db_userstory = UserStory(title=userstory.title, description=userstory.description)
    db.add(db_userstory)
    db.commit()
    db.refresh(db_userstory)
    return db_userstory

# Fetch all test cases
@app.get("/testcases", response_model=List[TestCaseResponse])
def get_testcases(db: Session = Depends(get_db)):
    testcases = db.query(TestCase).all()
    return testcases

# Fetch a test case by id
@app.get("/testcases/{testcase_id}", response_model=TestCaseResponse)
def get_testcase(testcase_id: int, db: Session = Depends(get_db)):
    testcase = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if testcase is None:
        raise HTTPException(status_code=404, detail="TestCase not found")
    return testcase

# Create test cases
@app.post("/testcases", response_model=List[TestCaseResponse])
def create_testcases(testcases: List[TestCaseCreate], db: Session = Depends(get_db)):
    db_testcases = []
    for testcase in testcases:
        db_testcase = TestCase(
            userstoryid=testcase.userstoryid,
            title=testcase.title,
            description=testcase.description,
            teststeps=testcase.teststeps,
            expected_result=testcase.expected_result,
            status=testcase.status,
            priority=testcase.priority,
            testtype=testcase.testtype
        )
        db.add(db_testcase)
        db.commit()
        db.refresh(db_testcase)
        db_testcases.append(db_testcase)
    return db_testcases

