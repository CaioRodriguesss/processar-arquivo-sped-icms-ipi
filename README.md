<h1>Processamento de arquivos SPED ICMS/IPI e EFD-Contribuições</h1>

<h2>Objetivo</h2>
<p>Processar o arquivo em formato .txt do SPED ICMS/IPI e do EFD-Contribuições, utilizado para leitura e transmissão pelos programas fornecidos pela Receita federal, de forma a estrurar os dados em um arquivo Excel (.xlsx) para facilitar o manuseio, a verificação e a interpratação dos dados presentes no arquivo.</p>

<h2>O projeto</h2>
<p>O projeto consiste em uma interface gráfica que permite que o usuário selecione o arquivo em formato .txt com dados do SPED ICMS/IPI ou do EFD-Contribuições que deseja processar e transforme-o em um arquivo Excel (.xlsx) paginado. Após o processamento, um novo arquivo é gerado e salvo na mesma pasta de seleção do arquivo em formato .txt. Dentro do Excel, os dados irão vir como texto, sendo necessário que o usuário faça a definição de tipos de dados, porque o processo normal ainda não faz isso.</p>
<p>Como forma de informação complementar do programa, caso o usuário tente processar o mesmo arquivo .txt um sgunda vez, o arquivo em formato .xlsx gerado anteriormente será sobrescrito pelo novo arquivo .xlsx, ou seja, a informação do arquivo anterior é perdida e substituída pela do novo arquivo. Para contornar isso, basta retirar o arquivo .xlsx gerado anteriormente da pasta, dessa forma, nada será sobrescrito.</p>
<p>Além disso, por falta de conhecimento para gerenciar a merória gasta da maneira correta, o prorgama possui um timer de 1 minuto que encerra o processo caso chegue em 00:00. Isso visa não deixar o programa aberto por acidente ou esquecimento do usuário.</p>

<h2>Como utilizar</h2>
<p>Faça o download dos arquivos ou clone o projeto em um repositório local. Com um interpretador Python instalado, edite o arquivo instalador.py de acordo com a sua necessidade e compile o arquivo em um único arquivo "onefile". Por fim, deve estar presente na pasta para funcionamento o arquivo .exe e o banco de dados "banco_validador.db", os ícones .ico não interferem no funcionamento normal, mas deixam as telas com uma imagem padrão do programa.</p>

<h2>Versões</h2>
<ul>
    <li>Python==3.11.0</li>
    <li>openpyxl==3.1.2</li>
    <li>PySimpleGui==4.60.4</li>
    <li>pyinstaller==5.11.0</li>
</ul>
