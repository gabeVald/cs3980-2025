from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse


async def homepage(request):
    return JSONResponse({"Hello": "World"})


app = Starlette(debug=True, routes=[Route("/", homepage)])
