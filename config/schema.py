import graphene

import hackernews.links.schema

class Query(hackernews.links.schema.Query, graphene.ObjectType):
    pass


class Mutation(hackernews.links.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
