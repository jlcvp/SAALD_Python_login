#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

tree = ET.parse('livros.xml')
root = tree.getroot()

tree_login = ET.parse('usuarios.xml')
root_login = tree_login.getroot()

urls = (
    '/livros', 'list_livros',
    '/livros/(.*)', 'get_livro',
    '/login', 'login' 
)

app = web.application(urls, globals())



class list_livros:        
    def GET(self):
	output = 'livros:[';
	for child in root:
                print 'child', child.tag, child.attrib
                output += str(child.attrib) + ','
	output += ']';
        return output

class get_livro:
    def GET(self, id): ## Pelo que entendi, ele busca por id
	for child in root:
		if child.attrib['id'] == id: ##Aqui
		    return str(child.attrib)

class login:
    def GET(self):
	
	params = web.input()
	print 'opa!\n'
	print "params= "+str(params)
	for child in root_login:
	    print child.attrib['username']
	    if child.attrib['username'] == params.username: 	#match login
		print 'login bateu'
		if child.attrib['password'] == params.password:	#match senha
		    print 'senha bateu'
		    chama_autenticacao(params.username, params.livro)
		    return True
	return False
    
    def chama_autenticacao(user,livro):
	##colocar o logica de pos login aqui, registrar o livro no nome do userdd
	

if __name__ == "__main__":
    app.run()
