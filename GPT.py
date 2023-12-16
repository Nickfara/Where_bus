import g4f
import asyncio
from fp.fp import FreeProxy
proxy = FreeProxy().get()

_providers = [
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
    g4f.Provider.GeekGpt,
    g4f.Provider.Hashnode,
    g4f.Provider.GptForLove,
    g4f.Provider.GPTalk

]

def send(text):
    async def run_provider(provider: g4f.Provider.BaseProvider, messages: list):
        try:
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                messages=messages,
                provider=provider
            )
            return response
        except:
            pass

    async def run_all(messages):
        calls = [
            run_provider(provider=provider, messages=messages) for provider in _providers
        ]
        response = await asyncio.gather(*calls)
        return response


    returner = None
    response = asyncio.run(run_all(text))
    for i in response:
        if i != None:
            returner = i
            break
        else:
            returner = i
    return returner

messages = []

def GPT(message: str):
    messages.append({"role": "user", "content": message})
    while True:
        answer = send(messages)
        if answer != None:
            break
    print('GPT: ' + str(answer))
    messages.append({"role": "user", "content": answer})