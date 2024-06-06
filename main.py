import os
import PyPDF2


def extract_pages(input_folder, output_folder, num_pages=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("--------Converting Pages----------")
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(input_folder, filename)
            output_pdf = os.path.join(output_folder, filename)

            with open(input_pdf, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                writer = PyPDF2.PdfWriter()

                for page_num in range(num_pages):
                    if page_num < len(reader.pages):
                        writer.add_page(reader.pages[page_num])

                with open(output_pdf, "wb") as output_file:
                    writer.write(output_file)
        print("Converted File Successfully\n")


input_folder_path = "input"
output_folder_path = "output"

extract_pages(input_folder_path, output_folder_path)
