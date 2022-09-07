from pymongo import MongoClient

# could be this 
# uri = "mongodb://vagrant:vagrant@192.168.2.14:27017/admin"

# test this using the command line 
uri = "mongodb://vagrant:vagrant@192.168.2.14:3000/admin"


def bfs(paper_code, coll):
    # by paper_code id
    visited = []
    queue = []

    adj_dict = {}

    # initalsie with empty list
    adj_dict[paper_code] = []
    visited.append(paper_code)
    queue.append(paper_code)

    while queue:
        # current node
        s = queue.pop(0)

        doc = coll.find_one({'paper_code':s})
        
        # essentially the neighbours
        prereqs = []
        if (doc is not None):
            prereqs = doc['prereq_list']
        # the neighbours
        for pre_paper in prereqs:
            result = coll.find_one({'paper_code': pre_paper})
            if (result is not None):
                if (result['paper_code'] not in set(adj_dict.keys())):
                    adj_dict[s] = result['prereq_list']
                else:
                    adj_dict[s] += [result]
            if pre_paper not in visited:
                visited.append(pre_paper)
                queue.append(pre_paper)
    
    # adjacentcy dict 
    return adj_dict


def get_prereq_list(paper_code):
    # Replace the uri string with your MongoDB deployment's connection string.
    client = MongoClient(uri)
    
    # database and collection code goes here
    db = client.admin
    coll = db.papers

    doc = coll.find_one({'paper_code':paper_code})
    prereqs = doc['prereq_list']

    adj_dict = bfs(paper_code, coll)
    
    # Close the connection to MongoDB when you're done.
    client.close()

    return adj_dict


if __name__ == '__main__':
    get_prereq_list('MATH306')