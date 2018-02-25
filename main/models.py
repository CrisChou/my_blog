from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(User):
    """
    用户表
    """
    avatar = models.ImageField(verbose_name='头像')

    def __str__(self):
        return self.first_name


# class Blog(models.Model):
#     """
#     博客信息
#     """
#     nid = models.BigAutoField(primary_key=True)
#     title = models.CharField(verbose_name='个人博客标题', max_length=64)
#     site = models.CharField(verbose_name='个人博客前缀', max_length=32)
#     theme = models.CharField(verbose_name='博客主题', max_length=32)
#     user = models.CharField(verbose_name='所属用户', max_length=32)

#     def __str__(self):
#         return self.title


# class Category(models.Model):
#     """
#     博主个人文章分类表
#     """
#     nid = models.AutoField(primary_key=True)
#     title = models.CharField(verbose_name='分类标题', max_length=32)

#     # blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid')
#     def __str__(self):
#         return self.title


class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)
    # blog = models.ForeignKey(verbose_name='所属博客', to=Blog, on_delete=models.SET_NULL, to_field='nid', null=True)
    def __str__(self):
        return self.title


class Article(models.Model):
    type_choices = [
        (1, "Python"),
        (2, "Django"),
        (3, "JavaScripy"),
        (4, "MySql"),
        (5, "Scrapy"),
    ]
    nid = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name='文章标题', max_length=128)
    summary = models.CharField(verbose_name='文章简介', max_length=255)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid')
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='文章类型', to_field='nid', null=True)
    article_type_id = models.IntegerField(choices=type_choices, default=None)
    tags = models.ManyToManyField(
        verbose_name='文章个人标签',
        to=Tag,)

    def __str__(self):
        return self.title





class ArticleDetail(models.Model):
    """
    文章详细表
    """
    content = models.TextField(verbose_name='文章内容')
    article = models.OneToOneField(verbose_name='所属文章', to=Article, on_delete=models.SET_NULL, to_field='nid', null=True)


# class UpDown(models.Model):
#     """
#     文章顶或踩
#     """
#     article = models.ForeignKey(verbose_name='文章', to=Article, on_delete=models.SET_NULL, to_field='nid',null=True)
#     user = models.ForeignKey(verbose_name='赞或踩用户', to=UserInfo, on_delete=models.SET_NULL, to_field='nid',null=True)
#     up = models.BooleanField(verbose_name='是否赞')

#     class Meta:
#         unique_together = [
#             ('article', 'user'),
#         ]


# class Comment(models.Model):
#     """
#     评论表
#     """
#     nid = models.BigAutoField(primary_key=True)
#     content = models.CharField(verbose_name='评论内容', max_length=255)
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

#     reply = models.ForeignKey(verbose_name='回复评论', to='self', related_name='back', null=True)
#     article = models.ForeignKey(verbose_name='评论文章', to=Article, to_field='nid')
#     user = models.ForeignKey(verbose_name='评论者', to=UserInfo, to_field='nid')






class Article2Tag(models.Model):
    article = models.ForeignKey(verbose_name='文章', to=Article, on_delete=models.SET_NULL, to_field='nid', null=True)
    tag = models.ForeignKey(verbose_name='标签', to=Tag, on_delete=models.SET_NULL, to_field='nid', null=True)

    class Meta:
        unique_together = [
            ('article', 'tag'),
        ]