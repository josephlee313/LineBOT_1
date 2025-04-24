from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user_id = models.CharField(max_length=50, unique=True)  # LINE 用戶唯一識別碼
    nickname = models.TextField()  # 顯示暱稱
    total_messages = models.IntegerField(default=0)  # 發言總數
    positive_score = models.IntegerField(default=0)  # 正面語句次數
    negative_score = models.IntegerField(default=0)  # 負面語句次數
    activity_level = models.CharField(max_length=1)  # 活躍等級（S/A/B）
    tags = models.TextField(blank=True)  # 產品喜好、身份標籤（例如媽媽、主婦）


class ChatLog(models.Model):
    message_id = models.AutoField(primary_key=True)  # 訊息編號
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # 發言者 ID
    content = models.TextField()  # 訊息內容
    timestamp = models.DateTimeField(auto_now_add=True)  # 發言時間
    sentiment = models.CharField(max_length=10)  # 情緒傾向（positive/neutral/negative）
    keyword_match = models.JSONField(default=list)  # 匹配的關鍵字清單


class ProductInterest(models.Model):
    product_name = models.TextField(unique=True)  # 商品名稱
    mentions = models.IntegerField(default=0)  # 被提及次數
    wishlist_count = models.IntegerField(default=0)  # 許願次數（含求再開團等語句）
    is_hot = models.BooleanField(default=False)  # 是否為非開團熱門商品


class ActivityTimeSlot(models.Model):
    time_range = models.CharField(max_length=20, unique=True)  # 小時區間（例：09:00-10:00）
    active_user_count = models.IntegerField(default=0)  # 該時段內活躍用戶數
    message_count = models.IntegerField(default=0)  # 發言總數


class CommunityEventLog(models.Model):
    event_id = models.AutoField(primary_key=True)  # 活動編號
    title = models.TextField()  # 活動名稱
    date = models.DateField()  # 活動日期
    tags = models.JSONField(default=list)  # 活動類型標籤（例：抽獎、直播、投票）
    notes = models.TextField(blank=True)  # 備註或活動成果摘要
