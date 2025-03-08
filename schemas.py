from pydantic import BaseModel
from typing import List, Optional

#schemas for the UserStory models
class UserStoryBase(BaseModel):
    title: str
    description: str

class UserStoryCreate(UserStoryBase):
    pass

class UserStoryResponse(UserStoryBase):
    id: int
    
    class Config:
        from_attributes = True

#schemas  for the TestCase models
class TestCaseBase(BaseModel):
    userstoryid: int
    title: str
    description: str
    teststeps: str
    expected_result: str
    status: str
    priority: str
    testtype: str

class TestCaseCreate(TestCaseBase):
    pass

class TestCaseResponse(TestCaseBase):
    id: int
    class Config:
        from_attributes = True



