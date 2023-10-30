import strawberry

@strawberry.type
class Mutation:
    @strawberry.mutation
    def twice(num: int)-> int:
        return num * 2
