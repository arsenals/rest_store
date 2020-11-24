from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, primary_key=True)
    parent = models.ForeignKey('self',
                               related_name='children',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', null=True, blank=True)


# exact -> =
# проверка значения на равенство
# Product.objects.filter(title__exact='Nike')

# iexact -> ILIKE
# регистронезависимая проверка на равенство
# Product.objects.filter(title__exact='Nike')
# SELECT * FROM product WHERE title ILIKE 'Nike';

# contains -> LIKE
# Product.objects.filter(title__contains='Nike')
# SELECT * FROM product WHERE title LIKE '%Nike%';

# icontains => ILIKE
# Product.objects.filter(title__icontains='Nike')
# SELECT * FROM product WHERE title ILIKE '%Nike%';


# in -> IN
# Product.objects.filter(id__in=[1,2,3,4,6])
# SELECT * FROM products WHERE id IN (1,2,3,4,6);

# featured_categories = Category.objects.filter(status='featured').values('slug')
# Product.objects.filter(category_id__in=featured_categories)
# SELECT * FROM product WHERE category_id IN (SELECT slug FROM category WHERE status = 'featured');

# gt -> >

# Product.objects.filter(price__gt=5000)
# SELECT * FROM product WHERE price > 5000;

# gte -> >=
# Product.objects.filter(price__gte=5000)
# SELECT * FROM product WHERE price >= 5000;

# lt -> <
# Product.objects.filter(price__lt=5000)
# SELECT * FROM product WHERE price < 5000;

# lte -> <=
# Product.objects.filter(price__lte=5000)
# SELECT * FROM product WHERE price <= 5000;

# startswith
# Product.objects.filter(title__startswith='Nike')
# SELECT * FROM product WHERE title LIKE 'Nike%';

# istartswith
# Product.objects.filter(title__istartswith='Nike')
# SELECT * FROM product WHERE title ILIKE 'Nike%';

# endswith
# Product.objects.filter(title__endswith='Nike')
# SELECT * FROM product WHERE title LIKE '%Nike';

# iendswith
# Product.objects.filter(title__endswith='Nike')
# SELECT * FROM product WHERE title ILIKE '%Nike';

# Product.objects.filter(price__gte=15000, price__lte=20000)
# SELECT * FROM product WHERE price >= 15000 AND price <= 20000;

# Product.objects.filter(price__range=(15000, 20000))
# SELECT * FROM product WHERE price BETWEEN 15000 AND 20000;

# isnull
# Category.objects.filter(parent__isnull)
# SELECT * FROM category WHERE parent IS NULL;