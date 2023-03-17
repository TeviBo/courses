from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """

    def create_user(self, email, name, password=None):
        """Creates a new user profile

        Args:
            email (string): user email
            name (string): user name
            password (password, optional): user password. Defaults to None.

        Returns:
            _type_: UserProfile
        """
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # This method is inherited from AbstractBaseUser class and it hash the password
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details

        Args:
            email (_type_): _description_
            name (_type_): _description_
            password (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    """ Cuando se autentiquen, mediante este metodo indicamos que
    en lugar de utilizar el nombre de la persona,
    utilizara el campo email como usuario """
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """
        Retrieve full name of user
        """
        return self.name

    def get_short_name(self):
        """
        Retrieves short name of the user
        """
        return self.name

    def __str__(self):
        """
        Return string representation of our user
        """
        return self.email
