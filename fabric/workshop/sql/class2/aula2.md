# Databases - Filtros e CRUD
Agora que aprendemos como fazer consultas simples ao banco de dados, e como combinar alguns de nossos resultados, vamos começar a adicionar mais algumas funcionalidades às nossas consultas.

Lembrando que vamos precisar do nosso `MySQL Server` rodando, e do banco `sakila` criado na aula anterior.

<details>
<summary>Relembranco como subir o MySQL Server</summary>

```bash
docker container start mysql-residencia
```
</details>

## O que vamos aprender?
- Dia 2:
    - Filtrar resultados de consultas com `WHERE`;
    - Utilizar operadores lógicos em consultas com `AND`, `OR` e `NOT`;
    - Criar consultas mais dinâmicas e maleáveis com `LIKE`;
    - Fazer consultas que englobam uma faixa de resultados com `IN` e `BETWEEN`;
    - Inserir dados em tabelas com `INSERT`;
    - Atualizar dados em tabelas com `UPDATE`;
    - Apagar dados em tabelas com `DELETE`;

## `WHERE` - Especificando seus resultados.
O `WHERE` é uma cláusula que nos permite filtrar os resultados de uma consulta, retornando apenas os resultados que atendem a um critério específico.
Por exemplo, se quisermos consultar todos os filmes que foram lançados em 2006, podemos fazer isso com a seguinte consulta:

```sql
SELECT * FROM sakila.film
    WHERE release_year = 2006;
```

Essa consulta retornará todos os filmes que foram lançados em 2006, e não retornará nenhum outro filme.

### `AND`, `OR` e `NOT` - Combinando condições
Podemos combinar várias condições em uma única consulta usando os operadores lógicos `AND`, `OR` e `NOT`. Esses operadores nos permitem criar consultas mais complexas e específicas.

Por exemplo, se quisermos consultar todos os filmes que foram lançados em 2006 e que possuem uma duração de mais de 90 minutos, podemos fazer isso com a seguinte consulta:

```sql
SELECT * FROM sakila.film
    WHERE release_year = 2006
        AND length >= 90;
```

> **⚠️ Atenção:** Sempre que for combinar mais de um operador lógico, atente-se para a ordem de precedência dos operadores. A ordem de precedência dos operadores lógicos é a seguinte:
> `Parênteses > Multiplicação e Divisão > Subtração e Adição > NOT > AND > OR`

Sendo assim, quando fazemos a seguinte query:

```sql
SELECT * FROM sakila.payment
WHERE amount = 0.99 OR amount = 2.99 AND staff_id = 2;
```

Como o operador `AND` tem preferência sobre o operador `OR`, ele é avaliado primeiro. Então os registro buscados são aqueles nos quais `amount = 2.99` e `staff_id = 2`. Na sequeência, são buscados os registros nos quais`amount = 0.99`, independente do valor de `staff_id`. Os valores retornados serão os resultados dessas duas buscas. Ou seja, a _query_ é executada como se tivesse os seguintes parênteses: `amount = 0.99 OR (amount = 2.99 AND staff_id = 2)`.

Para corrigir nossa _query_ de forma que ela faça mais sentido, podemos fazer o seguinte:

```sql
SELECT * FROM sakila.payment
WHERE (amount = 0.99 OR amount = 2.99) AND staff_id = 2;
```

Essa consulta retornará todos os pagamentos que foram feitos por um funcionário específico (neste caso, o funcionário com `staff_id = 2`) e que possuem um valor de pagamento de 0.99 ou 2.99.

### `LIKE` - Consultas dinâmicas
Percebemos que o `WHERE` é uma cláusula muito poderosa. Mas quando precisamos fazer comparações de strings, o comparador de igualdade (`=`) não é muito útil. Para isso, podemos usar o operador `LIKE`, que nos permite fazer consultas mais dinâmicas e flexíveis.

O operador `LIKE` é usado para buscar um padrão específico em uma coluna de texto. Ele é especialmente útil quando queremos encontrar registros que correspondem a um padrão parcial, em vez de uma correspondência exata.

