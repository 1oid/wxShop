from django.db import models


class Category(models.Model):
    """
    标签分类
    """
    category_name = models.CharField(max_length=50, verbose_name="分类名")
    category_rank = models.IntegerField(default=1, verbose_name="优先级(越大越优先)")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "分类管理"


class Product(models.Model):
    """
    商品
    """
    product_name = models.CharField(max_length=50, verbose_name="商品名")
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_description = models.TextField(verbose_name="商品介绍")
    product_price = models.FloatField(default=0.0, verbose_name="商品价格")
    product_amount = models.IntegerField(default=9999, verbose_name="商品数量")

    product_status = models.BooleanField(default=True, verbose_name="商品出售中")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="商品创建时间")

    def __str__(self):
        return self.product_name

    def decrease_product_amount(self, amount=1):
        if self.product_amount <= 0:
            return

        self.product_amount = self.product_amount - amount
        self.save()

    class Meta:
        verbose_name = "商品管理"
