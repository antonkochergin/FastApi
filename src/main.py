import asyncio
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(root_path="/api/v1")

app.add_middleware(
    CORSMiddleware, # type: ignore
    allow_origins=["*"], # с каких можно запускать
    allow_credentials=True,
    allow_methods=["*"], # какие можно вызывать метода get/set
    allow_headers=["*"], # разрешения по запросам jwt
)
# по умолчанию все запрещено


# описание как запускать приложение
async def run() -> None:
    # в файле main приложение app
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, reload=False)
    server = uvicorn.Server(config=config)
    # задачи
    tasks = (
        asyncio.create_task(server.serve()),
    )
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

# точка входа в приложение
if __name__ == "__main__":
    loop = asyncio.get_event_loop() # крутит в себе все задачи приложения
    loop.run_until_complete(run()) #



# роберт мартин - чистый код,чистая архитектура