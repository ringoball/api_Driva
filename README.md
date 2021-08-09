# api_Driva
Simple api for exam of Driva

Para usar no Windows após o repositório vá no path C:/../api_Driva.

Dê o comando cd venv/Scripts e o path ficará assim: C:/../api_Driva/venv/Scripts e então use o activate para ativar a venv.

Certifique-se que ficou assim após ativar a venv: (venv) C:/../api_Driva/venv/Scripts.

Volte ao diretório raiz, no caso api_driva: (venv) C:/../api_Driva

Instale o django: pip install django (a versão usada na aplicação é a 3.2.6 e a do python é a 3.9.6).

Instale também o swapi: pip install swapi e então ative o servidor: python manage.py runserver

<br />

Caso esteja usando Linux vá no path C:/../api_Driva.

Dê o comando: source venv/Scripts/activate

Certifique-se que ficou assim após ativar a venv: (venv) C:/../api_Driva/venv/Scripts.

Volte ao diretório raiz, no caso api_driva: (venv) C:/../api_Driva

Instale o django: pip install django (a versão usada na aplicação é a 3.2.6 e a do python é a 3.9.6).

Instale também o swapi: pip install swapi e então ative o servidor: python manage.py runserver


<br />
Para fazer a soma é necessário um post com um json no seguinte formato:

{
  "numero1" : 10,
  "numero2" : 10
}

Pode-se substituir os 10 pelo número desejado.
