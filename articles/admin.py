from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import *

class ArticleScopeTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag = 0

        for form in self.forms:
            if form.cleaned_data['is_main']:
                tag += 1

        if tag < 1:
            raise ValidationError('Укажите Основной раздел')
        elif tag > 1:
            raise ValidationError('Основным может быть только одни раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeTagInline(admin.TabularInline):
    model = ArticleScopeTag
    formset = ArticleScopeTagInlineFormset
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeTagInline]
