from pypdf import PdfReader, PdfWriter
import os

def merge_pdfs(pdf_files, output_file):
    writer = PdfWriter()

    for pdf in pdf_files:
        if not os.path.exists(pdf):
            print(f"File not found: {pdf}")
            continue

        reader = PdfReader(pdf)

        for page in reader.pages:
            writer.add_page(page)

    with open(output_file, "wb") as output:
        writer.write(output)

    print(f"\nPDFs merged successfully into '{output_file}'")


def main():
    print("PDF Merger using pyPDF")

    pdf_input = input("Enter PDF file names separated by commas: ")
    pdf_files = [pdf.strip() for pdf in pdf_input.split(",")]

    output_file = input("Enter output PDF file name: ")

    merge_pdfs(pdf_files, output_file)


if __name__ == "__main__":
    main()
