from django.contrib import admin

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership, CarPost, CarPostImage, CarPostComment, CarPostFavorite

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'year', 'color', 'rudder_location']
    # fields = ['brand', 'model']
    list_filter = ['license_plate', 'brand', 'model', 'year', 'color', 'rudder_location']
    list_per_page = 20
    search_fields = ['license_plate', 'brand', 'model', 'year', 'color', 'rudder_location']

@admin.register(SpecialMarks)
class SpecialMarksAdmin(admin.ModelAdmin):
    list_display = ['car', 'title']
    list_filter = ['car', 'title']
    list_per_page = 20
    search_fields = ['car__brand', 'title']

@admin.register(PeriodsOwnership)
class PeriodsOwnershipAdmin(admin.ModelAdmin):
    list_display = ['car', 'from_date', 'before_date']
    list_filter = ['car', 'from_date', 'before_date']
    list_per_page = 20
    search_fields = ['car__brand', 'from_date', 'before_date']

@admin.register(CarPost)
class CarPostAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'price']
    list_filter = ['brand', 'model', 'price']
    list_per_page = 20
    search_fields = ['brand', 'model', 'price']

@admin.register(CarPostImage)
class CarPostImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']
    list_per_page = 20

@admin.register(CarPostComment)
class CarCommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'text', 'created']
    list_filter = ['user']
    list_per_page = 20
    search_fields = ['post', 'user__username', 'text', 'created']

@admin.register(CarPostFavorite)
class CarPostFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']
    list_filter = ['user', 'post']
    list_per_page = 20