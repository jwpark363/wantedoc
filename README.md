# LLM + RAG + LangGraph 를 이용한 문서 사전 검토 에이전트
- 문서의 양식에 맞게 작성 되었는지를 검토하는 AI 에이전트
- 구조
    1. 문서별 검토 기준서 RAG Vector 구성
    2. 문서 제목을 통한 문서 구분
    3. 문서 구분에 따른 검토 기준 정보 로드
    4. 기준 정보 기준 문서 검토
    5. 검토 결과 리포트 작성
    6. 최종 통보

### 전체 구조
- 노드 5개
- 조건 노드 1개
- RAG Vector DB : PostgreSQL + PgVector
<img src='https://raw.githubusercontent.com/jwpark363/wantedoc/refs/heads/main/graph.png' height=480>

### 파일 구성
- 검토 기준서 : txt
- 기준 문서 : docx


### 기능
- 검토 대상 문서(docx) 패스 전달
- 문서 제목을 파악하여 RAG로 부터 해당 검토 기준서 로드
- 문서 pdf 파일로 변환
- pdf 문서 텍스트 추출
- 기준서 기준 문서 검토
- 검토 결과 리포트 생성
- 리포트 제출


### 기준서 샘플, 처리 결과 샘플
- 1 검토 기준서 샘플
<img src='https://raw.githubusercontent.com/jwpark363/wantedoc/refs/heads/main/document_rule.png' height=240>

- 2 에이전트 처리 결과 샘플
<img src='https://raw.githubusercontent.com/jwpark363/wantedoc/refs/heads/main/agent_result.png' height=400>