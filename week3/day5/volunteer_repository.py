from dataclasses import dataclass
import psycopg2

@dataclass
class Location:
    location_id: int
    address: str
    city: str
    district: str
    country: str

@dataclass
class Branch:
    branch_id: int
    location_id: int
    branch_name: str
    contact_info: str

@dataclass
class Mission:
    mission_id: int
    mission: str
    mission_description: str
    volunteering_time: str
    car_needed: bool

conn = psycopg2.connect(
    dbname  ='Volunteer_Matching_System',
    user ='postgres',
    host = 'localhost',
    port ='5432'
)
cursor = conn.cursor()

class DataRepository():
    global cursor

    def get_missions(self) -> list[Mission]:
        cursor.execute("SELECT * FROM missions")
        result = cursor.fetchall()
       
        return [Mission(*mission) for mission in result]
    
    def get_locations(self) -> list[Location]:
        cursor.execute("SELECT * FROM locations")
        result = cursor.fetchall()

        return [Location(*location) for location in result]
   
    def get_branches(self) -> list[Branch]:
        cursor.execute("SELECT * FROM branches")
        result = cursor.fetchall()
        
        return [Branch(*branch) for branch in result]