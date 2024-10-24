from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

PROMPT_TEMPLATE = """
You are a helpful assistant that help the user in different things that he needs
Your responses should be in Spanish.
You can't speak English.
you can't response with bad grammar and spelling mistakes.
you can't response with swear words.
you can't response with profanity.
you can't response with racism.
you can't response with sexism.
you can't response with hate speech.
you can't response with anything that is not related to the topic.
you have to response like a string no use json.
{messages}
"""


llm = ChatOllama(
    model="gemma2:latest",
    temperature= 0.5,
    num_predict=-2,
    )

def conversation(messages: list):
    try:
        messages = transform_messages(messages)
        prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["messages"])
        response = llm.invoke(prompt.format(messages=messages))
        print("response", response)
        return response.content
    except Exception as e:
        print(e)

def transform_messages(messages: list):
    for message in messages:
        message = (message["role"], message["content"])
    print("msgs", messages)
    return messages