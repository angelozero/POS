Ao longo da aula, discutimos sobre a importância dos testes no desenvolvimento de APIs. Sobre os tipos de testes, considere as seguintes afirmações:

Testes unitários: verificam o comportamento individual de unidades isoladas de código, como funções, métodos ou classes. Eles garantem que cada unidade funcione corretamente de acordo com suas especificações.
Testes de carga e desempenho: avaliam a capacidade da API de lidar com cargas de trabalho intensas e medem seu desempenho sob condições de alto tráfego.
Testes de integração: verificam a interação entre diferentes partes da API e suas dependências externas, como bancos de dados, serviços web ou outras APIs.
Testes de segurança: verificam se a API atende aos requisitos e aos comportamentos esperados pelo usuário final. Eles são escritos do ponto de vista do usuário e testam os fluxos de trabalho principais da API para garantir que ela funcione corretamente em cenários reais de uso. 
Assinale a alternativa que contém todas as afirmações corretas:

---

Sobre o padrão arquitetural cliente-servidor, vimos que nele a computação é dividida entre várias máquinas. A topologia desse padrão determina que componentes em uma máquina servidor fornecem funcionalidades para componentes em várias máquinas clientes por meio de uma conexão de rede. O servidor centraliza recursos computacionais. Assim, tais recursos podem ser compartilhados por muitos usuários, e os clientes desses recursos podem permanecer relativamente simples.

Diante desse contexto e do conteúdo apresentado na aula 1, considere as seguintes afirmações sobre as vantagens de uso do padrão arquitetural cliente-servidor:

I. O armazenamento de dados e a lógica de negócios ficam centralizados no servidor, facilitando o gerenciamento e a manutenção da aplicação.
II. A centralização das medidas de segurança permite ao servidor controlar a autenticação de usuários e a criptografia dos dados.
III. A escalabilidade do sistema possibilita adicionar ou remover clientes e servidores conforme a demanda.
IV. A disponibilidade do sistema é ilimitada, independentemente da confiabilidade da conexão de rede entre os clientes e o servidor.

Assinale a alternativa que contém afirmações corretas:

---

Ainda falando dos testes de segurança, considere os seguintes exemplos de testes e, a partir de suas descrições, identifique quais são exemplos corretos de teste de segurança.

I. Teste de autenticação inadequada. Esse teste verifica se a API implementa corretamente os mecanismos de autenticação e autorização. O objetivo é testar se apenas usuários autenticados e autorizados têm acesso aos recursos da API, garantindo que não seja possível explorar vulnerabilidades de acesso não autorizado.
II. Teste de validação de entrada. Esse teste verifica se a API valida corretamente os dados de entrada. O objetivo é testar se a API rejeita dados inválidos ou maliciosos e se trata adequadamente os casos de borda, evitando vulnerabilidades como ataques de buffer overflow ou manipulação de dados não esperados.
III. Teste de acessibilidade. Esse teste visa a garantir que uma aplicação ou sistema, incluindo uma API, seja acessível e utilizável por todas as pessoas, independentemente de suas habilidades físicas ou cognitivas.

Assinale a alternativa que identifica os exemplos corretos de teste de segurança:

---

O REST é amplamente utilizado na construção de APIs web, pois segue os princípios da web, usando métodos HTTP para manipular recursos e transferir dados em formatos como JSON ou XML. Além disso, ele é adequado para cenários de comunicação entre sistemas em uma arquitetura orientada a recursos.

Sobre os princípios seguidos pelo REST, considere as seguintes afirmações:

O REST utiliza os métodos GET, POST, PUT e DELETE para manipulação de recursos.
O REST não faz uso de URIs para identificar recursos.
O REST não tem ênfase na simplicidade, na escalabilidade e na evolução dos sistemas.
O REST permite a transferência de dados em formatos como JSON e XML.
O REST não faz uso dos padrões e infraestrutura já existentes na web.
Assinale a alternativa que contém afirmações corretas:

--- 

Uma variante do padrão em camadas bastante difundida e utilizada é o padrão modelo-visualização-controlador (MVC). A ideia do padrão MVC é separar o projeto em três camadas lógicas e independentes: o modelo (manipulação da lógica de dados), a visualização (a interface do usuário) e o controlador (fluxo de aplicação). Essa separação tem o objetivo de facilitar a manutenção da aplicação e fornecer sua reutilização em projetos futuros.

