# How to run

We used "llama3-8b-8192" through Groq API. 

To run the project, configure your API key in the following environment variable. 
```commandline
$ export GROQ_API_KEY="{YOUR API KEY}"
```


```commandline
$ python3 -m streamlit run app.py
```


# How to build

We use pipenv to manage dependencies.

To install all dependencies based on Pipfile.lock
(This might update Pipfile.lock if it's not consistent with Pipfile):
```commandline
pipenv install
```

To add a new dependency:
```commandline
pipenv install <package_name>  
```

To force update dependencies:
```commandline
pipenv update
```