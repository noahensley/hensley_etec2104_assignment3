import tornado.web

D={
    "alice": {
        "name" : "Alice Smith", 
        "dob" : "Jan. 1",
        "email": "alice@example.com",
        "icon": "/static/alice_smith.png"
    },
    "bob": { 
        "name" : "Bob Jones",
        "dob" : "Dec. 31",
        "email" : "bob@bob.xyz",
        "icon": "/static/bob_jones.png"
    },
    "carol": {
        "name" : "Carol Ling",
        "dob" : "Jul. 17",
        "email" : "carol@example.com",
        "icon": "/static/carol_ling.png"
    },
    "dave": {
        "name" : "Dave N. Port",
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
                name=info["name"], dateOfBirth=info["dob"],
                email=info["email"], user=uname, icon=info["icon"])