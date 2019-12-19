
from django.db import models
from lib.utils.mytime import UtilTime

class Banner(models.Model):

    id=models.AutoField(primary_key=True)
    url = models.CharField(max_length=255,verbose_name="地址")
    createtime = models.BigIntegerField()


    def save(self, *args, **kwargs):
        if not self.createtime:
            self.createtime = UtilTime().timestamp
        return super(Banner, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        db_table = 'banner'


class AttachMentGroup(models.Model):

    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,verbose_name="分组名称",null=True)
    number = models.IntegerField(default=0,verbose_name="数量",null=True)
    createtime = models.BigIntegerField(default=0)


    def save(self, *args, **kwargs):

        # if self.number:
        #     self.number +=1
        # else:
        #     self.number =0

        if not self.createtime:
            self.createtime = UtilTime().timestamp
        return super(AttachMentGroup, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '素材管理'
        verbose_name_plural = verbose_name
        db_table = 'attachmentgroup'

class AttachMent(models.Model):

    id=models.AutoField(primary_key=True)
    url = models.CharField(max_length=255,verbose_name="地址",null=True)
    title = models.CharField(max_length=255,verbose_name="名称",null=True)
    grouid = models.IntegerField(verbose_name="分组ID",null=True)
    createtime = models.BigIntegerField(default=0)
    type   = models.CharField(max_length=255,verbose_name="类型",null=True)


    def save(self, *args, **kwargs):
        if not self.createtime:
            self.createtime = UtilTime().timestamp
        return super(AttachMent, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '素材管理'
        verbose_name_plural = verbose_name
        db_table = 'attachment'


class OtherMemo(models.Model):

    id=models.AutoField(primary_key=True)
    html = models.TextField()
    type = models.CharField(max_length=1,verbose_name="类型,1-公告,2-联系我们")
    createtime = models.BigIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.createtime:
            self.createtime = UtilTime().timestamp
        return super(OtherMemo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '公告联系我们'
        verbose_name_plural = verbose_name
        db_table = 'othermemo'

class Sysparams(models.Model):

    id=models.AutoField(primary_key=True)
    pushtype = models.CharField(max_length=1,verbose_name="小程序发布状态:0-开发,1-审核,2-上线",default="0")


    def save(self, *args, **kwargs):
        if not self.createtime:
            self.createtime = UtilTime().timestamp
        return super(Sysparams, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '参数'
        verbose_name_plural = verbose_name
        db_table = 'sysparams'
