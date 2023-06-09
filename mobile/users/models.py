from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
# Create your models here.


class CustomUser(AbstractBaseUser):
    phone = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField(blank=True, null=True, max_length=60)
    gender = models.CharField(blank=False, max_length=20)
    firstname = models.CharField(blank=False, max_length=30)
    lastname = models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=True, max_length=20, unique=True)
    birthday = models.DateField(blank=True, null=True)
    followers_count = models.IntegerField(blank=False, default=0)
    following_count = models.IntegerField(blank=False, default=0)
    finrenderer_count = models.IntegerField(blank=False, default=0)
    location = models.CharField(
        blank=True, null=True, default="", max_length=80)
    website = models.CharField(
        blank=True, null=True, default="", max_length=100)
    biograpyh = models.CharField(
        blank=True, null=True, default="", max_length=200)
    qr_code = models.CharField(blank=False, null=False, max_length=100)
    created_at = models.DateTimeField(
        verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="update at", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class OTPRegister(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(blank=False, max_length=100)
    otp = models.CharField(blank=False, max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class OTPForgotPassword(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(blank=False, max_length=100)
    otp = models.CharField(blank=False, max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Followers(models.Model):
    follower_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="follower_user")
    followed_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="followed_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Finrend(models.Model):
    finrender_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="finrender_user")
    finrendered_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="finrendered_user")
    is_finrend_accepted = models.BooleanField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.finrender_user)


class Portfolio(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    portfolio_coin_id=models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


