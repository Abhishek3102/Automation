import pyttsx3, PyPDF2
pdf_reader = PyPDF2.PdfReader(open('DJ60_LockNCode_1692.pdf', 'rb'))
speaker = pyttsx3.init()

for page_number in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_number].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'pdf_in_audio.mp3')
speaker.runAndWait()

speaker.stop()