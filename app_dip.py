# you should not do

# Say you are building an application that have a FrontEnd class to display data 
# to the users in a friendly way. The app currently gets its data from a database,
# so you end up with the following code 

class FrontEnd:
    def __init__(self, backend):
        self.backend = backend

    def get_data(self):
        data = self.backend.get_data_from_database()
        print("Display data: ", data)

class Backend:
        def get_data_from_database(self):
             return "Data from database"
        
# In this example the FrontEnd class depends on the Backend class and its concrete 
# implementation. You can say that both classes are tightly coupled. This coupling
# can lead to the scalability issues. For example, say your app is growing fast
# and you want the app to be able to read data from REST API.
# You may think adding a new method to the BackEnd to retrieve data from the REST API.
# However, that will also require to modify FrontEnd.

