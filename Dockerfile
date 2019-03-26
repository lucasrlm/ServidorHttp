FROM python:3

ADD ServidorHttp.py /
ADD ConversorInteiroParaExtenso.py /

CMD [ "python", "./ServidorHttp.py" ]