import csv
import json
import os
from datetime import datetime

# CSV 파일 메타데이터 추출 함수
def extract_csv_metadata(csv_file_path):
    metadata = {}
    # 파일 이름과 크기
    metadata['file_name'] = os.path.basename(csv_file_path)
    metadata['file_size'] = f"{os.path.getsize(csv_file_path) / 1024:.2f} KB"  # KB 단위로 표시

    # CSV 파일 열기
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # 첫 번째 줄 (헤더)

        # 컬럼 정보를 딕셔너리 형태로 저장
        metadata['columns'] = {}
        for col in header:
            if col.strip():  # 컬럼명이 비어 있지 않은 경우
                metadata['columns'][col.strip()] = "No description provided"  # 기본값 설정

    # 파일 생성 시간 (년-월-일 형식)
    metadata['created_at'] = datetime.fromtimestamp(os.path.getctime(csv_file_path)).strftime('%Y-%m-%d')
    metadata['description'] = 'CSV 파일의 메타데이터'

    return metadata

# 메타데이터를 JSON 파일로 저장
def save_metadata_as_json(metadata, output_json_path):
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(metadata, json_file, indent=4, ensure_ascii=False)

# 실행 예시
csv_file_path = 'example.csv'  # 분석할 CSV 파일 경로
output_json_path = 'metadata.json'  # 저장할 JSON 파일 경로

metadata = extract_csv_metadata(csv_file_path)

# 사용자 입력으로 컬럼 설명 업데이트
print("각 컬럼에 대한 설명을 입력하세요:")
for column_name in metadata['columns']:
    user_description = input(f"'{column_name}' 컬럼에 대한 설명: ").strip()
    if user_description:  # 입력이 있으면 업데이트
        metadata['columns'][column_name] = user_description

# 레코드 수 계산
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # 헤더 건너뛰기
    metadata['row_count'] = sum(1 for row in reader)  # 전체 레코드 수

# source 입력
metadata['source'] = input("파일의 출처(source)를 입력하세요: ").strip()

# 메타데이터 JSON 저장
save_metadata_as_json(metadata, output_json_path)

print(f"Metadata JSON 파일이 생성되었습니다: {output_json_path}")