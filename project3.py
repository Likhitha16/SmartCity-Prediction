import os
from PyPDF2 import PdfReader
def readPdf():
    folder_path = "../cs5293sp23-project3/smartcity"
    files = os.listdir(folder_path)
    all_text = []
    for file_name in files:
        if file_name.endswith(".pdf"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page in range(len(pdf_reader.pages)):
                pdf_page = pdf_reader.pages[page]
                text = pdf_page.extract_text()
                all_text.append(text)
                print(all_text)
def cityandrawtext():
    data = []
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
    file_path = os.path.join(folder_path, pdf_file)
# Extract the city name from the file name
    city_name = pdf_file[:-4]  # Remove '.pdf' from the file name
     # Extract the raw text from the PDF file
    with open(file_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        raw_text = ''
        for page in pdf_reader.pages:
            raw_text += page.extract_text()
    data.append([city_name, raw_text])
df = pd.DataFrame(data, columns=['city', 'raw_text'])
print(df)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--document",type=str,required=True,help="cities",action="append")
    args = parser.parse_args()
    main(args)
