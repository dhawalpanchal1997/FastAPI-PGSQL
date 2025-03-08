from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

class UserStory(Base):
    __tablename__ = "userstories"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    test_cases = relationship("TestCase", back_populates="userstory")
   

class TestCase(Base):
    __tablename__ = "testcases"
    
    id = Column(Integer, primary_key=True, index=True)
    userstoryid = Column(Integer, ForeignKey("userstories.id", ondelete="CASCADE"))
    title = Column(String)
    description = Column(String)
    teststeps = Column(String)
    expected_result = Column(String)
    status = Column(String)
    priority = Column(String)
    testtype = Column(String)
    
    userstory = relationship("UserStory", back_populates="test_cases")