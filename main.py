from loguru import logger

from src.data import TEXT_TO_CHUNK
from src.llm_service import llm_service

from src.eval import eval_text, questions
from src.models import Index


# def main():
#     logger.info('MAIN | start')
    
#     vectors = Index(text=TEXT_TO_CHUNK)
    
#     logger.info(vectors)
    
#     query = 'Who invented transformers?'
    
#     chunks = vectors.search(query)
    
#     user_prompt = f'Context: {chunks}. \n Question: {query}'
    
#     logger.success(llm_service.ask_llm(user_prompt))    
    
#     logger.info('MAIN | end')
    
# def eval():
#     vs = VectorStorage(text=eval_text)
    
    
#     hr = 0
#     for question in questions:
#         correct_index = question[1]
#         if correct_index == -1:
#             continue
#         retrieval = vs.search(question[0])

#         if vs.chunks[correct_index] in [v.text for v in retrieval]:
#             hr += 1
#     # print(hr)
        

def main():
    
    vs = Index(text=eval_text)
    
    print(vs.cossim_search('What was the name of the first artificial satellite?'))
    print(vs.bm25_search('What was the name of the first artificial satellite?'))
    
    print(vs.hybrid_search('What was the name of the first artificial satellite?'))

if __name__ == '__main__':
    # bm25_test()
    main()