import asyncio
import tornado.web
import Index
import Profile
import os.path

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)

def makeApp():
    endpoints=[
        ("/",Index.Handler),
        ("/profile/.*",Profile.Handler)
    ]
    
    app = tornado.web.Application(endpoints, static_path=HTMLDIR)
    app.listen(8000)
    print("Point your browser at http:://localhost:8000")
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()