import logging
from django.core.management.base import BaseCommand
# from django.db import transaction
from django.utils import timezone
from django.core.mail import send_mail

logger=logging.getLogger(__name__)

class Command(BaseCommand):
    '''
    メール送信バッチ
    実際の運用ではメール送信用テーブルから取得して送信
    '''

    help = '実行方法： python manage.py send_mail'

    def handle(self, *args, **options):
        logger.info('バッチ処理を開始')

        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        logger.info('バッチ処理を終了')
