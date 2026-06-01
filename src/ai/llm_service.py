from loguru import logger
from openai import OpenAI

from src.config import AI_KEY


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            base_url='https://openrouter.ai/api/v1',
            api_key=AI_KEY
        )
    
    def get_response_from_llm(self, messages):
        logger.info(f'LLM | {messages}')
        response = self.client.chat.completions.create(
            model='openai/gpt-oss-120b:free',
            messages=messages
        )
        
        return response.choices[0].message.content
        
    def ask_llm(self, user_prompt, system_prompt=None):
        logger.info(f'LLM | ASK LLM | {user_prompt}')
        system_prompt = '''
        You are search engine.
        Give the most accurate answer for asked question, based on provided context
        
        BASE ONLY ON PROVIIDED INFORMATION
        you can rephrase, replace and regrammar context for answer, but dont add addictional meaning
        
        Answer must contain no markdown, no extra (intro, outro) text.
        '''
        
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
        
        return self.get_response_from_llm(messages)


llm_service = LLMService()