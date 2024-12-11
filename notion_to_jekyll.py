import os
import time
import uuid
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
        # 첫 번째 태그를 파일명에 포함
        tag_label = f"[{self.first_tag}]" if hasattr(self, 'first_tag') else ""

        # 포스트 제목과 태그로 폴더명 생성
        folder_name = f"{tag_label}-{page_title}".replace(" ", "_").replace("/", "_").lower()
        folder_name = re.sub(r'[^a-z0-9_\-]', '', folder_name)  # 불필요한 문자 제거

        image_folder = self.image_dir / folder_name
        image_folder.mkdir(parents=True, exist_ok=True)

        # 이미지 파일명에 UUID 추가
        unique_id = uuid.uuid4().hex
        filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{unique_id}.png"
        image_path = image_folder / filename

        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(image_path, 'wb') as f:
                f.write(response.content)
            time.sleep(0.5)  # API 요청 제한 방지를 위한 지연
            print(f"Image downloaded: {image_path}")
            return f"/assets/images/{folder_name}/{filename}"
        except Exception as e:
            print(f"Failed to download image: {url} - {e}")
            return None

    def convert_block_to_markdown(self, block, indent_level=0):
        """노션 블록을 마크다운으로 변환"""
        block_type = block["type"]
        text = ""
    
        try:
            indent = '    ' * indent_level  # 현재 들여쓰기 레벨 적용

            if block_type == "column_list":
                columns = self.notion.blocks.children.list(block["id"])["results"]
                text = "<div class='column-list' style='display: flex; gap: 1em;'>\n"
                for column in columns:
                    text += self.convert_block_to_markdown(column, indent_level + 1)
                text += "</div>\n\n"

            elif block_type == "column":
                children = self.notion.blocks.children.list(block["id"])["results"]
                text = "<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>\n"
                for child in children:
                    text += self.convert_block_to_markdown(child, indent_level + 1)
                text += "</div>\n"

            elif block_type == "paragraph":
                content = self.convert_rich_text(block["paragraph"]["rich_text"])
                text = f"{content}\n\n" if content else "\n"
    
            elif block_type == "heading_1":
                text = f"\n# {self.convert_rich_text(block['heading_1']['rich_text'])}\n\n"
    
            elif block_type == "heading_2":
                text = f"\n## {self.convert_rich_text(block['heading_2']['rich_text'])}\n\n"
    
            elif block_type == "heading_3":
                text = f"\n### {self.convert_rich_text(block['heading_3']['rich_text'])}\n\n"
    
            elif block_type == "bulleted_list_item":
                content = self.convert_rich_text(block['bulleted_list_item']['rich_text'])
                text = f"{indent}- {content}\n"

                # 하위 항목이 있는 경우 재귀 호출
                if block.get("has_children", False):
                    children = self.notion.blocks.children.list(block["id"])["results"]
                    for child in children:
                        text += self.convert_block_to_markdown(child, indent_level + 1)


            elif block_type == "numbered_list_item":
                content = self.convert_rich_text(block['numbered_list_item']['rich_text'])
                text = f"{indent}1. {content}\n"

                # 하위 항목이 있는 경우 재귀 호출
                if block.get("has_children", False):
                    children = self.notion.blocks.children.list(block["id"])["results"]
                    for child in children:
                        text += self.convert_block_to_markdown(child, indent_level + 1)
    
            elif block_type == "code":
                language = block["code"]["language"]
                code = self.convert_rich_text(block["code"]["rich_text"])
                text = f"```{language}\n{code}\n```\n\n"
    
            elif block_type == "equation":
                expr = block['equation']['expression']
                text = f"$${expr}$$\n\n"
    
            elif block_type == "quote":
                text = f"> {self.convert_rich_text(block['quote']['rich_text'])}\n\n"
    
            elif block_type == "callout":
                icon = block["callout"].get("icon", {})
                emoji = ""
                if icon and "emoji" in icon:
                    emoji = icon["emoji"]

                callout_text = self.convert_rich_text(block["callout"]["rich_text"])
                text = (
                    f"{indent}> {emoji} {callout_text}\n\n"
                )
    
            elif block_type == "image":
                if block["image"]["type"] == "external":
                    url = block["image"]["external"]["url"]
                else:
                    url = block["image"]["file"]["url"]

                caption = ""
                if "caption" in block["image"] and block["image"]["caption"]:
                    caption = self.convert_rich_text(block["image"]["caption"])
                    # 캡션의 줄바꿈을 <br>로 변환
                    caption = caption.replace("\n", "<br>")

                image_path = self.download_image(url, self.current_page_title)
                if image_path:
                    if caption:
                        text = f"![]({image_path})\n\n>*{caption}*\n\n"
                    else:
                        text = f"![]({image_path})\n\n"
    
            elif block_type == "divider":
                text = f"{indent}---\n\n"  # 마크다운 구분선 추가

            else:
                text = ""
                print(f"Unhandled block type: {block_type}")
    
        except Exception as e:
            print(f"Error processing block type {block_type}: {str(e)}")
            text = ""
    
        return text if text else ""

    def convert_rich_text(self, rich_text):
        """리치 텍스트를 마크다운으로 변환"""
        if not rich_text:
            return ""

        text = ""
        for rt in rich_text:
            content = rt["plain_text"]

            # 수식 처리 개선
            if rt.get("type") == "equation":
                content = f"$${content}$$"
            else:
                annotations = rt.get("annotations", {})
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

        # 첫 번째 태그 추출
        self.first_tag = tags[0] if tags else "General"
        post_head_tag = "[" + self.first_tag + "] "
        
        front_matter = {
            "title": post_head_tag + title,
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
            content += self.convert_block_to_markdown(block, indent_level=0)

        # 첫 번째 태그를 제목에 추가
        tag_label = f"[{self.first_tag}]"
        title_slug = re.sub(r'[^a-z0-9]+', '-', self.current_page_title.lower())
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{tag_label}-{title_slug}.md"

        with open(self.posts_dir / filename, 'w', encoding='utf-8') as f:
            f.write(content)

        return filename

def extract_page_id_from_url(url):
    """노션 링크에서 페이지 ID 추출"""
    match = re.search(r"([a-f0-9]{32})", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Notion URL. Could not extract page ID.")
    
def main():
    notion_token = "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"  # 여기에 실제 토큰을 입력하세요
    notion_url = input("Enter Notion page URL: ").strip()

    try:
        page_id = extract_page_id_from_url(notion_url)
        print(f"Extracted Page ID: {page_id}")
    except ValueError as e:
        print(e)
        return
    
    converter = NotionToJekyll(notion_token)
    filename = converter.convert_page(page_id)
    print(f"Created post: {filename}")

if __name__ == "__main__":
    main()