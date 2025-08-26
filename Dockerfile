FROM python:slim
WORKDIR /home/Project/page_obj_proj
COPY ./page_obj_proj /home/Project/page_obj_proj
RUN pip install -r requirements.txt
CMD ["pytest", "-s", "-v", "testScripts/test_script1.py", "--html=outputs/report.html", "--reruns", "2"]

