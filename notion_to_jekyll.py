import os
from datetime import datetime
from notion_client import Client
import requests
from pathlib import Path
import re
import yaml

class NotionToJekyll:
    def __init__(self, notion_token):
        self.notion = Client(auth=notion_token)
        self.image_dir = Path("assets/images")
        self.posts_dir = Path("_posts")
        
        # 디렉토리 생성
        self.image_dir.mkdir(parents=True, exist_ok=True)
        self.posts_dir.mkdir(parents=True, exist_ok=True)

    def download_image(self, url, page_title):
        """이미지 다운로드 및 저장"""
        # 포스트 제목으로 단일 폴더명을 생성
        folder_name = page_title.replace(" ", "_").lower()
        image_folder = self.image_dir / folder_name
        image_folder.mkdir(parents=True, exist_ok=True)

        # 이미지 파일명 생성
        filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image_path = image_folder / filename

        response = requests.get(url)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return f"/assets/images/{folder_name}/{filename}"
        return None

    def convert_block_to_markdown(self, block):
        """노션 블록을 마크다운으로 변환"""
        block_type = block["type"]
        text = ""
    
        try:
            if block_type == "paragraph":
                content = self.convert_rich_text(block["paragraph"]["rich_text"])
                text = f"{content}\n\n" if content else "\n"
    
            elif block_type == "heading_1":
                text = f"# {self.convert_rich_text(block['heading_1']['rich_text'])}\n\n"
    
            elif block_type == "heading_2":
                text = f"## {self.convert_rich_text(block['heading_2']['rich_text'])}\n\n"
    
            elif block_type == "heading_3":
                text = f"### {self.convert_rich_text(block['heading_3']['rich_text'])}\n\n"
    
            elif block_type == "bulleted_list_item":
                indent = "    " * block.get("indent", 0)
                content = self.convert_rich_text(block['bulleted_list_item']['rich_text'])
                text = f"{indent}- {content}\n"
                
                # 중첩된 리스트 처리
                if "has_children" in block and block["has_children"]:
                    children = self.notion.blocks.children.list(block["id"])
                    for child in children["results"]:
                        text += self.convert_block_to_markdown(child)
    
            elif block_type == "numbered_list_item":
                indent = "    " * block.get("indent", 0)
                content = self.convert_rich_text(block['numbered_list_item']['rich_text'])
                text = f"{indent}1. {content}\n"
                
                # 중첩된 리스트 처리
                if "has_children" in block and block["has_children"]:
                    children = self.notion.blocks.children.list(block["id"])
                    for child in children["results"]:
                        text += self.convert_block_to_markdown(child)
    
            elif block_type == "code":
                language = block["code"]["language"]
                code = self.convert_rich_text(block["code"]["rich_text"])
                text = f"```{language}\n{code}\n```\n\n"
    
            elif block_type == "equation":
                expr = block['equation']['expression'].replace('\\', '\\\\')
                text = f"\\[{expr}\\]\n\n"
    
            elif block_type == "quote":
                text = f"> {self.convert_rich_text(block['quote']['rich_text'])}\n\n"
    
            elif block_type == "callout":
                emoji = block["callout"].get("icon", {}).get("emoji", "💡")
                callout_text = self.convert_rich_text(block["callout"]["rich_text"])
                text = f"<div class='notice--info' markdown='1'>\n{emoji} {callout_text}\n</div>\n\n"
    
            elif block_type == "image":
                if block["image"]["type"] == "external":
                    url = block["image"]["external"]["url"]
                else:
                    url = block["image"]["file"]["url"]
    
                caption = ""
                if "caption" in block["image"] and block["image"]["caption"]:
                    caption = self.convert_rich_text(block["image"]["caption"])
    
                image_path = self.download_image(url, self.current_page_title)
                if image_path:
                    text = f"![{caption}]({image_path})\n\n"
    
            else:
                print(f"Unhandled block type: {block_type}")
                text = "\n"
    
        except Exception as e:
            print(f"Error processing block type {block_type}: {str(e)}")
            text = "\n"
    
        return text

    def convert_rich_text(self, rich_text):
        """리치 텍스트를 마크다운으로 변환"""
        if not rich_text:
            return ""

        text = ""
        for rt in rich_text:
            content = rt["plain_text"]
            annotations = rt.get("annotations", {})

            # 수식 처리
            if rt.get("type") == "equation":
                content = f"${content}$"
            else:
                if annotations.get("bold"):
                    content = f"**{content}**"
                if annotations.get("italic"):
                    content = f"*{content}*"
                if annotations.get("strikethrough"):
                    content = f"~~{content}~~"
                if annotations.get("code"):
                    content = f"`{content}`"
                if annotations.get("underline"):
                    content = f"<u>{content}</u>"

            text += content

        return text

    def create_front_matter(self, page):
        """Front matter 생성"""
        title = page["properties"]["title"]["title"][0]["plain_text"]
        
        # 터미널에서 카테고리와 태그 입력 받기
        categories_input = input("Enter categories (comma-separated): ").strip()
        tags_input = input("Enter tags (comma-separated): ").strip()
        
        # 입력값을 리스트로 변환
        categories = [cat.strip() for cat in categories_input.split(",") if cat.strip()]
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        
        front_matter = {
            "title": title,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "categories": categories if categories else ["개발"],  # 기본값 설정
            "tags": tags,
            "toc": True
        }
        return yaml.dump(front_matter, allow_unicode=True)

    def convert_page(self, page_id):
        page = self.notion.pages.retrieve(page_id)

        # 페이지 제목 가져오기
        self.current_page_title = page["properties"]["title"]["title"][0]["plain_text"]

        blocks = self.notion.blocks.children.list(page_id)

        content = f"---\n{self.create_front_matter(page)}---\n\n"

        for block in blocks["results"]:
            content += self.convert_block_to_markdown(block)

        title_slug = re.sub(r'[^a-z0-9]+', '-', self.current_page_title.lower())
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{title_slug}.md"

        with open(self.posts_dir / filename, 'w', encoding='utf-8') as f:
            f.write(content)

        return filename

def main():
    notion_token = "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"  # 여기에 실제 토큰을 입력하세요
    page_id = str(input("Type Page ID: "))
    
    converter = NotionToJekyll(notion_token)
    filename = converter.convert_page(page_id)
    print(f"Created post: {filename}")

if __name__ == "__main__":
    main()