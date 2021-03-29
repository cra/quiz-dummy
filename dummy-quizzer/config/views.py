import textwrap
import random
from typing import NamedTuple, Optional
import json

from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4, UUID


class Label(NamedTuple):
    min_: str
    max_: str
    na_: Optional[str] = None

    def json(self):
        if self.na_ is None:
            return {'min': self.min_, 'max': self.max_}
        else:
            return {'min': self.min_, 'max': self.max_, 'na': self.na_}


class Question(NamedTuple):
    text: str
    labels: Label
    question_uuid: UUID

    def json(self):
        return {
            'text': self.text,
            'labels': self.labels.json(),
            'question_uuid': self.question_uuid,
        }


UUID = '6f208012-7882-45c4-b04c-aed368c593f9'
QID1 = '6f208012-7882-45c4-b04c-ae0000000001'
QID2 = '6f208012-7882-45c4-b04c-ae0000000002'
QID3 = '6f208012-7882-45c4-b04c-ae0000000003'
QID4 = '6f208012-7882-45c4-b04c-ae0000000004'


@csrf_exempt
def index(request):
    return JsonResponse({
            '_links': [
                '/q/quiz-slug',
                f'/q/quiz-slug/{UUID}',
                f'/q/quiz-slug/{UUID}/1',
                f'/q/quiz-slug/{UUID}/1/score',
                f'/q/quiz-slug/{UUID}/2',
                f'/q/quiz-slug/{UUID}/2/score',
                f'/q/quiz-slug/{UUID}/3',
                f'/q/quiz-slug/{UUID}/3/score',
                f'/q/quiz-slug/{UUID}/final',
            ],
            'message': 'quiz-slug can by any slug string',
        }
    )

@csrf_exempt
def quiz_start(request, quiz_slug):
    if request.method == 'GET':
        return JsonResponse({
                'header': f'Quiz for {quiz_slug}',
                'intro_text': 'Very <b>cool</b> please <i>proceed</i> yes',
                'checkbox_text': 'Agree to sell your soul to the devil',
                'button_text': "Let's go",
            }
        )
    elif request.method == 'POST':
        return redirect(f'/q/{quiz_slug}/{UUID}/1')


@csrf_exempt
def quiz_section(request, quiz_slug, user_uuid, section_part):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError as err:
            print('ERROR decoding json:', err)
        else:
            print(f'request body i got: {body}')
            if 'answers' in body:
                for q_id in [QID1, QID2, QID3, QID4]:
                    if q_id in body['answers']:
                        print(f"Found response for {q_id}: {body['answers'][q_id]}")
            return redirect(f'/q/{quiz_slug}/{UUID}/{section_part}/score')
    questions = [
        Question(
            text="Какое жывотне вы кусаити?",
            labels=Label('1', '5'),
            question_uuid=QID1,
        ),
        Question(
            text="How you met your mother? Assuming you are not a god and you have one. You do, right?",
            labels=Label('Lol what', 'Fuck yeah', 'Yes daddy'),
            question_uuid=QID2,
        ),
        Question(
            text="Is there anybody out there?",
            labels=Label('No', 'Yes', 'Pink Floyd sucks'),
            question_uuid=QID3,
        ),
        Question(
            text="Did you ever hear the Tragedy of Darth Plagueis the Wise?",
            labels=Label('Ironic', 'Yes', 'Not like this!'),
            question_uuid=QID4,
        )
    ]
    random.shuffle(questions)
    return JsonResponse({
            'header': f'Quiz for {quiz_slug}',
            'intro_text': f'Very <b>cool</b>, {user_uuid}, please fill all these',
            'button_text': 'SUBMIT EVERYTHING',
            'error_message': 'так не пойдёт, заполни всё',
            'questions': [q.json() for q in questions],
        }
    )


def quiz_section_score(request, quiz_slug, user_uuid, section_part):
    next_url = f'/q/{quiz_slug}/{UUID}/{section_part + 1}'
    if section_part >= 3:
        next_url = f'/q/{quiz_slug}/{UUID}/final'
    return JsonResponse({
            'header': f'Your score for {quiz_slug}/{section_part}',
            'text': "<b>Check 'em</b>! Nice job blablabla please proceed. Here's <i>your score</i> btw",
            'score': f'{random.random() * 10:.2f}',
            'postscriptum': "His apprentic killed him in his sleep, that's true.",
            'button_text': 'Listen to other stories',
            'next_url': next_url,
        }
    )


def quiz_section_final(request, quiz_slug, user_uuid):
    scores = [
        {
            'short_name': 'meeting relatives',
            'score': f'{random.random() * 10:.2f}',
        },
        {
            'short_name': 'pink floyd albums',
            'score': f'{random.random() * 10:.2f}',
        },
        {
            'short_name': 'star wars crazy tales',
            'score': f'{random.random() * 10:.2f}',
        },
        {
            'short_name': 'kobo abe poetry',
            'score': f'{random.random() * 10:.2f}',
        },
        {
            'short_name': 'TOOL lyrics',
            'score': f'{random.random() * 10:.2f}',
        },
    ]
    return JsonResponse({
            'header': f'Score for {quiz_slug}',
            'text': "<b>Check 'em</b>! Nice job blablabla please proceed. Here's <i>your score</i> btw",
            'group_scores': scores,
            'postscriptum': "See you in the next one, <i>bro</i>."
        }
    )
