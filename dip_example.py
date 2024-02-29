from app_dip2 import API, Database, FrontEnd

db_front_end = FrontEnd(Database())
print(db_front_end.display_data())

api_front_end = FrontEnd(API())
print(api_front_end.display_data())
