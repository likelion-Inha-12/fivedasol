from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, id, email, name, generation, gender, password=None):

        user = self.model(
            id = id,
            email=self.normalize_email(email),
            # 이메일 정규화 '소문자(or 숫자)@소문자'
            name=name,
            generation = generation,
            gender = gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, email, name, generation, gender, password):
        user = self.create_user(
            id,
            email = email,
            name=name,
            generation = generation,
            gender = gender,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER_OPT =(
        ('남자', '남자'),
        ('여자', '여자'),
    )
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )

    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    generation = models.IntegerField(default=0)
    gender = models.CharField(max_length=2, choices=GENDER_OPT, default='')

    objects = UserManager()

    USERNAME_FIELD = 'id' # 로그인 할 때 id값 사용함
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'user' # 테이블명을 user로 설정
