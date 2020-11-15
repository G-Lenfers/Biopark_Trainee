xxxxxxxxxxxxxxxxxx
xxx   Read Me   xxx
xxxxxxxxxxxxxxxxxx

Este arquivo apresenta descrições do programa desenvolvido para etapa técnica do programa de Trainees Biopark.

Sumário
1. Controle de versões e pacotes utilizados
2. Desenvolvimento do programa
3. Instruções para uso
4. Limitações do programa
5. Sugestões de melhoria para versões futuras

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxx   1. Controle de versões e pacotes utilizados   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

A plataforma de envio de agendamento de comunicação foi desenvolvida em linguagem Python. Para isto, utilizou-se a Anaconda para baixar a interface de usuário Spyder, bem como todos os pacotes necessários. A seguinte lista apresenta as versões utilizadas.

-Windows 10
-Conda 4.9.1
-Spyder: 4.1.5
-Python: 3.8.5
-Flask: 1.1.2
-Flask-SQLAlchemy: 2.4.4

Se sua máquina não possui algum dentre os listados, será necessário realizar o download e instalação.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxx   2. Desenvolvimento do programa   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

O autor optou pelo desenvolvimento na linguagem Python por ter mais afinidade esta. Embora acredite que seja importante conhecer Java, este que escreve ainda não teve a oportunidade de inicar os estudos de tal linguagem. 

Importante ressaltar que o autor desenvolveu o programa utilizando o sistema operacional Windows 10. Sendo assim,  a seção de instruções de uso (mais specificamente, na seção 3.4) foi escrita com base em tal sistema. Caso esteja utilizando Unix ou MAC, os comandos podem ser levemente diferentes.

Ainda, optou-se pela utilização do pacote Flask para lidar com o servidor. Esta decisão basea-se no fato de que tal pacote apresentou a melhor curva de aprendizagem. Vale ressaltar que o autor possuía conhecimento nulo em desenvolvimento de redes antes de receber o desafio do programa Trainee.

O fato acima acarretou, também, na escolha do banco de dados SQLite, pelo mesmo motivo da curva de aprendizagem. Este se trata de uma biblioteca que implementa um banco de dados imbutido na memória da máquina, diferenciando-se das opções propostas pelo desafio (MySQL, PostgreSQL). O autor buscou aprender sobre como implementar tais bancos, mas não obteve sucesso a tempo.

Por fim, o autor convida a todos os avaliadores a visualizarem o código fonte. Pois tais arquivos foram escritos de forma que facilite a leitura, com a inserção de vários comentários ao longo do código.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxx   3. Instruções para uso   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

3.1 - Baixe a pasta de arquivos na página do Git (link);
3.2 - Baixe e instale os programas e pacotes descritos na seção 1;
3.3 - Abra o console Python e mova o diretório para a pasta dos arquivos baixados na seção 3.1;
3.4 - Antes de rodar o programa app.py, fundamental digitar no console os seguintes comandos para criar o banco de dados:

from app import db
db.create_all()

3.5 - Rode o programa app.py;
3.6 - Abra no seu navegador o seguinte endereço:

http://localhost:5000/home

3.7 - Clique no botão indicado para ir à pagina com todos os agendamentos. Inicialmente a página deverá estar vazia.
3.8 - Clique no botão "Agendar novo envio de comunicação"
3.9 - Preencha os campos indicados. NOTA: o campo "Mês" deverá ser preenchido com valores numéricos. Exemplo: "10" ao invés de "Outubro";
3.10 - Após preencher os campos, clique em "Solicitar agendamento"
3.11 - Perceba que seu agendamento foi adicionado na página com todos agendamentos. Note também que é possível deletá-lo, caso queira.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxx   4. Limitações do programa   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

A maior limitação deste programa, conforme comentado na seção 2, é a utilização de banco de dados que salva as informações na memória da própria máquina. Conforme descrito no desafio, deveria ser utilizado um banco de dados que salve as informações na nuvem. Assim, o cliente pode utilizar a aplicação mesmo estando em um host diferente, além de que o programa estaria apto a receber comandos de múltiplos clientes. 

Houve ainda a dificuldade de salvar as informações no banco de dados com formato JSON. Por padrão, este formato aceita texto na codificação ASCII. Todavia, por utilizarmos acentos na Língua Portuguesa, a codificação mais adequada deveria ser Unicode. Por não conseguir resolver a formatação a tempo, o autor preferiu não utilizar formato JSON no banco de dados.

A função "datetime" do Python retorna datas no formato AAAA/MM/DD. O autor tentou trocar a ordem para DD/MM/AAAA mas esbarrou no que chamam de "leading zeros", que acarreta em 1/1/2020 ao invés de 01/01/2020. Até aí tudo bem.  O pior está nos horários, apresentando 5:2 ao invés de 05:02. Pelos minutos consistirem em formato que traria mais dúvidas do que esclarecimentos, o autor preferiu deixar o formato de datas e horários no padrão.

Uma última limitação, o campo "Mês" na página de "Adicionar agendamento" aceita apenas entradas numéricas. Entradas como "nov", "Novembro", ou ainda "November" não são aceitas pelo programa, sendo necessário neste caso incluir "11" no campo.

Embora existam tais limitações, o autor preferiu enviar o projeto da forma como conseguiu desenvolver, ao invés de não entregar nenhum programa e desistir do programa de Trainee. O autor fez o possível para aprender do zero todos os conceitos de desenvolvimento de redes em 5 dias.

O autor aguarda abertamente críticas e sugestões dos avaliadores.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxx   5. Sugestões de melhoria para versões futuras   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

5.1 - Implementar banco de dados MySQL ou PostreSQL;
5.2 - Descobrir e implementar uma forma de hospedar o programa além do "localhost:5000";
5.3 - Salvar os dados em formato JSON com codificação Unicode no banco de dados;
5.4 - Aprimorar a apresentação das datas dos agendamentos de forma que fique mais natural para os brasileiros;
5.5 - Deixar o programa mais robusto na inserção do campo "Mês";
5.6 - Aprender e aplicar mais técnicas front-end para que o programa fique mais agradável visualmente.