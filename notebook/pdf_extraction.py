import fitz

doc=fitz.open("raw_data/annual_report_2024.pdf")

all_text=""

for page_num in range(len(doc)):
    page=doc.load_page(page_num)
    text=page.get_text()
    all_text+=text

with open(
    "cleaned_data/annual+report_2024.txt",
    "w",encoding="utf-8"
)as f :
    f.write(all_text)

    

doc=fitz.open("raw_data/annual_report_2025.pdf")

all_text=""

for page_num in range(len(doc)):
    page=doc.load_page(page_num)
    text=page.get_text()
    all_text+=text

    with open(
        "cleaned_data/annual+report_2025.txt",
        "w",encoding="utf-8"
    )as f:
        f.write(all_text)
    
  

doc=fitz.open("raw_data/quaterly_report_q1.pdf")

all_text=""

for page_num in range(len(doc)):
    page=doc.load_page(page_num)
    text=page.get_text()
    all_text+=text

    with open(
        "cleaned_data/quaterly+report_q1.txt",
        "w",encoding="utf-8"
    )as f:
        f.write(all_text)
    
    

doc=fitz.open("raw_data/quaterly_report_q2.pdf")

all_text=""

for page_num in range(len(doc)):
    page=doc.load_page(page_num)
    text=page.get_text()
    all_text+=text

    with open(
        "cleaned_data/quaterly+report_q2.txt",
        "w",encoding="utf-8"
    )as f:
        f.write(all_text)
    
    

doc=fitz.open("raw_data/quaterly_report_q3.pdf")

all_text=""

for page_num in range(len(doc)):
    page=doc.load_page(page_num)
    text=page.get_text()
    all_text+=text

    with open(
        "cleaned_data/quaterly+report_q3.txt",
        "w",encoding="utf-8"
    )as f:
        f.write(all_text)
    
    

doc=fitz.open("raw_data/quaterly_report_q4.pdf")

all_text=""

for page_num in range(len(doc)):
    page=doc.load_page(page_num)
    text=page.get_text()
    all_text+=text

    with open(
        "cleaned_data/quaterly+report_q4.txt",
        "w",encoding="utf-8"
    )as f:
        f.write(all_text)
    
    