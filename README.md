# Guidance for Quiz Generation

An example repo showing how to use https://github.com/microsoft/guidance with Jupyter notebooks for generating content programatically.

## Local setup
```
docker build -t quizzes .
docker run -e OPENAI_API_KEY="KEY_HERE" -p 8888:8888 -v "$(pwd):/app" quizzes
```

## Using normal python code

[Quiz and Answers](./Quiz%20and%20Answers.ipynb)

## Using `await` inputs to define entire flow in a single prompt
[Quiz and Answers All In One](./Quiz%20and%20Answers%20All%20In%20One.ipynb)

See the [pausing execution with await](https://github.com/microsoft/guidance#pausing-execution-with-await) section of the Guidance docs for more info on this approach.

## Playing with form widgets
In [Quiz with Form WIP](./Quiz%20with%20Form%20WIP.ipynb)
![image](https://github.com/jmandel/guidance-guidance/assets/313089/fbcbf8f5-1f91-4e21-a997-568dada4e9e7)
^^ Rendering inputs as forms is a hack right now. Probably better just to play with normal python code