Por exemplo, se quisermos buscar um filme que termine com `don`, podemos fazer isso com a seguinte consulta:

```sql
SELECT * FROM sakila.film
    WHERE title LIKE '%don';
```

O caractere `%` é um caractere curinga que representa zero ou mais caracteres. Portanto, essa consulta retornará todos os filmes que terminam com `don`, independentemente do que vem antes dele.

Temos dois caracteres curinga que podemos usar com o `LIKE`:
- `%` - Representa zero ou mais caracteres;
- `_` - Representa exatamente um caractere.

Por exemplo, se quisermos buscar um filme que tenha `DRAGON` no título, mas não termine com essa palavra, podemos fazer isso com a seguinte consulta:

```sql
SELECT * FROM sakila.film WHERE title LIKE '%DRAGON_%';
```

### `IN` e `BETWEEN` - Englobando faixas de resultados
O `IN` e o `BETWEEN` são operadores que nos permitem fazer consultas que englobam uma faixa de resultados. Eles são especialmente úteis quando queremos buscar registros que atendem a um conjunto específico de condições.

O operador `IN` é usado para buscar registros que correspondem a um conjunto específico de valores. Por exemplo, se quisermos buscar por um grupo de atores pelo seu primeiro nome, poderiamos fazer isso com a seguinte consulta:

```sql
SELECT * FROM sakila.actor
    WHERE first_name IN ('PENELOPE', 'NICK', 'JULIE');
```

Essa consulta retornará todos os atores que possuem o primeiro nome `PENELOPE`, `NICK` ou `JULIE`.

Já o operador `BETWEEN` é usado para buscar registros que estão dentro de um intervalo específico. Por exemplo, se quisermos buscar todos os filmes que foram lançados entre 2005 e 2007, podemos fazer isso com a seguinte consulta:

```sql
SELECT * FROM sakila.film
    WHERE release_year BETWEEN 2005 AND 2007;
```

# Manipulando os dados e as tabelas.
Talvez um dos termos mais utilizados no mundo de banco de dados seja o CRUD. Esse termo é um acrônimo que representa as quatro operações básicas que podemos realizar em um banco de dados: **Create**, **Read**, **Update** e **Delete**. Essas operações nos permitem manipular os dados armazenados em nossas tabelas.

## Removendo e Restaurando o Banco de Dados
Nesse ponto, precisaremos ser capazes de apagar e restaurar o banco de dados, para ter mais liberdade para aprendermos os próximos comandos. Utilizando o `Workbench`, podemos fazer isso clicando com o botão direito do mouse no banco de dados e selecionando a opção `Drop Schema`. Isso irá apagar o banco de dados, e você poderá criar um novo banco de dados com o mesmo nome. Caso esteja utilizando o `MySQL` pelo terminal, você pode fazer isso com os seguintes comandos:

```sql
DROP SCHEMA sakila;
```

E em seguida, recuperando o arquivo que usamos na aula anterior: [Backup Sakila](../database_backup/sakila.sql). Abrindo-o no `Workbench` e executando o script.

## `INSERT` - Inserindo dados em tabelas
O comando `INSERT` é usado para adicionar novos registros a uma tabela. Ele nos permite inserir dados em uma ou mais colunas de uma tabela.
A sintaxe básica do comando `INSERT` é a seguinte:

```sql
INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3)
VALUES (valor1, valor2, valor3);
```
Por exemplo, se quisermos adicionar um novo ator ao banco de dados, podemos fazer isso com a seguinte consulta:

```sql
INSERT INTO sakila.actor (first_name, last_name)
VALUES ('REBECCA', 'FERGUSON');
```

Essa consulta irá adicionar um novo ator com o primeiro nome `REBECCA` e o sobrenome `FERGUSON` à tabela `actor`.

