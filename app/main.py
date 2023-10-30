import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from mutation import Mutation
from query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema=schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
