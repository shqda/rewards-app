from celery import shared_task
from .models import ScheduledReward, RewardLog


@shared_task
def give_reward(scheduled_reward_id):
    reward = ScheduledReward.objects.get(id=scheduled_reward_id)
    user = reward.user
    user.coins += reward.amount
    user.save()
    RewardLog.objects.create(user=user, amount=reward.amount)
