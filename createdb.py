from database import Base,engine
from models import applicant

Base.metadata.create_all(engine)