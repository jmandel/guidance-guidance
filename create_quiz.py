template = '''
{{#system~}}
You are a helpful and terse assistant that generates quizzes. You produce only outputs, no banter.
{{~/system}}

{{#user~}}
I want to create a quiz on the following topic:
{{topic}}
List {{num_learning_objectives}} potential learning objectives.
{{~/user}}

{{#assistant~}}
{{gen 'learning_objectives' temperature=.75 max_tokens=300}}
{{~/assistant}}

{{#user~}}
Great, now please provide a bullet list of {{num_questions}} short-answer questions for the quiz.
Questions should be aligned with learning objectives.
Do not write the answers yet.
{{~/user}}

{{#assistant~}}
{{gen 'questions' temperature=0 max_tokens=100}}
{{~/assistant}}

{{#user~}}
Finally, output a numbered list of grading rubrics describing how to award points
(hitting all requirements will award {{points_per_question}} points per question).
Rubrics should help a non-expert grade assign grades.
Rubrics must fit on a single line (no newlines within the rubric).
{{~/user}}

{{#assistant~}}
{{gen 'rubric' temperature=0 max_tokens=1000}}
{{~/assistant}}
'''
