from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# CREATE TABLE `Company` (
# 	`COMPANY_ID`	SERIAL	NOT NULL,
# 	`COMPANY_NAME`	VARCHAR	NOT NULL,
# 	`COUNTRY`	VARCHAR	NOT NULL,
# 	`REGION`	VARCHAR	NOT NULL,
# 	`CREATED_AT`	TIMESTAMP	NOT NULL,
# 	`UPDATED_AT`	TIMESTAMP	NOT NULL
# );

class Company(TimeStampedModel):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    region = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.company_id)
    
    class Meta:
        db_table = 'company'

# CREATE TABLE `User` (
# 	`USER_ID`	SERIAL	NOT NULL,
# 	`USER_NAME`	VARCHAR	NOT NULL,
# 	`CREATED_AT`	TIMESTAMP	NOT NULL,
# 	`UPDATED_AT`	TIMESTAMP	NOT NULL
# );

class User(TimeStampedModel):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        db_table = 'user'

# CREATE TABLE `recruitment` (
# 	`RECRUITMENT_ID`	SERIAL	NOT NULL,
# 	`POSITION`	VARCHAR	NOT NULL,
# 	`COMPENSATION`	INT	NOT NULL,
# 	`CONTENT`	TEXT	NOT NULL,
# 	`SKILL`	VARCHAR	NOT NULL,
# 	`CREATED_AT`	TIMESTAMP	NOT NULL,
# 	`UPDATED_AT`	TIMESTAMP	NOT NULL,
# 	`COMPANY_ID`	INT	NOT NULL
# );

class Recruitment(TimeStampedModel):
    recruitment_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=255, null=False)
    compensation = models.IntegerField(null=False, default=0)
    content = models.TextField(null=False)
    skill = models.CharField(max_length=255, null=False)
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        related_name="company"
    )

    def __str__(self):
        return str(self.recruitment_id)
    
    class Meta:
        db_table = 'recruitment'

# CREATE TABLE `resume` (
# 	`RESUME_ID`	SERIAL	NOT NULL,
# 	`CREATED_AT`	TIMESTAMP	NOT NULL,
#   `UPDATED_AT`	TIMESTAMP	NOT NULL,
# 	`USER_ID`	INT	NOT NULL,
# 	`RECRUITMENT_ID`	INT	NOT NULL
# );

class Resume(TimeStampedModel):
    resume_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user"
    )
    recruitment = models.ForeignKey(
        Recruitment,
        on_delete=models.SET_NULL,
        null=True,
        related_name="recruitment"
    )

    def __str__(self):
        return str(self.resume_id)
    
    class Meta:
        db_table = "resume"
        constraints = [
            models.UniqueConstraint(fields=['user', 'recruitment'], name='unique_user_recruitment')
        ]