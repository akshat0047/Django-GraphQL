import graphene
from apps.reckonsys.schema import Query as Q, Mutation as M


class Query(Q, graphene.ObjectType):
    pass


class Mutation(M, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
