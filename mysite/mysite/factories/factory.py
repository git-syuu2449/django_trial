'''
Factory
TODO： 実運用の際はモデルごとに分離
公式
https://pypi.org/project/factory-boy/
'''
from factory.django import DjangoModelFactory
from factory import Sequence, fuzzy, FuzzyChoice
# from faker import Faker
from faker import Factory
from django.utils import timezone

from polls.models import *

fakegen = Faker('ja_JP')

class QuestionFactory(DjangoModelFactory):
    '''
    QuestionモデルのFactoryクラス
    '''
    class Meta:
        model = Question

    question_text = factory.Sequence(lambda n: u'質問 %d' % n)
    pub_date = timezone.now()

class ChoiceFactory(DjangoModelFactory):
    '''
    ChoiceモデルのFactoryクラス
    '''
    class Meta:
        model = Choice

    # questionは外部からQuestionをselectして挿入
    choice_text = factory.Sequence(lambda n: u'選択肢 %d' % n)
    votes = fuzzy.FuzzyInteger(1, 5)

class ContactFactory(DjangoModelFactory):
    '''
    ContactモデルのFactoryクラス
    '''
    class Meta:
        model = Contact

    title = factory.Sequence(lambda n: u'問い合わせ %d' % n)
    text = factory.Sequence(lambda n: u'内容 %d' % n)
    mail_address = fakegen.email()
    status = factory.fuzzy.FuzzyChoice([1, 2, 9])
