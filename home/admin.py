from django.contrib import admin
from .models import Service, Slider, Contact, Feature, HomePage, HomePageService, HomePageFeature


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    search_fields = ('title', 'description')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image', 'button_text', 'button_url')
    search_fields = ('title', 'subtitle')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')
    search_fields = ('phone', 'email')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')
    search_fields = ('name', 'description')


class HomePageServiceInline(admin.TabularInline):
    model = HomePageService
    extra = 1


class HomePageFeatureInline(admin.TabularInline):
    model = HomePageFeature
    extra = 1


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('slider', 'contact_info')
    inlines = [HomePageServiceInline, HomePageFeatureInline]
    search_fields = ('slider__title', 'contact_info__email')


# Optional: Register intermediate models if you want them explicitly in the admin
@admin.register(HomePageService)
class HomePageServiceAdmin(admin.ModelAdmin):
    list_display = ('homepage', 'service')
    search_fields = ('homepage__slider__title', 'service__title')


@admin.register(HomePageFeature)
class HomePageFeatureAdmin(admin.ModelAdmin):
    list_display = ('homepage', 'feature')
    search_fields = ('homepage__slider__title', 'feature__name')


