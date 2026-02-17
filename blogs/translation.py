from modeltranslation.translator import translator, TranslationOptions
from .models import Post, Category

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'content',)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Post, PostTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
