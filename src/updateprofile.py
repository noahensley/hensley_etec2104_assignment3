import tornado.web
import json
import base64

D={
    "alice": {
        "fname": "Alice", 
        "lname": "Smith",
        "dob": "Jan. 1",
        "email": "alice@example.com",
        "icon": "/static/alice_smith.png"
    },
    "bob": { 
        "fname": "Bob",
        "lname": "Jones",
        "dob": "Dec. 31",
        "email": "bob@bob.xyz",
        "icon": "/static/bob_jones.png"
    },
    "carol": {
        "fname": "Carol",
        "lname": "Ling",
        "dob": "Jul. 17",
        "email": "carol@example.com",
        "icon": "/static/carol_ling.png"
    },
    "dave": {
        "fname": "Dave",
        "lname": "N. Port",
        "dob" : "Mar. 14",
        "email" : "dave@dave.dave",
        "icon": "/static/dave_n_port.png"
    }
}

class Handler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        info = D[uname]
        if info:
            self.render( "updateprofile.html",
                fname=info["fname"], lname=info["lname"], dateOfBirth=info["dob"],
                email=info["email"], user=uname, icon=info["icon"])
            
    def post(self):
        J=json.loads(self.request.body)
        userName = J["userName"]
        firstName = J["firstName"]
        lastName = J["lastName"]
        dob = J["birthDate"]
        ppic = base64.b64decode(J["pic"])
        ppic_str = J["pic"]
        print("WE GOT:",userName,firstName,lastName,dob,ppic[:20])

        # writes the data to the dictionary
        D[userName]["fname"] = firstName
        D[userName]["lname"] = lastName
        D[userName]["dob"] = dob    
        if ppic[:4] == b'\x89PNG': # PNG
            image_data = "data:image/png;base64," + ppic_str
            # print(image_data)
            D[userName]["icon"] = image_data
        elif ppic[:4] == b'\xff\xd8': # JPEG
            image_data = "data:image/jpeg;base64," + ppic_str
            # print(image_data)
            D[userName]["icon"]

        # presents the updated info to the user
        info = D[userName]
        if info:
            self.render( "updateprofile.html",
                fname=info["fname"], lname=info["lname"], dateOfBirth=info["dob"],
                email=info["email"], user=userName, icon=info["icon"])
            
        