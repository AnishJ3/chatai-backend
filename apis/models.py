from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Data(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class UserAccountManager(BaseUserManager):

    def create_user(self,email,name, password = None):
        if not email:
            raise ValueError('Users must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email,name = name)

        user.set_password(password)
        user.save()
        return user
    # def create_superuser():

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    name= models.CharField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    ID_FIELD  = 'user_id'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        return self.name
    
    def __str__(self):
        return self.email
    

class Chats(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    chat_title = models.TextField()
    def __str__(self):
        return f"Chat {self.chat_id} by {self.user_id}"

class ChatHistory(models.Model):
    prompt_id = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey(Chats, on_delete=models.CASCADE, related_name='history')
    prompt = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Prompt {self.prompt_id} for Chat {self.chat_id}"