# data_analysis 폴더

- 데이터 출처: [Kaggle](https://www.kaggle.com/) | [Seaborn](https://github.com/mwaskom/seaborn-data)
- 각 폴더 앞부분의 숫자는 분석을 진행한 데이터를 순차적으로 표시 
    - e.g. 01_project_1 > 02_project_2
- 폴더 구조
    - `data`: 프로젝트 안에서 사용하는 모든 데이터들이 포함된 폴더
        - `raw`: 다운로드 받은 csv등의 데이터 파일 (변경 x)
        - `processed`: 전처리 작업을 완료한 데이터 파일 (변경 o)
        - `metadata`: data파일의 문서화 및 메타데이터
    
    - `docs`: 작업 진행, 작업 과정, 세부 설명등 프로젝트와 관련된 모든 문서가 포함된 폴더
        - `project_overview.md`: 프로젝트의 목적과 배경등 전반적인 개요를 담고 있는 파일
        - `references.md`: 외부 자료 인용 및 참고 문헌을 정리한 파일
    
    - `notebooks`: 데이터 분석을 위한 jupyter 파일을 담고 있는 폴더
        - `data_overview.ipynb`: 데이터 초기화, 탐색, 전처리

    - `results`: 시각화 자료, 결과를 통한 인사이트 도출등 프로젝트 결과를 전체적으로 포함한 폴더
        - `visualiztions`: 시각화 그래프
            -`individual_sample_results`: 개별적 통계 데이터 분석에 의한 시각화 그래프
            -`overall_result`: 종합 결과
        - `reports`: 데이터 탐색 결과 요약