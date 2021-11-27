# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # 2021 NLP & AI Coding Test
#
# ![](https://item.kakaocdn.net/do/8ad594ffa619c5063075206d55ec79a18f324a0b9c48f77dbce3a43bd11ce785)
#
# - 안녕하세요! 2021 NLP & AI 연구실의 코딩 테스트에 오신 여러분 환영합니다. 👨
# - 본 테스트는 파이썬(python)🐍 언어를 이용하여 다양한 프로그래밍 상황에서의 간단한 퀴즈를 통해 여러분들에게 필요한 핵심 역량을 파악하는 것을 목적으로 합니다.
# - 여러분들은 이미 인턴으로 NLP & AI 연구실의 인원으로 합류하셨으며 👏, 그 능력의 출중함은 이미 평가되었다 생각합니다. 그러므로 무리하게 정답을 맞추는 것은 본 테스트의 목적은 아니므로 부담 없이 뇌 운동한다 생각하고 참여해주시면 됩니다. 🏝️

# %%
# 실행해주세요!
get_ipython().system('git clone https://github.com/taeminlee/cote_vol_1')

# %% [markdown]
# # 세션 1 : 파이썬 아일랜드
#
# ![](https://images-na.ssl-images-amazon.com/images/S/pv-target-images/7548d4378a9ebcc60173995446a08014b114efc66e4713a4f292205981a5cf62._RI_V_TTW_.jpg)
# %% [markdown]
# ### Q1 : KorQuAD 데이터 집합에서 `question` 키의 값만 가지는 리스트를 만들고자 한다. 이를 한줄의 파이썬 코드로 작성하시오.
#
# - KorQuAD 데이터 집합의 스키마는 다음과 같음
#
# ```
# {
#   "version": string
#   "data" : [
#     "paragraphs" : [
#       "qas" : [
#         "question" : string,
#         "id" : string,
#         "answers" : [
#           "text" : string,
#           "answer_start" integer
#         ]
#     ]
#   ]
# }
# ```

# %%
from cote_vol_1.q1 import Q1
import pprint

q1_dataset = Q1.load_dataset()


# %%
# answer = [list(map(lambda y: y['question'], qa)) for qa in map(lambda x: x['qas'], data['paragraphs']) for data in q1_dataset['data']]
answer = []
for data in q1_dataset['data']:
    for qa in map(lambda x: x['qas'], data['paragraphs']):
        answer.append(list(map(lambda y: y['question'], qa)))


# %%
from itertools import chain
answer = list(chain.from_iterable([list(chain(map(lambda t: t['question'], k))) for k in (map(lambda y: y['qas'] ,paragraph)) for paragraph in map(lambda x: x['paragraphs'] ,q1_dataset['data'])]))

len(answer)


# %%
# questions = # 여기에 코드를 작성하세요

questions = list(chain.from_iterable(answer))

get_ipython().run_line_magic('time', 'Q1.validate(questions)')

# %% [markdown]
# ### Q2 : $n$ 사이즈의 리스트의 각각의 원소 $e$를 검사하여 짝수인 경우 $e^2$ 값으로, 홀수인 경우 $\sqrt{e}$로 변환하는 이터레이터(iterator)를 작성하시오.

# %%
from cote_vol_1.q2 import Q2
import math

q2_dataset = Q2.load_dataset()
print("데이터 집합의 크기 :", len(q2_dataset))


# %%
class Iterator:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.length = len(dataset)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.length:
            raise StopIteration
        if self.dataset[self.current] % 2 == 0:
            num = math.pow(self.dataset[self.current] , 2)
            self.current += 1
            return num
        else:
            num = math.sqrt(float(self.dataset[self.current] ))
            self.current += 1
            return num


# %%
iterator = Iterator(q2_dataset)
get_ipython().run_line_magic('time', 'Q2.validate(iterator)')

# %% [markdown]
# ### Q3 : 구분 문자로 분절하는 SimpleTokenizer를 상속받아 다음의 tokenizer들을 구현하시오.
#
# - uni-gram tokenizer
#   - 예 : `신인 샹송 가수의 신춘 샹송 쇼` -> [`신인`, `샹송`, `가수의`, `신춘`, `샹송`, `쇼`]
# - bi-gram tokenizer with stride 1
#   - 예 : `신인 샹송 가수의 신춘 샹송 쇼` -> [`신인 샹송`, `샹송 가수의`, `가수의 신춘`, `신춘 샹송`, `샹송 쇼`]
# - tri-gram tokenizer with stride 2
#   - 예 : `신인 샹송 가수의 신춘 샹송 쇼` -> [`신인 샹송 가수의`, `가수의 신춘 샹송`, `샹송 쇼`]

# %%
test = '신인 샹송 가수의 신춘 샹송 쇼'

test = test.split(' ')
count = len(test)

test
[" ".join(test[i:i+2]) for i in range(0, count-1,1)]


# %%
from cote_vol_1.q3 import Q3
from typing import List

class SimpleTokenizer:
  def __init__(self, delimiter=' '):
    self.delimiter = delimiter
  def tokenize(self, sentence: str) -> List[str]:
    raise NotImplementedError
  def detokenize(self, tokens: List[str]) -> str:
    raise NotImplementedError


# %%
q3_dataset = Q3.load_dataset()


# %%
import itertools

