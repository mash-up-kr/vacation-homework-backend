from django.db import models
import json
from vacation.users import models as user_models

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Question(TimeStampedModel):

    """ Single question Model """

    message = models.TextField()

    def __str__(self):
        return self.message


class Question_set(TimeStampedModel):

    """ Question list Model """

    question_list = models.TextField()

    def __str__(self):
        return self.question_list

    @property
    def questions(self):
        dict_quesion = json.loads(self.question_list)

        question_list = []

        for id in dict_quesion:
            current_question = Question.objects.filter(id=id)
            question_list.append(current_question[0])
   
        return question_list


    @property
    def answersCount(self):
       return  answers.objects.filter(di = self.id)
   

class Single_diary(TimeStampedModel):

    """ Single diary Model """

    creator = models.ForeignKey(user_models.User, related_name='diaries', on_delete=models.CASCADE)
    question_set = models.ForeignKey(Question_set, related_name='diaries', on_delete=models.CASCADE)

    @property
    def answer_count(self):
        return answers.all().count()
       
    @property
    def current_question(self):
        imdex = self.answer_count
        q_set = self.question_set.questions # list 
        return q_set[index]


class User_answer(TimeStampedModel):

    """ User answer Model """

    diary = models.ForeignKey(Single_diary, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    creator = models.ForeignKey(user_models.User, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

