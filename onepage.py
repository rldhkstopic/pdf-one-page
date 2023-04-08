import os
import glob
import re
import argparse
import pikepdf

# 명령행 인수 파싱
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, default=1, help="starting number")
args = parser.parse_args()

# PDF 파일 경로 지정
pdf_path = "./pdfs/*.pdf"
output_path = "./outputs"

if not os.path.exists(output_path):
    os.makedirs(output_path)

# PDF 파일 이름 변경 및 첫 페이지 추출
for i, file_path in enumerate(sorted(glob.glob(pdf_path)), start=args.n):
    # 파일 이름에서 접두사를 제거하고 한글 부분만 추출
    old_file_name = os.path.basename(file_path)
    old_file_name = re.sub(r"\.pdf$", "", old_file_name)

    # 새로운 파일 이름 생성
    new_file_name = f"IS-03-{i}. {old_file_name}.pdf"

    # pikepdf 라이브러리를 사용하여 PDF 파일의 첫 페이지를 복사
    with pikepdf.open(file_path) as pdf_reader:
        first_page = pikepdf.Page(pdf_reader.pages[0])

        with pikepdf.new() as pdf_writer:
            # 첫 페이지를 새로운 PDF에 추가
            pdf_writer.pages.append(first_page)

            # 새로운 PDF 파일을 저장할 경로 설정
            new_pdf_path = os.path.join(output_path, new_file_name)

            # 새로운 PDF 파일을 저장
            os.makedirs(output_path, exist_ok=True)
            pdf_writer.save(new_pdf_path)
