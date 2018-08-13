from django.contrib import admin
from blog.models import Category,Tag,Post,PostComment

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostComment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # to make the display of field in this order
    fields = ("permalink","title","post_date","release","post_body",
              "category",
              "tags",
              "user")

    # to define readonly fields          
    readonly_fields  = ["permalink"]

    # custom save /update behavior to auto generate permalink
    def save_model(self, request, obj, form, change):
      obj.permalink = obj.title.strip().lower().replace(" ","-")
      super().save_model(request, obj, form, change)
