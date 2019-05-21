FROM brianweet/gpt-2-cpu

WORKDIR /gpt-2
ADD src/app.py /gpt-2/src
ADD src/generate_conditional.py /gpt-2/src

ENTRYPOINT ["python3"]
CMD ["src/app.py"]