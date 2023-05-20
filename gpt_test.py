import os
import openai
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--database', '-db', help="사용할 데이터 베이스를 입력하세요", required=True)
parser.add_argument('--question', '-q', help="묻고 싶은 내용을 입력하세요", required = True)
args = parser.parse_args()


API_KEY = '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'
openai.api_key = API_KEY


prompt = '''데이터 : 2024학년도 세종과학예술영재학교 신입생을 다음과 같이 모집합니다.
가. 지원 자격: 중학교 재학생, 졸업자 또는 법령에 의하여 이와 동등 이상의 학력을 갖추고 수학·과학 분야에서 뛰어난 재능과 잠재적 역량이 있으며 인문·예술 융합 소양을 갖춘 자로서 학교장이나 지도교사의 추천을 받은 자
나. 전형 일정 5.29.(월) 09:00 ~ 6.1.(목) 17:00 진학어플라이 접수
1단계(서류 평가) 합격자 발표 6.30.(금) 16:00
2단계(영재성 평가) 전형 7.9.(일) 수학 과학 역량 평가
3단계(창의융합역량 평가) 전형 8.6.(일) 3단계 합격자 발표 8.25.(금) 16:00
최종합격자 발표 2023년 12월 중
  ※ 영재교육진흥법 시행령 제14조 제5항에 의거하여 본교와 초중등교육법에 의거하여 설립된 전기고(과학고 등), 후기고(외고,국제고,자사고,일반고)와 이중지원이 가능함
다. 그 외 자세한 사항은 학교 홈페이지(https://sasa.sjeduhs.kr/)-입학안내 참조
라. 기타 문의: 세종과학예술영재학교입학관리부(044-903-1121~4)
'''

prompt = args.question + prompt

response = openai.Completion.create(
    prompt = prompt, 
    model = 'text-davinci-003', 
    max_tokens=1000,
    temperature=1,
    n=1,
    stop=['---']
)

for result in response.choices:
    print(result.text)