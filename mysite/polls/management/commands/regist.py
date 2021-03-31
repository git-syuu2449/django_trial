import logging
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from polls.models import Choice, Question

logger=logging.getLogger(__name__)

class Command(BaseCommand):
    help = '実行方法： python manage.py regist 1 --opt 2'
    def add_arguments(self, parser):
        parser.add_argument('opt1', help='必須オプション')
        parser.add_argument('--opt2', help='任意オプション')

    def handle(self, *args, **options):
        logger.info('バッチ処理を開始')
        
        logger.info('options: ' + options.__str__())
        self.stdout.write(options.__str__())
        
        # サンプルとしてQuestionモデルにインサートして更新する
        regist_question()
        
        logger.info('バッチ処理を終了')

# TODO: Modelに切り出し
def regist_question():
    try:
        register = Question(question_text="batch register", pub_date=timezone.now())
        register.save()
        logger.info('登録完了')

        with transaction.atomic():
            question = Question.objects.select_for_update().get(id=register.id)
            logger.debug(question)
            question.question_text = 'change text'
            question.save()
            logger.info('更新完了')
    except Exception as e:
        logger.error(e)
        transaction.rollback()
    else:
        transaction.commit()
