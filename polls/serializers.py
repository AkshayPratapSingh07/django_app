from rest_framework import serializers
from .models import Question, Choice

# class ChoiceSerializer(serializers.ModelSerializer):
#     question_text = serializers.CharField(source='question.question_text', read_only=True)

#     class Meta:
#         model = Choice
#         fields = ['question_text','id', 'choice_text', 'votes',]
class   ChoiceSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(write_only=True)
    question_text = serializers.CharField(source='question.question_text', read_only=True)

    class Meta:
        model = Choice
        fields = ['question_id', 'question_text', 'id', 'choice_text', 'votes']

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Question
        fields = ['id','question_text','pub_date','owner']

    


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date','choices']