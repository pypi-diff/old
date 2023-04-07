# Comparing `tmp/django-common-objects-1.0.4.tar.gz` & `tmp/django-common-objects-1.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-common-objects-1.0.4.tar", last modified: Mon Mar 13 09:55:18 2023, max compression
+gzip compressed data, was "django-common-objects-1.0.5.tar", last modified: Fri Apr  7 08:59:16 2023, max compression
```

## Comparing `django-common-objects-1.0.4.tar` & `django-common-objects-1.0.5.tar`

### file list

```diff
@@ -1,36 +1,40 @@
-drwxrwxrwx   0        0        0        0 2023-03-13 09:55:18.147884 django-common-objects-1.0.4/
--rw-rw-rw-   0        0        0     1085 2023-02-28 03:17:44.000000 django-common-objects-1.0.4/LICENSE
--rw-rw-rw-   0        0        0      296 2023-03-13 09:55:18.147884 django-common-objects-1.0.4/PKG-INFO
--rw-rw-rw-   0        0        0       21 2023-02-28 03:17:44.000000 django-common-objects-1.0.4/README.md
-drwxrwxrwx   0        0        0        0 2023-03-13 09:55:18.131104 django-common-objects-1.0.4/django_common_objects/
--rw-rw-rw-   0        0        0        0 2023-02-28 03:21:57.000000 django-common-objects-1.0.4/django_common_objects/__init__.py
--rw-rw-rw-   0        0        0     5521 2023-02-28 03:24:51.000000 django-common-objects-1.0.4/django_common_objects/admin.py
--rw-rw-rw-   0        0        0      155 2023-02-28 03:45:02.000000 django-common-objects-1.0.4/django_common_objects/apps.py
--rw-rw-rw-   0        0        0     2580 2023-02-28 03:45:52.000000 django-common-objects-1.0.4/django_common_objects/choices.py
--rw-rw-rw-   0        0        0     1498 2023-02-28 03:29:27.000000 django-common-objects-1.0.4/django_common_objects/fields.py
--rw-rw-rw-   0        0        0     1133 2023-03-07 02:45:55.000000 django-common-objects-1.0.4/django_common_objects/forms.py
-drwxrwxrwx   0        0        0        0 2023-03-13 09:55:18.143883 django-common-objects-1.0.4/django_common_objects/migrations/
--rw-rw-rw-   0        0        0     4311 2023-03-07 07:19:54.000000 django-common-objects-1.0.4/django_common_objects/migrations/0001_initial.py
--rw-rw-rw-   0        0        0        0 2023-03-07 07:13:25.000000 django-common-objects-1.0.4/django_common_objects/migrations/__init__.py
--rw-rw-rw-   0        0        0     3920 2023-02-28 03:42:34.000000 django-common-objects-1.0.4/django_common_objects/models.py
--rw-rw-rw-   0        0        0      488 2023-02-16 05:39:51.000000 django-common-objects-1.0.4/django_common_objects/rest_view.py
--rw-rw-rw-   0        0        0      738 2023-02-16 09:09:26.000000 django-common-objects-1.0.4/django_common_objects/serializers.py
--rw-rw-rw-   0        0        0      439 2023-03-13 09:48:04.000000 django-common-objects-1.0.4/django_common_objects/settings.py
--rw-rw-rw-   0        0        0      804 2023-03-13 09:30:10.000000 django-common-objects-1.0.4/django_common_objects/site.py
--rw-rw-rw-   0        0        0       63 2023-02-28 03:21:57.000000 django-common-objects-1.0.4/django_common_objects/tests.py
-drwxrwxrwx   0        0        0        0 2023-03-13 09:55:18.146890 django-common-objects-1.0.4/django_common_objects/utils/
--rw-rw-rw-   0        0        0        0 2023-02-16 03:57:14.000000 django-common-objects-1.0.4/django_common_objects/utils/__init__.py
--rw-rw-rw-   0        0        0      166 2023-02-28 03:30:14.000000 django-common-objects-1.0.4/django_common_objects/utils/admin.py
--rw-rw-rw-   0        0        0      904 2023-02-17 06:35:48.000000 django-common-objects-1.0.4/django_common_objects/utils/algorithm.py
--rw-rw-rw-   0        0        0      522 2023-02-28 03:46:13.000000 django-common-objects-1.0.4/django_common_objects/utils/foreign_key.py
--rw-rw-rw-   0        0        0      880 2023-02-15 06:14:26.000000 django-common-objects-1.0.4/django_common_objects/validator.py
--rw-rw-rw-   0        0        0       66 2023-02-28 03:21:57.000000 django-common-objects-1.0.4/django_common_objects/views.py
--rw-rw-rw-   0        0        0     2183 2023-03-07 02:46:25.000000 django-common-objects-1.0.4/django_common_objects/widgets.py
-drwxrwxrwx   0        0        0        0 2023-03-13 09:55:18.141883 django-common-objects-1.0.4/django_common_objects.egg-info/
--rw-rw-rw-   0        0        0      296 2023-03-13 09:55:18.000000 django-common-objects-1.0.4/django_common_objects.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      994 2023-03-13 09:55:18.000000 django-common-objects-1.0.4/django_common_objects.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-13 09:55:18.000000 django-common-objects-1.0.4/django_common_objects.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       43 2023-03-13 09:55:18.000000 django-common-objects-1.0.4/django_common_objects.egg-info/requires.txt
--rw-rw-rw-   0        0        0       22 2023-03-13 09:55:18.000000 django-common-objects-1.0.4/django_common_objects.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-13 09:55:18.147884 django-common-objects-1.0.4/setup.cfg
--rw-rw-rw-   0        0        0      456 2023-03-13 09:48:10.000000 django-common-objects-1.0.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:59:16.297664 django-common-objects-1.0.5/
+-rw-rw-rw-   0        0        0     1085 2023-02-28 03:17:44.000000 django-common-objects-1.0.5/LICENSE
+-rw-rw-rw-   0        0        0      296 2023-04-07 08:59:16.297664 django-common-objects-1.0.5/PKG-INFO
+-rw-rw-rw-   0        0        0       21 2023-02-28 03:17:44.000000 django-common-objects-1.0.5/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 08:59:16.241406 django-common-objects-1.0.5/django_common_objects/
+-rw-rw-rw-   0        0        0        0 2023-02-28 03:21:57.000000 django-common-objects-1.0.5/django_common_objects/__init__.py
+-rw-rw-rw-   0        0        0     5521 2023-02-28 03:24:51.000000 django-common-objects-1.0.5/django_common_objects/admin.py
+-rw-rw-rw-   0        0        0      155 2023-02-28 03:45:02.000000 django-common-objects-1.0.5/django_common_objects/apps.py
+-rw-rw-rw-   0        0        0     2580 2023-02-28 03:45:52.000000 django-common-objects-1.0.5/django_common_objects/choices.py
+-rw-rw-rw-   0        0        0     1498 2023-02-28 03:29:27.000000 django-common-objects-1.0.5/django_common_objects/fields.py
+-rw-rw-rw-   0        0        0     1374 2023-04-04 01:25:03.000000 django-common-objects-1.0.5/django_common_objects/forms.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:59:16.284383 django-common-objects-1.0.5/django_common_objects/migrations/
+-rw-rw-rw-   0        0        0     4311 2023-03-07 07:19:54.000000 django-common-objects-1.0.5/django_common_objects/migrations/0001_initial.py
+-rw-rw-rw-   0        0        0      832 2023-04-04 01:15:03.000000 django-common-objects-1.0.5/django_common_objects/migrations/0002_alter_commoncategory_model_and_more.py
+-rw-rw-rw-   0        0        0      826 2023-04-07 08:58:05.000000 django-common-objects-1.0.5/django_common_objects/migrations/0003_alter_commoncategory_unique_together_and_more.py
+-rw-rw-rw-   0        0        0        0 2023-03-07 07:13:25.000000 django-common-objects-1.0.5/django_common_objects/migrations/__init__.py
+-rw-rw-rw-   0        0        0     4035 2023-04-07 08:56:28.000000 django-common-objects-1.0.5/django_common_objects/models.py
+-rw-rw-rw-   0        0        0      488 2023-02-16 05:39:51.000000 django-common-objects-1.0.5/django_common_objects/rest_view.py
+-rw-rw-rw-   0        0        0      738 2023-02-16 09:09:26.000000 django-common-objects-1.0.5/django_common_objects/serializers.py
+-rw-rw-rw-   0        0        0      439 2023-03-13 09:48:04.000000 django-common-objects-1.0.5/django_common_objects/settings.py
+-rw-rw-rw-   0        0        0      804 2023-03-13 09:30:10.000000 django-common-objects-1.0.5/django_common_objects/site.py
+-rw-rw-rw-   0        0        0       63 2023-02-28 03:21:57.000000 django-common-objects-1.0.5/django_common_objects/tests.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:59:16.296381 django-common-objects-1.0.5/django_common_objects/utils/
+-rw-rw-rw-   0        0        0        0 2023-02-16 03:57:14.000000 django-common-objects-1.0.5/django_common_objects/utils/__init__.py
+-rw-rw-rw-   0        0        0      166 2023-02-28 03:30:14.000000 django-common-objects-1.0.5/django_common_objects/utils/admin.py
+-rw-rw-rw-   0        0        0      904 2023-02-17 06:35:48.000000 django-common-objects-1.0.5/django_common_objects/utils/algorithm.py
+-rw-rw-rw-   0        0        0      522 2023-02-28 03:46:13.000000 django-common-objects-1.0.5/django_common_objects/utils/foreign_key.py
+-rw-rw-rw-   0        0        0      880 2023-02-15 06:14:26.000000 django-common-objects-1.0.5/django_common_objects/validator.py
+-rw-rw-rw-   0        0        0       66 2023-02-28 03:21:57.000000 django-common-objects-1.0.5/django_common_objects/views.py
+-rw-rw-rw-   0        0        0     2183 2023-03-07 02:46:25.000000 django-common-objects-1.0.5/django_common_objects/widgets.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:59:16.268898 django-common-objects-1.0.5/django_common_objects.egg-info/
+-rw-rw-rw-   0        0        0      296 2023-04-07 08:59:16.000000 django-common-objects-1.0.5/django_common_objects.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1176 2023-04-07 08:59:16.000000 django-common-objects-1.0.5/django_common_objects.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 08:59:16.000000 django-common-objects-1.0.5/django_common_objects.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       43 2023-04-07 08:59:16.000000 django-common-objects-1.0.5/django_common_objects.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       28 2023-04-07 08:59:16.000000 django-common-objects-1.0.5/django_common_objects.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 08:59:16.297664 django-common-objects-1.0.5/setup.cfg
+-rw-rw-rw-   0        0        0      456 2023-04-04 01:29:04.000000 django-common-objects-1.0.5/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:59:16.296381 django-common-objects-1.0.5/tests/
+-rw-rw-rw-   0        0        0        0 2023-04-04 01:09:57.000000 django-common-objects-1.0.5/tests/__init__.py
```

### Comparing `django-common-objects-1.0.4/LICENSE` & `django-common-objects-1.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/admin.py` & `django-common-objects-1.0.5/django_common_objects/admin.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/choices.py` & `django-common-objects-1.0.5/django_common_objects/choices.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/fields.py` & `django-common-objects-1.0.5/django_common_objects/fields.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/forms.py` & `django-common-objects-1.0.5/django_common_objects/forms.py`

 * *Files 24% similar despite different names*

```diff
@@ -15,16 +15,21 @@
         super().__init__(*args, **kwargs)
         instance: CommonCategory = self.instance
         if instance.id:
             self.fields['parent'].queryset = CommonCategory.objects.filter(
                 model=instance.model, user=instance.user
             ).exclude(id__in=foreign_key.get_related_object_ids(instance))
 