class Tokenizer(SimpleTokenizer):
    def __init__(self, n) -> None:
        super().__init__()
        self.n = n
        if n == 1:
            self.stride = 0
        elif n == 2:
            self.stride = 1
        else:
            self.stride = 2

    def tokenize(self, sentence: str) -> List[str]:
        sentence = sentence.split(self.delimiter)
        count = len(sentence)
        if self.stride == 0:
            return sentence
        elif self.stride == 1:
            if count == 1:
                return sentence
            else:
                return [" ".join(sentence[i:i+2]) for i in range(0, count-1,1)]
        else:
            return [" ".join(sentence[i:i+self.stride+1]) for i in range(0, count,self.stride)]

    def detokenize(self, tokens: List[str]) -> str:
        result = []
        for token in tokens:
            if len(token.split(self.delimiter)) == 1:
                result.append([token])
                continue
            result.append(token.split(self.delimiter)[:-1])

        try:
            result.append(token.split(self.delimiter)[1:])
        except:
            print(tokens)

        return " ".join(chain.from_iterable(result))



# %%
test = '신인'
tk = Tokenizer(2)
(tk.tokenize(test))


# %%
unigram_tokenizer = Tokenizer(1)
bigram_tokenizer = Tokenizer(2)
trigram_tokenizer = Tokenizer(3)
get_ipython().run_line_magic('time', 'Q3.validate(unigram_tokenizer)')
get_ipython().run_line_magic('time', 'Q3.validate(bigram_tokenizer)')
get_ipython().run_line_magic('time', 'Q3.validate(trigram_tokenizer)')

# %% [markdown]
# # 세션 2 : 넘파이 정글
#
# ![](https://creativemazes.com.au/wp-content/uploads/2019/04/CreativeMazes_Mandurah_HighRes-6.jpg)
# %% [markdown]
# ### Q4 : Numpy를 이용하여 linear regression을 구현하시오.
#
# - input : $x_{i} \in \mathbb{R}$
# - output : $y_{i} \in \mathbb{R}$
# - error function : MSE
# - learning algorithm : gradient descent

# %%
import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,2,4,3,5])
Y = np.array([1,3,3,2,5])

print("X:", X)
print("Y:", Y)

plt.scatter(X, Y)


# %%
class LinearModel:
  def __init__(self):
    self.W = 1.
    self.b = 0.
    self.lr = 0.001
  def forward(self, X: np.array) -> (np.array, np.array):
    self.X = X
    y_hat = self.W*self.X + self.b
    return y_hat, np.square(np.subtract(y_hat, Y)).mean()

  def backward(self, loss: np.array):
    self.W = self.W - loss * self.lr
    self.b = self.b - loss * self.lr



epochs = 10000
model = LinearModel()
for _ in range(epochs):
  y_hat, loss = model.forward(X)
  model.backward(loss)
print(y_hat)

# %% [markdown]
# ### Q5 : Numpy를 이용하여 Convolution 2d 연산을 구현하시오.
#
# - kernel size : 3
# - stride : 1
# - padding : 1
# - bias는 사용하지 않음
#
# ![](https://cdn-images-1.medium.com/max/1200/1*1okwhewf5KCtIPaFib4XaA.gif)

# %%
from cote_vol_1.q5 import Q5

x, w = Q5.load_dataset()


# %%
y = # conv2d 연산 결과를 자유롭게 작성하세요
Q5.validate(y)

# %% [markdown]
# # 세션3 : 퀴즈 타임
#
# ![](https://blog.hubspot.com/hubfs/google-quiz.jpg)
# %% [markdown]
# ### Q6 : 주어진 리스트의 단어 각각에 `은`/`는` 조사를 적절히 붙여주는 함수를 작성하시오.
#
# - Tip : 종성 유무에 따라 적절한 조사가 정해집니다. 예를 들어, 종성이 있으면 `은` 종성이 없으면 `는`이 붙어야 합니다. `애플은` | `사과는`

# %%
from cote_vol_1.q6 import Q6

dataset = Q6.load_dataset()


# %%
josa_append_dataset = # 자유롭게 조사가 붙은 데이터셋을 만들어보세요!
Q6.validate(josa_append_dataset)

# %% [markdown]
# ### Q7 : 토큰화된 문장의 일부를 마스킹 처리하여 언어 모형을 학습하고자 합니다. 토큰화된 리스트가 주어졌을 때, 다음의 규칙을 준수하는 마스킹 된 데이터 집합을 만들어 보세요!
#
# - 마스킹 토큰은 `<mask>` 으로 표현합니다.
# - 마스킹 토큰의 id는 6번 입니다.
#
# > The training data generator chooses 15% of the token positions at random for
# prediction. If the i-th token is chosen, we replace the i-th token with (1) the [MASK] token 80% of the time (2) a random token 10% of the time (3) the unchanged i-th token 10% of the time.

# %%
get_ipython().system('pip install datasets')
get_ipython().system('pip install transformers')


# %%
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2")


# %%
from datasets import load_dataset
dataset = load_dataset('kor_ner')
texts = [record['text'] for record in dataset['train']]


# %%
# 토큰화 리스트
tokens = [tokenizer.tokenize(text) for text in texts]
# 토큰 ID화 리스트
token_ids = [tokenizer.encode(text) for text in texts]


# %%
print("토큰:", tokens[0][:10],"...")
print("ID:", token_ids[0][:10],"...")


# %%
# 자유롭게 마스킹된 토큰 리스트 (혹은 토큰 ID 리스트) 을 만들어보세요!

# %% [markdown]
# # 마무리
#
# ![](https://item.kakaocdn.net/do/0936dbb0aaa6270bd577ad286a1525aa8b566dca82634c93f811198148a26065)
#
# 고생이 많으셨습니다!
#
# 마지막으로, colab 에서 저장 후 `파일` -> `다운로드` 하여 ipynb 파일을 카톡방이나, taeminlee@korea.ac.kr 으로 전송해주세요 😊
#
# 그럼 다음에 또 봐요~~

