import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Post, Comment
from django.utils import timezone


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query(ObjectType):
    post = graphene.Field(PostType, id=graphene.Int())
    posts = graphene.List(PostType)
    comment = graphene.Field(CommentType, id=graphene.Int())
    comments = graphene.List(CommentType)

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Post.objects.get(pk=id)

        return None

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Comment.objects.get(pk=id)

        return None

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()


# Create input-type for Post
class PostInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    author = graphene.String()


class CommentInput(graphene.InputObjectType):
    id = graphene.ID()
    post = graphene.Field(PostInput)
    text = graphene.String()
    author = graphene.String()


# Create mutations for Post
class CreatePost(graphene.Mutation):
    class Arguments:
        input = PostInput(required=True)

    ok = graphene.Boolean()
    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        post_instance = Post(title=input.title,
                             description=input.description,
                             author=input.author)

        post_instance.save()
        return CreatePost(ok=ok, post=post_instance)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PostInput(required=True)

    ok = graphene.Boolean()
    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        post_instance = Post.objects.get(pk=id)
        if post_instance:
            ok = True
            post_instance.title = input.title
            post_instance.description = input.description
            post_instance.author = input.author
            post_instance.publish_date = timezone.now()

            post_instance.save()
            return UpdatePost(ok=ok, post=post_instance)
        return UpdatePost(ok=ok, post=None)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()
    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, id):
        ok = False
        post_instance = Post.objects.get(pk=id)

        if post_instance:
            ok = True
            post_instance.delete()
            return DeletePost(ok=ok)
        return DeletePost(ok=ok)


class CreateComment(graphene.Mutation):
    class Arguments:
        input = CommentInput(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(CommentType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actors = []

        post = Post.objects.get(pk=input.post.id)
        if post is None:
            return CreateComment(ok=False, comment=None)

        comment_instance = Comment(
          post=post,
          text=input.text,
          author=input.author
          )

        comment_instance.save()
        return CreateComment(ok=ok, comment=comment_instance)


class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, root, info, id):
        ok = False
        comment_instance = Comment.objects.get(pk=id)

        if comment_instance:
            ok = True
            comment_instance.delete()
            return DeleteComment(ok=ok)
        return DeleteComment(ok=ok)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()

    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
