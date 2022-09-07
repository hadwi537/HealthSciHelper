from pymongo import MongoClient


uri = "mongodb://vagrant:vagrant@localhost:27017/admin"


def connect_to_mongo_db():
    # Replace the uri string with your MongoDB deployment's connection string.
    client = MongoClient(uri)

    # database and collection code goes here
    db = client.admin
    coll = db.papers

    # coll.drop()
    # insert code goes here
    data = [
        {'paper_code': "MATH306", 'year': "2022", 'title': "Geometry of Curves and Surfaces", 'points': "18", 'teaching_period': "S2", 
                'subject': "Mathematics", 'prereq_string': "36 points at 200 level", 'prereq_list': ['MATH203', 'MATH202'], 'dl_dict': 'none'},
        {'paper_code': "COSC343", 'year': "2022", 'title': "AI", 'points': "18", 'teaching_period': "S2", 
                'subject': "Computer Science", 'prereq_string': "36 points at 200 level", 'prereq_list': ['COSC343', 'MATH202'], 'dl_dict': 'none'},
        {'paper_code': "MATH202", 'year': "2022", 'title': "Multivariable calculus", 'points': "18", 'teaching_period': "S1", 
                'subject': "Mathematics", 'prereq_string': "MATH170", 'prereq_list': ['MATH170'], 'dl_dict': 'none'},
    ]
    result = coll.insert_many(data)
    # display the results of your operation
    print(result.inserted_ids)
    # Close the connection to MongoDB when you're done.
    client.close()

if __name__ == '__main__':
    connect_to_mongo_db()