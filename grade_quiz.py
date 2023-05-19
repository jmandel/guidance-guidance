template = '''
{{#system~}}
You are a helpful and terse assistant that generates quizzes.
{{~/system}}

{{#user~}}
Please grade the following quiz answers.

## Quiz Questions
{{quiz}}

## Answers
{{answers}}

## Scoring Rubric
{{rubric}}

After generating a score, provide helpful and constructive feedback for the student.
{{~/user}}

{{#assistant~}}
{{gen 'report' temperature=.75 max_tokens=300}}
{{~/assistant}}
'''
