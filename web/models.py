# encoding=utf-8

from django.db import models
from common.models import (
    BaseModel,
)


class SavorTeam(BaseModel):
    name = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="团队成员名称",
    )
    image = models.ImageField(
        upload_to="image/%Y/%m/%d/",
        verbose_name="NFT头像",
        blank=True,
        null=True,
    )
    introduce = models.CharField(
        max_length=1024,
        default="",
        blank=True,
        null=True,
        verbose_name="成员介绍",
    )
    position = models.CharField(
        max_length=100,
        default="0",
        blank=True,
        null=True,
        verbose_name="团队内部职位",
    )

    is_active = models.BooleanField(
        default=True, verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "团队成员介绍表"
        verbose_name_plural = "团队成员介绍表"

    def __str__(self):
        return self.name

    def as_dict(self):
        return {"id": self.id}


class Position(BaseModel):
    name = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="职位名称",
    )
    is_active = models.BooleanField(
        default=True, verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "职位表"
        verbose_name_plural = "职位表"

    def __str__(self):
        return self.name

    def as_dict(self):
        return {"id": self.id}


class WantJoin(BaseModel):
    position = models.ForeignKey(
        Position,
        related_name="position_relate",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="职位",
    )
    weichat = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="微信",
    )
    email = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="邮箱",
    )
    phone = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="手机号码",
    )
    experience = models.CharField(
        max_length=1024,
        default="",
        blank=True,
        null=True,
        verbose_name="项目经验",
    )
    skill = models.CharField(
        max_length=1024,
        default="",
        blank=True,
        null=True,
        verbose_name="技能",
    )
    is_active = models.BooleanField(
        default=True, verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "加入表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phone

    def as_dict(self):
        return {"id": self.id}