### Inserindo dados em várias colunas
Podemos inserir dados em várias colunas de uma tabela ao mesmo tempo. Para isso, basta listar as colunas que queremos inserir os dados e os valores correspondentes na mesma ordem.
Por exemplo, se quisermos adicionar um novo filme ao banco de dados, podemos fazer isso com a seguinte consulta:

```sql
INSERT INTO sakila.actor (first_name, last_name)
    VALUES ('JOSH', 'BROLIN')
    , ('JAVIER', 'BARDEN');
```

### `INSERT SELECT` (Inserindo dados de outra tabela)
O comando `INSERT SELECT` é usado para inserir dados de uma tabela em outra tabela. Ele nos permite copiar dados de uma tabela para outra, com base em uma consulta.

A sintaxe básica do comando `INSERT SELECT` é a seguinte:

```sql
INSERT INTO nome_da_tabela_destino (coluna1, coluna2, coluna3)
SELECT coluna1, coluna2, coluna3
FROM nome_da_tabela_origem
WHERE condicao;
```

Por exemplo, se quisermos copiar funcionários da tabela `staff` para a tabela `actor`, podemos fazer isso com a seguinte consulta:

```sql
INSERT INTO sakila.actor (first_name, last_name)
    SELECT ST.first_name, ST.last_name
    FROM sakila.staff AS ST
    LIMIT 2;
```

## `UPDATE` - Atualizando dados em tabelas
O comando `UPDATE` é usado para modificar os dados existentes em uma tabela. Ele nos permite atualizar os valores de uma ou mais colunas de um registro específico.
A sintaxe básica do comando `UPDATE` é a seguinte:

```sql
UPDATE nome_da_tabela
SET coluna1 = valor1, coluna2 = valor2
WHERE condicao;
```
Por exemplo, se quisermos atualizar o sobrenome de um ator específico, podemos fazer isso com a seguinte consulta:

```sql
UPDATE sakila.actor
SET first_name = 'EDWARD'
WHERE first_name = 'ED';
```

O problema aqui é que, por padrão, o **MySQL Server** não vai permitir que façamos essa operação. Existe uma configuração chamada **safe updates mode** que só permite operações de `UPDATE` e `DELETE` onde a condição do `WHERE` inclua o `id` da tabela.

<details>
<summary>Como desativar o safe updates mode</summary>

Para desativar essa configuração, podemos executar o seguinte comando:

```sql
SET SQL_SAFE_UPDATES = 0;
```

Mas, atenção! Essa configuração é importante para evitar que você atualize ou delete dados acidentalmente. Portanto, sempre que for fazer uma operação de `UPDATE` ou `DELETE`, verifique se a condição do `WHERE` está correta e se você realmente deseja fazer essa operação.
Para reativar essa configuração, basta executar o seguinte comando:

```sql
SET SQL_SAFE_UPDATES = 1;
```

</details>
<br/>
Vamos então fazer uma atualização segura, utilizando o `id` do ator:

```sql
UPDATE sakila.actor
SET first_name = 'EDWARD'
WHERE actor_id = 3;
```
Essa consulta irá atualizar o primeiro nome do ator com `actor_id = 3` para `EDWARD`.

### Atualizando dados em várias colunas
Podemos atualizar dados em várias colunas de uma tabela ao mesmo tempo. Para isso, basta listar as colunas que queremos atualizar e os novos valores correspondentes.
Por exemplo, se quisermos atualizar o primeiro e o último nome de um ator específico, podemos fazer isso com a seguinte consulta:

```sql
UPDATE sakila.actor
SET first_name = 'OSCAR', last_name = 'ISAAC'
WHERE actor_id = 2;
```

### `UPDATE` em massa
Por questões de performance, para que apenas uma solicitação de _query_ seja enviada ao servidor, podemos fazer uma atualização em massa.

```sql
UPDATE sakila.actor
SET first_name = (
CASE actor_id WHEN 1 THEN 'JOE'
              WHEN 2 THEN 'DAVIS'
              WHEN 3 THEN 'CAROLINE'
            ELSE first_name
END);
```

