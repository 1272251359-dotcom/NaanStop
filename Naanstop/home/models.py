# Post model (main feed)
class Post(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title


# Comment model (linked to Post)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Comment by {self.name} on {self.post.title}"
