import datetime
import logging

from django.db import models
from django.utils import timezone

# logger
logger=logging.getLogger(__name__)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# seedデータを別途投入する
# Jsonを読む方法(loaddata(fixtures))、migrate時に作る方法(post_migrate)、sqlを実行する方法(dumpdata)がある
# railsのdb:reset、C#のEntityFrameworkのUpdate-Databaseをするにはflush後に再度migrate実行してからテストデータを発行する必要がありそう
# 全てをjsonファイルで用意するのは手間なのでfactory boyやsetUp、setUpTestDataを活用するとよさそう
# 例えば負荷テストで大量にデータを用意する場合やデータの関連性を担保する際に使う
# バッチやrunscriptを利用してダミーデータを作成するのもあり
# 理想はテストの度にデータが担保されるべきなのでテスト内で削除→生成は必要
# 負荷試験だったりブラウザでの動作検証用はfixturesかfactory、fakerで作成したデータを使う
# fixtureに関してはマスタデータ以外の利用は厳しい
class Contact(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    mail_address = models.EmailField(max_length=254, null=True)
    status = models.PositiveSmallIntegerField(default=1, max_length=2) # 1:未送信 2: 送信済み 9: 送信失敗
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)