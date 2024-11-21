from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yaml
from langchain_ollama import OllamaLLM

origins = [
    "http://localhost",
    "http://localhost:3000",
]

prompt_template = """
Answer the following question: {question}.
Wrap the response in appropriate tags starting with p tag. Use ordered lists if needed. Put code elements inside code tag.
Use inline css for proper styling. Put code in black background with color coded text.
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserInput(BaseModel):
    text: str

def query_prompt(prompt: str) -> str:
    model = OllamaLLM(model="qwen2.5-coder:3b")
    response_text = model.invoke(prompt)
    return response_text


@app.post("/generate_response")
async def generate_response(input: UserInput):
    try:
        # Load YAML data for retrieval
        # with open("knowledge.yaml", "r") as file:
        #     data = yaml.safe_load(file)

        # Initialize LangChain components and RAG retrieval
        # retriever = YAMLRetriever(yaml_data=data)
        # chain = LanguageChain(retriever=retriever)

        # Generate response
        prompt = prompt_template.format(question=input.text)
        response_text, actions = [query_prompt(prompt), ["Summarize", "Restructure"]]

        return {
            "response": response_text,
            "actions": actions
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
