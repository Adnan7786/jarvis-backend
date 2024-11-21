# J.A.R.V.I.S Fastapi Backend

## Prerequisites

### Download and install Git
- **Windows** - Go to https://git-scm.com/downloads/win
- **MacOs** - Run```git --version``` and instal xcode installation prompt
- **Linux** - Run```sudo apt install git-all
``` or```sudo dnf install git-all```


### Download and install Python
- Go to https://www.python.org/downloads/

### Download and install ollama application
- Go to https://ollama.com/ and click on Download
- You can also choose model at https://ollama.com/search


### Pull models from ollama CLI
- Go to terminal or powershell and run ```ollama pull qwen2.5-coder:3b```
- You can also run the model directly in command line. Go to terminal or powershell and run ```ollama run qwen2.5-coder:3b```


## Steps to follow:

### Clone github repo
- Go to terminal or powershell and run ```git clone https://github.com/Adnan7786/jarvis-backend.git```

### Change directory
- Go to terminal or powershell and run ```cd jarvis-backend```

### Create virtual environment
- Go to terminal or powershell and run ```python3 -m venv .venv```

### Activate virtual environment
- Go to powershell and run ```.venv\Scripts\activate``` or go to terminal and run ```. .venv/bin/activate```

### Install dependencies
- Go to terminal or powershell and run ```pip install -r requirements.txt```

### Run fastapi application
- Go to terminal or powershell and run ```fastapi run main.py --reload```

### Check api swagger
Go to http://127.0.0.1:8000/docs