-    def is_valid(self):
-        return super().is_valid()
+    def clean(self):
+        cleaned_data = super().clean()
+        model = cleaned_data.get('model')
+        parent = cleaned_data.get('parent')
+        if model and parent and model != parent.model:
+            raise forms.ValidationError('所属模型不一致')
+        return cleaned_data
 
     class Meta:
         model = CommonCategory
         fields = "__all__"
 
 
 class TagForm(forms.ModelForm):
```

### Comparing `django-common-objects-1.0.4/django_common_objects/migrations/0001_initial.py` & `django-common-objects-1.0.5/django_common_objects/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/models.py` & `django-common-objects-1.0.5/django_common_objects/models.py`

 * *Files 5% similar despite different names*

```diff
@@ -47,27 +47,27 @@
 
 class CommonCategory(models.Model):
     id = models.AutoField(primary_key=True)
     model = models.CharField(max_length=100, verbose_name='所属模型')
     parent = models.ForeignKey('self', blank=True, null=True, db_constraint=False, on_delete=models.CASCADE,
                                related_name='children', verbose_name='父类别')
     name = models.CharField(max_length=50, verbose_name='名称')
-    config = ConfigField(default=get_default_config('CommonCategory'), blank=True, null=True, verbose_name='详细')
+    config = models.JSONField(default=get_default_config('CommonCategory'), blank=True, null=True, verbose_name='详细')
     user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_constraint=False, verbose_name='用户')
     create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
     update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
 
     @property
     def related_categories_ids(self):
         return foreign_key.get_related_object_ids(self)
 
     class Meta:
         db_table = 'common_category'
         verbose_name = verbose_name_plural = '通用类别'
