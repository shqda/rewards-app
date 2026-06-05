from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RewardLog, ScheduledReward, User


@admin.register(User)
class RewardsUserAdmin(UserAdmin):
    list_display = ["username", "email", "coins", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (("Rewards", {"fields": ("coins",)}),)  # type: ignore


@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ["user", "amount", "execute_at"]


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ["user", "amount", "given_at"]
