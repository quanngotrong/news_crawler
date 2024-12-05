Requirements:
- Save html in S3
- Deploy in EC2
- Queue ?
- Crawl all questions and answer

Home page: https://oshiete.goo.ne.jp/
Question page:

DynamoDB schema
- content
    -

- page
    - id: from url
        - type: string
    - author_id
        - type: string
    - timestamp:
        - type: number
    - response_number:
        - type: number
    - category_id:
        - type: string
    - title:
        - type: string
    - questions:
        - type: question[]


