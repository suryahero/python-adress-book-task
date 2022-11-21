from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from task import router as task_router
from account import router as account_router
from address import router as address_router
from theme import router as theme_router

app = FastAPI(title="Address Book App",
    docs_url="/address-book-docs",
    version="0.0.1")


@app.get("/")
async def root():
    return {"message": "Hello Address Book API Jackson"}


app.include_router(task_router.router)
app.include_router(account_router.router)
app.include_router(theme_router.router)
app.include_router(address_router.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    