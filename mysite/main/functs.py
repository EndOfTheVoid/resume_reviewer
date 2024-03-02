from PyPDF2 import PdfReader 
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()


def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    content = content.replace("\n", " ")
    return content


def file_to_text_to_result(files,jobname, jobtext):
    responselist = []
    prompt = read_file("prompt_text.txt")
    for file in files:
        reader = PdfReader(file) 
        fulltext = ""
        for i in range(len(reader.pages)):
            page = reader.pages[i] 
            text = page.extract_text()
            fulltext += " "
            fulltext += text
            fulltext = fulltext.replace(",", ";")
            cvPrompt = "Job Name: " + jobname + " Job Description: " + jobtext + " Resume: " + fulltext
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": cvPrompt}
            ]
        )

        temp = json.loads(response.choices[0].message.content)

        responselist.append(temp)

    return responselist