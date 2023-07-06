import openai
import pandas as pd
import sys
import numpy as np
import random

API_BASE_URL = "http://8.219.254.96:9000/v1"
API_KEY = "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"
openai.api_base = API_BASE_URL
openai.api_key = API_KEY
MODEL_CHAT = 'gpt-3.5-turbo'
MODEL_DAVINCI = 'text-davinci-003'

def query_gpt(messages):
    completions = openai.ChatCompletion.create(
        model=MODEL_CHAT,
        messages=messages,
        temperature=0,
    )
    response_text = completions.choices[0]['message']['content']

    return response_text
        
def make_sample(doc, answers=None):
    
    formatted_answers = []
    
    if answers is not None:
        for answer in answers:
            index = label_to_index[answer]
            answer_str = '{}. {}'.format(index, answer)
            formatted_answers.append(answer_str)
    
        sample = [
            '裁判文书：', doc,
            '争议焦点：', ' '.join(formatted_answers),
        ]
    else:
        sample = [
            '裁判文书：', doc,
            '争议焦点：',
        ]
        
    return sample
    
    
def get_total_labels(label_path):
    labels = np.array(pd.read_csv(label_path, sep='\t', header=None)[0])
    label_to_index = {}
    for index, label in enumerate(labels):
        label_to_index[label] = index
    return labels, label_to_index
        
    
def generate_label_candidates(labels:list) -> str:
    formatted_candidates = ['{}. {}'.format(index, label) for index, label in enumerate(labels)]
    formatted_candidates_str = '\n'.join(formatted_candidates)
    return formatted_candidates_str


def generate_contexts(context_ids, docs, ans, labels) -> str:
    contexts = []
    for id in context_ids:
        context = '\n'.join(make_sample(docs[id], labels[ans[id]]))
        contexts.append(context)
    contexts_str = '\n'.join(contexts)
    return contexts_str


train_set_path = "../judge/data/raw_json/train_reduce.json"
valid_set_path = "../judge/data/raw_json/valid_reduce.json"
label_path = '../judge/data/label_index.txt'

train_set = pd.read_json(train_set_path)
train_doc = list(train_set['text'])
train_ans = list(train_set['labels_index'])

valid_set = pd.read_json(valid_set_path)
valid_doc = list(valid_set['text'])
valid_ans = list(valid_set['labels_index'])

labels, label_to_index = get_total_labels(label_path)


def global_candidate():
    contexts_ids = [2]
    contexts_str = generate_contexts(contexts_ids, train_doc, train_ans, labels)
    
    task_description = '这段裁判文书的争议焦点是什么？从如下选项中选择：'
    candidates_str = generate_label_candidates(labels)
    for i in [109, 112, 123, 1, 3, 4, 5, 6, 40, 10]:
        doc, answer_ids = valid_doc[i], valid_ans[i]
        query = make_sample(doc)
        query_str = '\n'.join(query)
        
        # prompt_text = '\n'.join([task_description, candidates_str, query_str])
        prompt_text = '\n'.join([task_description, candidates_str, contexts_str, query_str])
        
        # print(prompt_text)
        
        messages = [
            {'role': 'system', 'content': '你是一个值得信赖的法官'},
            {'role': 'user', 'content': prompt_text},
        ]
        
        response = query_gpt(messages=messages)
        print(response)   
        
        print('ans:')
        for answer_id in answer_ids:
            print(answer_id, labels[answer_id])        
        print()

def partial_candidate():
    contexts_ids = [2]
    contexts_str = generate_contexts(contexts_ids, train_doc, train_ans, labels)
    
    question_str = '这段裁判文书的争议焦点是什么？从如下选项中选择不超过三个选项：'
    for i in range(1, 1000, 50):
        doc, answer_ids = valid_doc[i], valid_ans[i]
        query = make_sample(doc)
        query_str = '\n'.join(query)
        
        # prompt_text = '\n'.join([task_description, candidates_str, query_str])
        candidates = answer_ids + random.sample(range(1, 147), 10) + train_ans[contexts_ids[0]]
        candidates = list(set(candidates))
        candidates_str = ''
        for candidate in candidates:
            candidates_str += '{}. {}\n'.format(candidate, labels[candidate])
            
        prompt_text = [
            question_str, 
        ]
        
        # prompt_text = '\n'.join([question_str, candidates_str, query_str])
        
        prompt_text = '\n'.join([question_str, candidates_str, contexts_str, query_str])
        
        print(prompt_text)
        
        messages = [
            {'role': 'system', 'content': '你是一个值得信赖的法官'},
            {'role': 'user', 'content': prompt_text},
        ]
        
        response = query_gpt(messages=messages)
        print(response)   
        
        print('正确答案:')
        for answer_id in answer_ids:
            print(answer_id, labels[answer_id])        
        print('=====================================================\n')

    
if __name__ == '__main__':
    partial_candidate()



# completions = openai.Completion.create(
#         engine=MODEL_DAVINCI,
#         prompt=prompt,            
#         temperature=0,
#         max_tokens=100,
#     )    

# response_text = completions.choices[0].text.strip()