Mais informações sobre como usar o `CASE`, [nesse link](https://www.w3schools.com/sql/func_mysql_case.asp).

## `DELETE` - Apagando dados em tabelas
Antes de aprendermos a excluir dados de uma tabela, vale ressaltar que nem sempre que você clica em excluir, dentro de um sistema ou site, a informação terá sido **de fato** excluída do banco de dados. Em muitos casos, a funcionalidade de **"excluir"** apenas marcará a informação como inativa ou excluída, ou algum campo equivalente.

Isso ocorre pela necessidade de seguir normas ou regulamentos sobre disponibilidade, segurança e integridade de dados. Relatórios podem necessitar de informações que já foram "excluídas" ou pode ser necessário manter logs de uso (históricos de acontecimentos no sistema) de seu software.

## Excluindo dados de uma tabela
Para excluir dados de forma básica, temos a seguinte sintaxe:

```sql
DELETE FROM nome_da_tabela
WHERE condicao;
-- o WHERE é "opcional". Porém, sem ele, todas as linhas da tabela seriam excluídas.
```

Exemplo utilizando nosso banco `sakila`:

> Lembre de desativar o `safe updates mode` antes de executar esse comando.

```sql
DELETE FROM sakila.film_text
WHERE title = 'ACADEMY DINOSAUR';
```

Essa consulta irá excluir todos os registros da tabela `film_text` que possuem o título `ACADEMY DINOSAUR`.

### "Meu `DELETE` não foi permitido"
Caso haja relações entre tabelas (**primary key** e **foreign key**) e existam restrições aplicadas a elas, ao executar o `DELETE` ocorrerá uma ação de acordo com a restrição que tiver sido imposta na criação da **foreign key**. Essas restrições podem ser:

```sql
-- Rejeita o comando DELETE.
ON DELETE NO ACTION;

-- Rejeita o comando DELETE.
ON DELETE RESTRICT;

-- Permite a exclusão dos registros da tabela pai, e seta para NULL os registros da tabela filho.
ON DELETE SET NULL;

-- Exclui a informação da tabela pai e registros relacionados.
ON DELETE CASCADE;
```

Analisando um exemplo prático. Caso tentemos executar o seguinte comando:

```sql
DELETE FROM sakila.actor
WHERE first_name = 'GRACE';
```

O **MySQL** irá retornar o seguinte erro:

```
Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`sakila`.`film_actor`, CONSTRAINT `fk_film_actor_actor` FOREIGN KEY (`actor_id`) REFERENCES `actor` (`actor_id`) ON DELETE RESTRICT ON UPDATE CASCADE)
```

# Outras Funções Comuns no SQL
Como nosso objetivo aqui é demonstar apenas o básico de SQL, para que possamos utilizar o **ORM** mais na frente, entendendo o que está sendo feito, vou mencionar apenas por cima as funções mais comuns que podemos utilizar no SQL. Para mais informações, você pode consultar a [documentação oficial do MySQL](https://dev.mysql.com/doc/refman/8.0/en/functions.html).

- `UCASE`: Converte uma string para letras maiúsculas.
- `LCASE`: Converte uma string para letras minúsculas.
- `REPLACE`: Substitui uma substring por outra em uma string.
- `LEFT`: Retorna os primeiros N caracteres de uma string.
- `RIGHT`: Retorna os últimos N caracteres de uma string.
- `CHAR_LENGTH`: Exibe o número de caracteres de uma string.
- `LENGTH`: Exibe o número de bytes de uma string.
- `SUBSTRING`: Retorna uma parte de uma string.
- `IF`: Retorna um valor se uma condição for verdadeira e outro valor se for falsa.
- `CASE`: Avalia uma lista de condições e retorna um valor correspondente à primeira condição verdadeira.
- `DIV`: Realiza uma divisão inteira entre dois números.
- `MOD`: Retorna o resto da divisão entre dois números.
- `CURRENT_DATE`: Retorna a data atual.
- `NOW`: Retorna a data e hora atual.
- `DATEDIFF`: Retorna a diferença entre duas datas.
- `TIMEDIFF`: Retorna a diferença entre duas horas.
- `YEAR`: Retorna o ano de uma data.
- `AVG`: Retorna a média de um conjunto de valores.
- `MIN`: Retorna o menor valor de um conjunto de valores.
- `MAX`: Retorna o maior valor de um conjunto de valores.
- `SUM`: Retorna a soma de um conjunto de valores.
- `COUNT`: Retorna o número de linhas em um conjunto de resultados.

Enfim... A lista é grande, e não tá nem perto de se esgotar. Caso precise, consulte a documentação ou faça uma pesquisa rápida.

## Os temidos `JOINS`
Até agora você deve estar se perguntando: "E onde tá a parte 'relacional' do banco de dados relacional?". É aqui que entram os `JOINS`. É a partir deles que conseguimos recuperar os dados de várias tabelas, combinando-as através de suas chaves primárias e estrangeiras.

Na modelagem de bancos de dados, costumamos aplicar alguns passos para garantir que as tabelas estejam bem estruturadas **normalizadas**. Esse processo consiste em dividir os dados em tabelas menores e mais específicas, de forma a evitar redundâncias e garantir a integridade dos dados. Isso é feito através da criação de relações entre as tabelas, utilizando chaves primárias e estrangeiras. Não abordaremos esse assunto diretamente aqui, mas cabe a leitura adicional do assunto. Você pode encontrar mais [aqui](https://www.alura.com.br/artigos/normalizacao-banco-de-dados-estrutura?srsltid=AfmBOoqMt4Ukyqs7gTZsvZ8OQi6kTtSwpU2I0KsDtUPD6ZlJiDXfFz80).

Por conta disso, é comum vermos tabelas que parecem ter pouca informação, ou que não parecem fazer sentido sozinhas. Vejamos por exemplo a tabela `address` do banco `sakila`. Temos uma coluna chamada `city_id`, que vista isoladamente não nos diz muita coisa. Mas, olhando a modelagem dessa tabela, podemos ver que `city_id` é uma chave estrangeira que se relaciona com a tabela `city`. Sendo assim, podemos executar a seguinte consulta para ver o nome da cidade:

```sql
SELECT * FROM sakila.address AS SA
JOIN sakila.city AS SC ON SC.city_id = SA.city_id;
```

Essa consulta irá retornar todos os registros da tabela `address` e os registros correspondentes da tabela `city`, onde o `city_id` é igual em ambas as tabelas. O resultado será uma tabela com todas as colunas de ambas as tabelas, permitindo que possamos ver o nome da cidade correspondente a cada endereço.

Nessa _query_, apareceu mais um `id`. O `country_id` que é uma chave estrangeira que se relaciona com a tabela `country`. Podemos fazer o mesmo processo para ver o nome do país:

```sql
SELECT SA.address
    , SA.district
    , SC.city
    , CO.country
FROM sakila.address AS SA
INNER JOIN sakila.city AS SC 
    ON SC.city_id = SA.city_id
INNER JOIN sakila.country AS CO 
    ON CO.country_id = SC.country_id;
```

<details>
<summary>Sobre como escolher o tamanho do <i>alias</i></summary>

Sua _query_ é composta de poucas linhas? Então use apenas letras ou a primeira sílaba para representar a coluna. Por exemplo, **"actor"** se tornaria **"A"** ou **"ACT"**.

Caso esteja montando _queries_ com muitas linhas, é recomendado usar um _alias_ mais descritivo para tornar a leitura e interpretação de _query_ mais simples.
</details>

### Os diferentes tipos de `JOIN`
Veremos aqui os principais tipos de `JOIN` que podemos utilizar para combinar tabelas.
- `INNER JOIN`: Retorna apenas os registros que possuem correspondência em ambas as tabelas.
- `LEFT JOIN`: Retorna todos os registros da tabela da esquerda e os registros correspondentes da tabela da direita. Se não houver correspondência, os resultados da tabela da direita serão nulos.
- `RIGHT JOIN`: Retorna todos os registros da tabela da direita e os registros correspondentes da tabela da esquerda. Se não houver correspondência, os resultados da tabela da esquerda serão nulos.

### `INNER JOIN`
O `INNER JOIN` é o tipo mais comum de `JOIN`. Ele retorna apenas os registros que possuem correspondência em ambas as tabelas. Se não houver correspondência, o registro não será incluído no resultado.

Podemos fazer uma comparação dos `JOINS` com operações de conjuntos. Sendo assim, podemos pensar no `INNER JOIN` como a interseção entre dois conjuntos. Ou seja, ele retorna apenas os registros que estão presentes em ambos os conjuntos.

![Inner Join](../assets/inner_join.png)

### `LEFT JOIN`
O `LEFT JOIN` retorna todos os registros da tabela da esquerda e os registros correspondentes da tabela da direita. Se não houver correspondência, os resultados da tabela da direita serão nulos.
Podemos pensar no `LEFT JOIN` como a união entre dois conjuntos, onde o conjunto da esquerda é o conjunto principal e o conjunto da direita é o conjunto secundário. Ou seja, ele retorna todos os registros do conjunto da esquerda e apenas os registros correspondentes do conjunto da direita.

![Left Join](../assets/left_join.png)

### `RIGHT JOIN`
O `RIGHT JOIN` é o oposto do `LEFT JOIN`. Ele retorna todos os registros da tabela da direita e os registros correspondentes da tabela da esquerda. Se não houver correspondência, os resultados da tabela da esquerda serão nulos.
Podemos pensar no `RIGHT JOIN` como a união entre dois conjuntos, onde o conjunto da direita é o conjunto principal e o conjunto da esquerda é o conjunto secundário. Ou seja, ele retorna todos os registros do conjunto da direita e apenas os registros correspondentes do conjunto da esquerda.

![Right Join](../assets/right_join.png)

### Comparando os três:

Vamos visualizar a diferença entre os três joins já vistos até o momento. Rode e analise cada uma das três queries a seguir. Busque notar a diferença entre as colunas da direita e da esquerda e a quantidade de dados retornados em cada query. Gaste de dois a cinco minutos aqui e depois continue.

`LEFT JOIN`

```sql
SELECT C.customer_id
    , C.first_name
    , C.last_name
    , A.actor_id
    , A.first_name
    , A.last_name
FROM sakila.customer AS C
LEFT JOIN sakila.actor AS A
ON C.last_name = A.last_name
ORDER BY C.last_name;
```

`RIGHT JOIN`
```sql
SELECT C.customer_id
    , C.first_name
    , C.last_name
    , A.actor_id
    , A.first_name
    , A.last_name
FROM sakila.customer AS C
RIGHT JOIN sakila.actor AS A
ON C.last_name = A.last_name
ORDER BY C.last_name;
```

`INNER JOIN`

```sql
SELECT C.customer_id
    , C.first_name
    , C.last_name
    , A.actor_id
    , A.first_name
    , A.last_name
FROM sakila.customer AS C
INNER JOIN sakila.actor AS A
ON C.last_name = A.last_name
ORDER BY C.last_name;
```

# Recursos Adicionais
- [Como utilizar `INNER JOIN`, `LEFT JOIN` e `RIGHT JOIN` por Dev Media](https://www.devmedia.com.br/clausulas-inner-join-left-join-e-right-join-no-sql-server/18930)
- [MySQL Tutorial - `INNER JOIN`](https://www.mysqltutorial.org/mysql-basics/mysql-inner-join/)
- [Exercícios de `INNER JOIN` por SQLBolt](https://sqlbolt.com/lesson/select_queries_with_joins)
- [Normalização em Bancos de Dados - Medium](https://medium.com/@diegobmachado/normaliza%C3%A7%C3%A3o-em-banco-de-dados-5647cdf84a12)
- [Normalização de dados](https://www.luis.blog.br/normalizacao-de-dados-e-as-formas-normais.html)
