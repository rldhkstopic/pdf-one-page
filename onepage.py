import os
import glob
import re
import PyPDF2
import argparse

# 명령줄 인수 처리
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--start", type=int, default=1, help="start number")
args = parser.parse_args()

# PDF 파일 경로 지정
pdf_path = "./pdfs/*.pdf"

# PDF 파일 이름 변경 및 첫 페이지 추출
for i, file_path in enumerate(glob.glob(pdf_path)):
    # 파일 이름에서 접두사를 제거하고, "IS-03-N." 형태의 접두사 추가
    new_file_name = re.sub(r"^\d+_", "", os.path.basename(file_path))
    new_file_name = re.sub(r"\.pdf$", "", new_file_name)
    new_file_name = f"IS-03-{i+args.start:02d}. {new_file_name}.pdf"
    
    with open(file_path, "rb") as f:
        # PyPDF2 라이브러리를 사용하여 PDF 파일의 첫 페이지를 복사
        pdf_reader = PyPDF2.PdfFileReader(f)
        first_page = pdf_reader.getPage(0)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(first_page)
        
        # 새로운 PDF 파일을 저장할 경로 설정
        new_pdf_dir = "outputs"
        new_pdf_path = os.path.join(new_pdf_dir, new_file_name)
        
        # 새로운 PDF 파일을 저장
        os.makedirs(new_pdf_dir, exist_ok=True)
        with open(new_pdf_path, "wb") as new_pdf:
            pdf_writer.write(new_pdf)
