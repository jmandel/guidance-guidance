# Guidance for Quiz Generation

An example repo showing how to use https://github.com/microsoft/guidance with Jupyter notebooks for generating content programatically.

```
docker build -t quizzes .
docker run -e OPENAI_API_KEY="KEY_HERE" -p 8888:8888 -v "$(pwd):/app" quizzes
```
