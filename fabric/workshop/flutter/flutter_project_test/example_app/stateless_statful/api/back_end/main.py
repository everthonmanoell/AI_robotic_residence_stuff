from fastapi import FastAPI, Response, Request
from back_end.proto.package import User, UserList

app = FastAPI()

user_list = UserList()

@app.get("/get-users")
def get_users():
    return Response(
        content=bytes(user_list),
        status_code=200
    )

@app.post("/add-user")
async def add_user(request: Request):
    global user_list
    # Lê os bytes brutos enviados pelo front
    raw_body = await request.body()

    # Desserializa para o proto
    user = User()
    user.parse(raw_body)
    user_list.users.append(user)

    return Response(status_code=200)

@app.post("/remove-user")
async def remove_user(request: Request):
    global user_list
    # Lê os bytes brutos enviados pelo front
    raw_body = await request.body()

    # Desserializa para o proto
    user = User()
    user.parse(raw_body)
    for u in user_list.users:
        if user.name == u.name:
            user_list.users.remove(u)

    return Response(status_code=200)