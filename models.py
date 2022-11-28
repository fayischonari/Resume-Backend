from email.policy import default
from http import server
from database import Base
from sqlalchemy import TIMESTAMP, Date, ForeignKey, String,INTEGER,Column,DateTime,text
from datetime import datetime

class applicant(Base):
    __tablename__="primary_details"

    basic_details_id=Column(INTEGER,primary_key=True)
    name=Column(String(25),nullable=False)
    email=Column(String(25),nullable=False)
    phone=Column(String(25),nullable=False)
    summary=Column(String(500),nullable=True)
    image_URL=Column(String(100),nullable=True)
    date_applied=Column(TIMESTAMP(timezone=True),server_default=text('now()'),nullable=False)


class address(Base):
    __tablename__="address_details"

    address_id=Column(INTEGER,primary_key=True)
    basic_details_id=Column(INTEGER,ForeignKey("primary_details.basic_details_id",ondelete="CASCADE"))
    House_name=Column(String(50),nullable=False)
    Street=Column(String(25),nullable=False)
    City=Column(String(25),nullable=False)
    Country=Column(String(50),nullable=False)
    pincode=Column(String(25),nullable=False)



class education(Base):
    __tablename__="educational_detals"

    education_id=Column(INTEGER,primary_key=True)
    basic_details_id=Column(INTEGER,ForeignKey("primary_details.basic_details_id",ondelete="CASCADE"))
    Qualification=Column(String(25),nullable=False)
    Course_name=Column(String(25),nullable=False)
    University_name=Column(String(25),nullable=False)
    Location=Column(String(25),nullable=False)
    passing_year=Column(Date,nullable=False)


class experience(Base):
    __tablename__="experience_details"

    experience_id=Column(INTEGER,primary_key=True)
    basic_details_id=Column(INTEGER,ForeignKey("primary_details.basic_details_id",ondelete="CASCADE"))
    role=Column(String(25),nullable=True)
    start_date=Column(Date,nullable=True)
    end_date=Column(Date,nullable=True)
    company_name=Column(String(25),nullable=True)
    location=Column(String(25),nullable=True)


class skills(Base):
    __tablename__="skill_details"

    skill_id=Column(INTEGER,primary_key=True)
    basic_details_id=Column(INTEGER,ForeignKey("primary_details.basic_details_id",ondelete="CASCADE"))
    skill_name=Column(String(25),nullable=False)
    skill_level=Column(String(25),nullable=False)
    

class projects(Base):
    __tablename__="project_details"

    project_id=Column(INTEGER,primary_key=True)
    basic_details_id=Column(INTEGER,ForeignKey("primary_details.basic_details_id",ondelete="CASCADE"))
    project_title=Column(String(25),nullable=True)
    project_description=Column(String(100),nullable=True)

class social(Base):
    __tablename__="social_meadia_details"

    social_id=Column(INTEGER,primary_key=True)
    basic_details_id=Column(INTEGER,ForeignKey("primary_details.basic_details_id",ondelete="CASCADE"))
    platform=Column(String(25),nullable=True)
    username=Column(String(25),nullable=True)
    social_URL=Column(String(50),nullable=True)


