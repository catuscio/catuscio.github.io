import os
import json
from datetime import datetime
from notion_client import Client
import requests
from pathlib import Path
import re
import yaml

class NotionToJekyll:
    def __init__(self, notion_token, database_id):
        self.notion = Client(auth=notion_token)
        self.database_id = database_id
        self.image_dir = Path("assets/images")
        self.posts_dir = Path("_posts")
        
        # 디렉토리 생성
        self.image_dir.mkdir(parents=True, exist_ok=True)
        self.posts_dir.mkdir(parents=True, exist_ok=True)

    def download_image(self, url, filename):
        """이미지 다운로드 및 저장"""
        response = requests.get(url)
        if response.status_code == 200:
            image_path = self.image_dir / filename
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return f"/assets/images/{filename}"
        return None

    def convert_block_to_markdown(self, block):
        """노션 블록을 마크다운으로 변환"""
        block_type = block["type"]
        text = ""
        
        if block_type == "paragraph":
            text = self.convert_rich_text(block["paragraph"]["rich_text"])
        elif block_type == "heading_1":
            text = f"# {self.convert_rich_text(block['heading_1']['rich_text'])}\n"
        elif block_type == "heading_2":
            text = f"## {self.convert_rich_text(block['heading_2']['rich_text'])}\n"
        elif block_type == "heading_3":
            text = f"### {self.convert_rich_text(block['heading_3']['rich_text'])}\n"
        elif block_type == "bulleted_list_item":
            text = f"- {self.convert_rich_text(block['bulleted_list_item']['rich_text'])}\n"
        elif block_type == "numbered_list_item":
            text = f"1. {self.convert_rich_text(block['numbered_list_item']['rich_text'])}\n"
        elif block_type == "code":
            language = block["code"]["language"]
            code = self.convert_rich_text(block["code"]["rich_text"])
            text = f"```{language}\n{code}\n```\n"
        elif block_type == "equation":
            text = f"\\[{block['equation']['expression']}\\]\n"
        elif block_type == "image":
            if block["image"]["type"] == "external":
                url = block["image"]["external"]["url"]
            else:
                url = block["image"]["file"]["url"]
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            image_path = self.download_image(url, filename)
            if image_path:
                text = f"![image]({image_path})\n"

        return text

    def convert_rich_text(self, rich_text):
        """리치 텍스트를 마크다운으로 변환"""
        text = ""
        for rt in rich_text:
            content = rt["plain_text"]
            if rt.get("annotations"):
                if rt["annotations"]["bold"]:
                    content = f"**{content}**"
                if rt["annotations"]["italic"]:
                    content = f"*{content}*"
                if rt["annotations"]["code"]:
                    content = f"`{content}`"
            text += content
        return text

    def create_front_matter(self, page):
        """Front matter 생성"""
        properties = page["properties"]
        front_matter = {
            "title": properties["title"]["title"][0]["plain_text"],
            "date": datetime.now().strftime("%Y-%m-%d"),
            "categories": ["개발"],  # 기본 카테고리
            "tags": [],
            "toc": True
        }
        
        # 태그와 카테고리 처리
        if "Tags" in properties:
            front_matter["tags"] = [tag["name"] for tag in properties["Tags"]["multi_select"]]
        if "Category" in properties:
            if properties["Category"]["select"]:
                front_matter["categories"].append(properties["Category"]["select"]["name"])

        return yaml.dump(front_matter, allow_unicode=True)

    def convert_page(self, page_id):
        """노션 페이지를 Jekyll 포스트로 변환"""
        # 페이지 정보 가져오기
        page = self.notion.pages.retrieve(page_id)
        
        # 블록 내용 가져오기
        blocks = self.notion.blocks.children.list(page_id)
        
        # Front matter 생성
        content = f"---\n{self.create_front_matter(page)}---\n\n"
        
        # 블록 변환
        for block in blocks["results"]:
            content += self.convert_block_to_markdown(block)
        
        # 파일명 생성
        title_slug = re.sub(r'[^a-z0-9]+', '-', 
                           page["properties"]["title"]["title"][0]["plain_text"].lower())
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{title_slug}.md"
        
        # 파일 저장
        with open(self.posts_dir / filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filename

def main():
    # 환경 변수에서 토큰과 데이터베이스 ID 가져오기
    notion_token = "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"
    
    if not notion_token or not database_id:
        print("Error: NOTION_TOKEN and NOTION_DATABASE_ID environment variables are required")
        return
    
    converter = NotionToJekyll(notion_token, database_id)
    
    # 특정 페이지 변환
    page_id = "ab1a4083dd9e4084b6f389b0c526486d"  # 변환하고 싶은 페이지 ID
    filename = converter.convert_page(page_id)
    print(f"Created post: {filename}")

if __name__ == "__main__":
    main()