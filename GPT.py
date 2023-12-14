import g4f
import asyncio

_providers = [
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
    g4f.Provider.GeekGpt
]
responce = ['']
def GPT(text):
    async def run_provider(provider: g4f.Provider.BaseProvider):
        try:
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                messages=[{"role": "user", "content": text}],
                provider=provider,
            )
            responce[0] = response
            print(f"{provider.__name__}:", response)
        except Exception as e:
            responce[0] = e
            print(f"{provider.__name__}:", e)

    async def run_all(text):
        calls = [
            run_provider(provider) for provider in _providers
        ]
        await asyncio.gather(*calls)

    asyncio.run(run_all(text))
    return responce[0]

shablon = {'1':'вопрос о трамвае', '2':'любая цифра от 1 до 24', '3':'что-то другое'}
GPT('Есть тут спрашивается о трамвае: Где трамвай. То ответь 1')