-        unique_together = ('user', 'name', 'parent')
+        unique_together = ('name', 'user')
 
     def __str__(self):
         return self.name
 
     __repr__ = __str__
 
 
@@ -96,7 +96,11 @@
 
 
 FORMFIELD_FOR_DBFIELD_DEFAULTS[ConfigField] = {
     "widget": JSONWidget,
     "form_class": FiledConfigFiled
 }
 
+FORMFIELD_FOR_DBFIELD_DEFAULTS[models.JSONField] = {
+    "widget": JSONWidget,
+    "form_class": FiledConfigFiled
+}
```

### Comparing `django-common-objects-1.0.4/django_common_objects/serializers.py` & `django-common-objects-1.0.5/django_common_objects/serializers.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/site.py` & `django-common-objects-1.0.5/django_common_objects/site.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/utils/algorithm.py` & `django-common-objects-1.0.5/django_common_objects/utils/algorithm.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/utils/foreign_key.py` & `django-common-objects-1.0.5/django_common_objects/utils/foreign_key.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/validator.py` & `django-common-objects-1.0.5/django_common_objects/validator.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects/widgets.py` & `django-common-objects-1.0.5/django_common_objects/widgets.py`

 * *Files identical despite different names*

### Comparing `django-common-objects-1.0.4/django_common_objects.egg-info/SOURCES.txt` & `django-common-objects-1.0.5/django_common_objects.egg-info/SOURCES.txt`

 * *Files 15% similar despite different names*

```diff
@@ -18,12 +18,15 @@
 django_common_objects/widgets.py
 django_common_objects.egg-info/PKG-INFO
 django_common_objects.egg-info/SOURCES.txt
 django_common_objects.egg-info/dependency_links.txt
 django_common_objects.egg-info/requires.txt
 django_common_objects.egg-info/top_level.txt
 django_common_objects/migrations/0001_initial.py
+django_common_objects/migrations/0002_alter_commoncategory_model_and_more.py
+django_common_objects/migrations/0003_alter_commoncategory_unique_together_and_more.py
 django_common_objects/migrations/__init__.py
 django_common_objects/utils/__init__.py
 django_common_objects/utils/admin.py
 django_common_objects/utils/algorithm.py
-django_common_objects/utils/foreign_key.py
+django_common_objects/utils/foreign_key.py
+tests/__init__.py
```

