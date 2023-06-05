import json 
import requests 



URL="http://127.0.0.1:8000" 


# Get Data
def get_data( id = None):
    data={}
    
    if id is not None:
        data={'id':id}
    
    json_data=json.dumps(data)
    
    headers={'content-type':'application/json'}
    r=requests.get(url = URL , headers=headers ,  data = json_data)
     
    res_data=r.json()
    
    print(res_data)


get_data()   



# Insert Data 
# def post_data():
#     data={
#         'name':'mmmmmmmm',
#         'status':'PENDING',
#     }
    
        
#     json_data=json.dumps(data)
    
#     headers={'content-type':'application/json'}
#     r=requests.post(url = URL , headers=headers ,  data = json_data)
     
#     res_data=r.json()
    
#     print(res_data)

# post_data()


# Update Data 

# def update_data():
#     data={
#         'id':13,
#         'name':' bakar',
#         'status':'DONE',
#     }
    
        
#     json_data=json.dumps(data)
    
#     headers={'content-type':'application/json'}
#     r=requests.put(url = URL , headers=headers ,  data = json_data)
     
#     res_data=r.json()
    
#     print(res_data)

# update_data()




# Delete Data 
# def delete_data(id):
#     data={'id':id,}
#     json_data=json.dumps(data)
    
#     headers={'content-type':'application/json'}
#     r=requests.delete(url = URL , headers=headers ,  data = json_data)
    
#     res_data=r.json()
    
#     print(res_data)

# delete_data(3)