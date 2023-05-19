# Guidance for Quiz Generation

An example repo showing how to use https://github.com/microsoft/guidance with Jupyter notebooks for generating content programatically.

## Local setup
```
docker build -t quizzes .
docker run -e OPENAI_API_KEY="KEY_HERE" -p 8888:8888 -v "$(pwd):/app" quizzes
```

## Using normal python code

[Quiz and Answers](./Quiz%20and%20Answers.ipynb)

## Playing with form widgets
In [Quiz with Form WIP](./main/Quiz%20with%20Form%20WIP.ipynb)
![image](https://github.com/jmandel/guidance-guidance/assets/313089/fbcbf8f5-1f91-4e21-a997-568dada4e9e7)
^^ Rendering inputs as forms is a hack right now. Probably better just to play with normal python code
