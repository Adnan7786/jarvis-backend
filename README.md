# J.A.R.V.I.S Fastapi Backend

## Prerequisites

### Download and install ollama application
Go to https://ollama.com/ and click on Download
You can look for required models at https://ollama.com/search


### Pull models from ollama CLI
Go to terminal and run below command
```bash
ollama pull qwen2.5-coder:3b
```
You can also run the model directly in CLI using below command
```bash
ollama run qwen2.5-coder:3b
```


## Steps to follow:

### Clone github repo
```bash
git clone https://github.com/Adnan7786/jarvis-backend.git
```

### Create virtual environment
```python
python -m venv .venv
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run fastapi application
```bash
fastapi run main.py --reload
```

### Check api swagger
Go to http://127.0.0.1:8000/docs
