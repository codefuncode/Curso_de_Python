import requests as req
r = req.get('localhost/Proyectos/codefuncode/Curso_de_Python/docs/php.php')
print(r.text)