# resume_reviewer
A simple Django app that takes in one or more resumes, a job name, and a job description to give out filtered data and a relevancy score

To use it, install all dependencies mentioned in the requirements.txt file. Also, inside the root directory, i.e., the mysite folder, create a new folder named media, and inside that, create a folder named cvs. This is the folder where the resume files will be stored locally.  
Open the terminal and run "python manage.py runserver". This will start up the server and allow you to use the app.  

Approach:  
I used a fairly straightforward approach for this project due to the time constraints. I took in the resume files via an input field with the "multiple" attribute. This input field had to be tinkered with a bit in the HTML file used to render it, and then combined with a js function and then a view function to successfully store the actual file in a folder and the file path in the database. The next page was easy to build as it utilizes a simple form to take in two inputs, which are stored in the database as well.   
The pdfs are parsed and converted into a string using the PYPDF2 library, the strings are then used as input for OpenAI's API call, which utilizes chatgpt 3.5 turbo. The most important part of this step was the prompt, which I stored in prompt.txt due to its lengthy nature.  
The json_object I received from the API call was very difficult to work with since it had a non-standard type. It took a lot of trial and error to utilize the file and use it inside the results.html file used to render the results page.