Sobre o padrão MVC, considere as seguintes afirmações:

O projeto seguindo o padrão MVC resulta em um código mais testável, pois as diferentes camadas podem ser expostas a diferentes massas de teste com diferentes objetivos.
O uso do padrão MVC não aumenta a complexidade e o tamanho do código-fonte.
É possível ter múltiplas visualizações do mesmo modelo no padrão MVC, e essas visualizações podem ser habilitadas ou desabilitadas em tempo de execução.
O padrão MVC não busca reduzir o acoplamento entre as camadas do sistema.
Assinale a alternativa que contém afirmações corretas:

---

Como foi visto na segunda aula, o RPC é adequado para cenários em que uma aplicação cliente precisa fazer chamadas a procedimentos ou funções em um servidor remoto. Ele é muito utilizado em sistemas distribuídos que exigem comunicação eficiente entre componentes.

Existem variantes do estilo RPC. Sobre essas variantes, considere as seguintes afirmações:

XML-RPC usa XML como formato de mensagem para comunicação entre sistemas.
JSON-RPC usa JSON como formato de mensagem para comunicação entre sistemas.
gRPC é exclusivamente utilizado em sistemas legados.
Todas as variantes do RPC são baseadas em chamadas de procedimento remoto. 
Assinale a alternativa que contém afirmações corretas:

---

O GraphQL é útil quando há necessidade de flexibilidade na obtenção de dados por parte do cliente. É comumente usado em aplicações com requisitos complexos de consulta, como redes sociais ou painéis de administração, em que diferentes conjuntos de dados são buscados em uma única requisição.

No comparativo entre o REST e o GraphQL, considere as seguintes afirmações:

O REST permite o overfetching (receber mais dados do que o necessário) e o underfetching (receber menos dados do que o necessário), enquanto o GraphQL resolve esse problema.
O REST utiliza apenas o formato JSON para transferência de dados.
O GraphQL é adequado para cenários em que é necessária flexibilidade na obtenção de dados.
O REST é mais eficiente em relação ao consumo de recursos de rede.
Assinale a alternativa que contém afirmações corretas:

---

O padrão arquitetural em camadas é um dos mais conhecidos e utilizados para desenvolvimento de aplicações web. Sobre esse padrão arquitetural, considere as seguintes afirmações:


O padrão em camadas consiste em um conjunto de duas ou mais camadas organizadas hierarquicamente, cada uma com uma atribuição específica e se comunicando com as camadas subjacentes por meio de interfaces definidas.
O padrão em camadas tem duas especializações: a separação em camadas físicas (N-tier architecture) e a separação em camadas lógicas (layered architecture), em que as camadas físicas representam entidades físicas como computadores e dispositivos móveis, enquanto as camadas lógicas separam conceitos ou funcionalidades.
O padrão em camadas é utilizado exclusivamente em aplicações web.
Na separação em camadas físicas, cada camada representa uma funcionalidade específica.
Na arquitetura com três camadas lógicas (3-layer architecture), a camada de interface com usuário é responsável pela interação com o usuário; a camada de lógica de negócio contém a lógica principal do sistema; e a camada de acesso aos dados permite a interação com o banco de dados. Cada camada se comunica apenas com as camadas vizinhas, seguindo o princípio da separação de conceitos
Assinale a alternativa que contém afirmações corretas:

---

Ao longo da aula, foi abordada a importância da conteinerização com o uso do Docker. No texto a seguir, temos os comandos de um Dockerfile:

FROM python:3.9
WORKDIR /app
COPY requirements.txt
RUN pip install --no-no-cache-dir -r requirements.txt
COPY ..
CMD ["python", "app.py"]

Dentro do contexto do Dockerfile fornecido, considere as seguintes afirmações:

I. No Dockerfile está sendo definida uma imagem que vai utilizar como base um sistema operacional preparado para a execução do Python versão 3.9.
II. Na quarta linha acontece a instalação das dependências do projeto a partir do arquivo requirements.txt.
III. O comando COPY é usado para copiar os arquivos do projeto para o diretório de trabalho.
IV. O comando CMD define o comando padrão a ser executado quando o contêiner for iniciado.

Assinale a alternativa que contém todas as afirmações corretas:

