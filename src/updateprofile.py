import tornado.web
import json

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
        fullName = J["name"]
        dob = J["birthDate"]
        print("WE GOT:",fullName,dob)

        resp={"ok": True}
        self.write( json.dumps(resp) )
     