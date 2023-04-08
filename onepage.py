import os
import glob
import re
import argparse
import pikepdf

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, default=1, help="starting number")
args = parser.parse_args()

# PDF 파일 경로 지정
pdf_path = "./pdfs/*.pdf"
output_path = "./outputs"

if not os.path.exists(output_path):
    os.makedirs(output_path)

for i, file_path in enumerate(sorted(glob.glob(pdf_path)), start=args.n):
    old_file_name = os.path.basename(file_path)
    old_file_name = re.sub(r"\.pdf$", "", old_file_name)

    new_file_name = f"IS-03-{i}. {old_file_name}.pdf"

    with pikepdf.open(file_path) as pdf_reader:
        first_page = pikepdf.Page(pdf_reader.pages[0])

        with pikepdf.new() as pdf_writer:
            pdf_writer.pages.append(first_page)
            new_pdf_path = os.path.join(output_path, new_file_name)
            os.makedirs(output_path, exist_ok=True)
            pdf_writer.save(new_pdf_path)
