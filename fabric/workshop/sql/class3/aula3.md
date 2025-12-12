# Databases - ORM
Agora que já entendemos a estrutura básica de um banco de dados, e como se parece uma _query_ de consulta ou alteração, vamos facilitar um pouco esse processo. Para isso, vamos utilizar um ORM (_Object Relational Mapper_, ou Mapeamento Objeto-Relacional). 

## O que você vai aprender?
- Como utilizar o `SQLAlchemy` para criar uma conexão com o banco de dados.
- Como utilizar o `ORM` do `SQLAlchemy` para criar _queries_ de consulta e alteração.

## O que é `ORM`?
O Mapeamento Objeto-Relacional (**ORM**) é uma técnica que permite fazer um mapeamento estrutural entre as entidades do banco de dados e os objetos que as representam no código. No nosso caso, código `Python`. O mapeamento abstrai as diferenças entre os dois paradigmas, da aplicação e do banco de dados, permitindo que o desenvolvedor trabalhe com objetos em vez de escrever consultas SQL diretamente. Isso facilita a manipulação dos dados e melhora a legibilidade do código.

No Python, a biblioteca mais utilizada para esse fim é o `SQLAlchemy`. Esse pacote, além de um ORM, também é um _SQL toolkit_ que fornece uma interface de alto nível para trabalhar com bancos de dados relacionais. Ele permite criar e executar consultas SQL de forma programática, além de fornecer suporte a transações, gerenciamento de conexões e muito mais. Aqui, vamos focar apenas no uso básico da biblioteca, para que quando vocês forem interagir com os projetos aqui da Residência, vocês tenham uma noção inicial do que está acontecendo.

## PRÁTICA: `SQLAlchemy`
### Apresentação Rápida: `SQLite`
O `SQLite` é um banco de dados relacional leve, integrado ao Python, que armazena os dados em um único arquivo. Para o que vamos desenvolver aqui, é mais do que suficiente. A sintaxe SQL do `SQLite` é semelhante à de outros bancos de dados relacionais, como o `PostgreSQL` e o `MySQL`, então, não teremos problemas em migrar para esses bancos depois.

Além disso, já que utilizaremos o `SQLAlchemy`, nossas _queries_ serão escritas em Python, e não em SQL. Então, mesmo que o `SQLite` tenha algumas diferenças de sintaxe, não teremos problemas e não precisaremos reescrever as _queries_.

### Iniciando um novo projeto
Vamos criar um mini projeto que vai utilizar o `SQLAlchemy` para interagir com o banco de dados. Para isso, vamos criar uma pasta chamada `workshop_database` e dentro dela vamos definir a estrutura do nosso projeto.

<details>
<summary>Lembre de criar um ambiente virtual</summary>

Para criar um ambiente virtual com o `venv`, execute o seguinte comando:
```bash
# Criando o ambiente virtual
python3 -m venv venv
```
Depois, para ativar o ambiente virtual, execute o seguinte comando:
```bash
# Ativando o ambiente virtual
source venv/bin/activate
```
</details>

### Instalando o `SQLAlchemy`
Agora que já temos nosso ambiente virtual ativado, vamos instalar o `SQLAlchemy`. Para isso, execute o seguinte comando:
```bash
# Instalando o SQLAlchemy
pip install sqlalchemy
```

### Camada de conexão ao banco de dados
Agora que já temos o `SQLAlchemy` instalado, vamos criar uma `engine` de conexão com o banco de dados. A `Engine` do `SQLAlchemy` é o ponto de contato com o banco de dados, estabelecendo e gerenciando as conexões. Ela é instanciada através da função `create_engine()`, que recebe as credenciais do banco de dados, o endereço de conexão (URI) e configura o pool de conexões.

De forma geral, podemos definir a interação do `SQLAlchemy` com o projeto da seguinte forma:
![Dunossauro - FastAPI do Zero - SQLAlchemy scheme](../assets/dunossauro-sqlalchemy.png)
> _Fonte: [Dunossauro - Curso de FastAPI do Zero - Aula 4 - Configurando o Banco de Dados e gerenciando migrações com Alembic](https://fastapidozero.dunossauro.com/04/)_

> "Neste diagrama, vemos a relação completa entre a aplicação Python e o banco de dados. A conexão é estabelecida através do SQLAlchemy ORM, que fornece uma Session para interagir com os modelos. Esses modelos são mapeados para as tabelas no banco de dados, enquanto a Engine se conecta com o banco de dados e depende de Metadata para manter as informações das tabelas."

Vamos seguir a seguinte estrutura no nosso projeto:
```bash
├── workshop_database
│   ├── __init__.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── connection
│   │   │   ├── __init__.py
│   │   │   └── connection.py
│   │   ├── model
│   │   │   ├── __init__.py
│   │   │   ├── ... (nossos modelos)
│   │   └── dao
│   │       ├── __init__.py
│   │       ├── ... (Data Access Object Layer)
│   ├── main.py
README.md
```

Vamos criar a pasta `database` dentro da pasta `movie_rental_app`, e dentro dela, vamos criar as pastas `connection`, `models` e `dao`. A pasta `connection` vai conter o arquivo `connection.py`, que vai ser responsável por criar a conexão com o banco de dados. A pasta `models` vai conter os modelos do banco de dados, e a pasta `dao` vai conter a camada de acesso aos dados.
Agora, vamos criar o arquivo `connection.py` dentro da pasta `connection` e adicionar o seguinte código:

```python
# workshop_database/database/connection/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(
    'sqlite:///./workshop_database.db',  # URI de conexão com o banco de dados
)


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session() -> Session:
    return SessionLocal()
```

Temos algumas coisas novas aqui, então vamos explicar o que está acontecendo.
- `create_engine`: Essa função cria uma `engine` de conexão com o banco de dados. O parâmetro que passamos é a URI de conexão com o banco de dados. No nosso caso, estamos utilizando o `SQLite`, então a URI é `sqlite:///./wt4_rental.db`. O `./` indica que o arquivo do banco de dados vai ser criado na pasta atual.
- `Session`: Essa classe representa uma sessão de interação com o banco de dados. Ela é responsável por gerenciar as transações e as operações de CRUD (Create, Read, Update, Delete) no banco de dados.
- `sessionmaker`: uma fábrica de sessões — retorna objetos Session já configurados.
- `bind=engine` conecta essa sessão ao engine, ou seja, toda vez que você abrir uma sessão, ela estará usando esse banco (wt4_rental.db).
- `autoflush=False` evita que mudanças pendentes no objeto Python sejam automaticamente enviadas ao banco toda vez que você fizer uma query. Você controla manualmente quando isso deve acontecer (normalmente com session.flush() ou session.commit()).
- `autocommit=False`: significa que as operações não são salvas automaticamente no banco. Você precisa dar session.commit() para confirmar. Isso é bom porque garante consistência (você pode desfazer com rollback() se algo der errado).
- `get_session`: Quando chamamos a função, ela retorna um objeto `Session`, que podemos usar para interagir com o banco de dados.


### Criando nossas tabelas
Antes de criarmos nossas tabelas propriamente ditas, o `SQLAlchemy` sugere que criemos uma classe `Base`, que vai ser a classe base para todos os nossos modelos. Essa classe vai ser responsável por mapear as tabelas do banco de dados. Para isso, vamos criar um arquivo chamado `base.py` dentro da pasta `models` e adicionar o seguinte código:
```python
# workshop_database/database/model/base.py
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all database models.

    This class serves as the base for all database models in the application.
    It inherits from `DeclarativeBase` to provide
    declarative mapping.
    """

    def as_dict(self):
        """Returns the attributes of the model as a dictionary.
        """

        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }
```


Agora, vamos criar um modelo simples de exemplo, utilizando o banco do [Exercício 2](../database_backup/exa2_dnd.sql).

Primeiro, vamos começar com a tabela de `Players`. Para isso, vamos criar um arquivo chamado `player.py` dentro da pasta `models` e adicionar o seguinte código:
```python
# workshop_database/database/models/player.py
from datetime import datetime

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from workshop_database.database.model.base import Base


class Player(Base):
    """Model representing a player in the game.

    This class defines the structure of the `players` table in the database.
    It inherits from `Base`, which provides the necessary functionality for
    declarative mapping.
    """

    __tablename__ = 'players'  # Name of the table in the database

    player_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )  # Primary key
    player_name: Mapped[str] = mapped_column(String(255))  # Player's name
    email: Mapped[str] = mapped_column(String(100), unique=True)  # Player's email
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )  # Creation timestamp
    characters: Mapped[Optional[List["Character"]]] = relationship(
        back_populates="player")

```

Agora, vamos criar o modelo de `Characters`. Para isso, vamos criar um arquivo chamado `character.py` dentro da pasta `models` e adicionar o seguinte código:
```python
# workshop_database/database/models/character.py
from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from workshop_database.database.model.base import Base
from workshop_database.database.model.player import Player


class Character(Base):
    """Model representing a character in the game.

    This class defines the structure of the `characters` table in the database.
    It inherits from `Base`, which provides the necessary functionality for
    declarative mapping.
    """

    __tablename__ = 'characters'  # Name of the table in the database

    character_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )  # Primary key
    character_name: Mapped[str] = mapped_column(String(255))  # Character's name
    character_class: Mapped[str] = mapped_column(String(255))  # Character's class
    race: Mapped[str] = mapped_column(String(255))  # Character's race
    level: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )  # Character's level
    player_id: Mapped[int] = mapped_column(
        ForeignKey('players.player_id'),
    )  # Foreign key to players table
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )  # Creation timestamp

    player: Mapped["Player"] = relationship(
        back_populates="characters",
    )  # Relationship with Player model

```

### Camada DAO
Com nossos modelos criados, já poderiamos começar a interagir diretamente com o banco de dados. Utilizando do ORM do `SQLAlchemy`, já podemos criar _queries_ semelhantes às que aprendemos em SQL. Mas, pensando em manutenção de código e numa possível migração para outro banco de dados, no projeto de **Fotografia Automatizada**, aqui na Residência, utilizamos a camada DAO (Data Access Object). Para que vocês possam entender o código, caso se deparem com ele, vamos ver um pouco dessa ideia aqui também.

A camada DAO é uma camada de abstração que separa a lógica de acesso aos dados da lógica de negócio da aplicação. Ela fornece uma interface para interagir com o banco de dados, permitindo que a lógica de negócio não precise se preocupar com os detalhes de implementação do acesso aos dados. Isso facilita a manutenção e a evolução do código, além de permitir que possamos trocar o banco de dados sem precisar alterar a lógica de negócio.
Vamos criar a pasta `dao` dentro da pasta `database`, e dentro dela, vamos criar os arquivos `player_dao.py` e `character_dao.py`. Esses arquivos vão conter as classes que vão implementar a camada DAO para os modelos de `Player` e `Character`, respectivamente.

Vamos começar com o arquivo `player_dao.py`:
```python
# workshop_database/database/dao/player_dao.py
from typing import List, Optional

from sqlalchemy import delete, select, update
from sqlalchemy.exc import NoResultFound

from database.connection.connection import get_session
from database.model.player import Player


class PlayerDAO:
    """Data Access Object (DAO) for the Player model.

    This class provides methods to interact with the Player database table.
    It includes methods for creating, reading, updating,
    and deleting player records.
    """

    @staticmethod
    def create(model: Player) -> Player:
        """Creates a new player record in the database.
        Args:
            model (Player): The player model instance to be created.
        Returns:
            Player: The created player model instance.
        """
        session = get_session()
        try:
            session.add(model)
            session.commit()
            session.refresh(model)

            return model
        finally:
            session.close()

    @staticmethod
    def get_one(player_id: int) -> Optional[Player]:
        """Retrieves a player record by its ID.
        Args:
            player_id (int): The ID of the player to retrieve.
        Returns:
            Optional[Player]: The player model instance if found,
                otherwise None.
        """
        session = get_session()
        try:
            stmt = select(Player).where(Player.player_id == player_id)

            db_player = session.scalar(stmt)
            if db_player is None:
                raise NoResultFound(f"Player with ID {player_id} not found.")
            return db_player
        finally:
            session.close()

    @staticmethod
    def get_all() -> List[Player]:
        """Retrieves all player records from the database.
        Returns:
            List[Player]: A list of player model instances.
        """
        session = get_session()
        try:

            stmt = select(Player)

            db_players = session.scalars(stmt).all()
            return db_players
        finally:
            session.close()

    @staticmethod
    def update(model: Player) -> Player:
        """Updates an existing player record in the database.
        Args:
            model (Player): The player model instance to be updated.
        Returns:
            Player: The updated player model instance.
        """
        session = get_session()
        try:

            update_values = model.as_dict()
            del update_values["player_id"]
            stmt = (
                update(Player)
                .where(Player.player_id == model.player_id)
                .values(
                    **update_values,
                )
            )

            session.execute(stmt)
            session.commit()
            session.refresh(model)

            return model
        finally:
            session.close()

    @staticmethod
    def delete(player_id: int) -> None:
        """Deletes a player record from the database by its ID.
        Args:
            player_id (int): The ID of the player to delete.
        """
        session = get_session()
        try:
            stmt = delete(Player).where(Player.player_id == player_id)

            session.execute(stmt)
            session.commit()
        finally:
            session.close()

```

### O que temos de novo aqui?
Da forma como estruturamos nossa camada DAO nesse projeto, não precisamos nos preocupar com os atributos internos dessa classe. Ela é o que chamamos, em Orientação a Objetos, de _static class_, ou Classe Estática. Isso significa que não precisamos instanciar a classe para utilizá-la. Podemos chamar os métodos diretamente da classe, como `PlayerDAO.create()`, por exemplo.

Nossa class `PlayerDAO` implementa os métodos básicos de um CRUD (Create, Read, Update e Delete), que você pode ver que equivalem diretamente às operações em `SQL` que aprendemos na aula passada:
- `create`: Cria um novo registro no banco de dados. Equivalente ao `INSERT` em SQL.
- `get_all`: Um dos nossos **Read**. Recupera todos os registros do banco de dados. Equivalente ao `SELECT` em SQL.
- `get_one`: Um dos nossos **Read**. Recupera um único registro do banco de dados. Equivalente ao `SELECT` com `WHERE` em SQL.
- `update`: Atualiza um registro existente no banco de dados. Equivalente ao `UPDATE` em SQL.
- `delete`: Deleta um registro do banco de dados. Equivalente ao `DELETE` em SQL.

### Mostrando um pouco da sintaxe do `SQLAlchemy`
Se pegarmos como exemplo o método `get_one`, podemos quase ler o código como se fosse uma _query_ SQL. Vamos ver como ficaria a _query_ SQL equivalente:

```python
# workshop_database/database/dao/player_dao.py

stmt = select(Player).where(Player.player_id == player_id)

```

Essa linha de código é equivalente à seguinte _query_ SQL:
```sql
SELECT * FROM players WHERE player_id = player_id;
```

Da mesma forma, podemos ler o método `update` como uma _query_ SQL:
```python
# workshop_database/database/dao/player_dao.py

stmt = (
    update(Player)
    .where(Player.player_id == model.player_id)
    .values(
        **update_values,  # operação de desempacotamento
    )
)
```
Essa linha de código é equivalente à seguinte _query_ SQL:
```sql
UPDATE players
SET player_name = 'new_name', email = 'new_email', created_at = 'new_date'
WHERE player_id = player_id;
```

<details>
<summary><b>Dica: </b>O que é o <code>**</code>?</summary>
O `**` é o operador de desempacotamento de dicionário em Python. Ele permite passar os pares chave-valor de um dicionário como argumentos nomeados para uma função. No caso do `update`, estamos passando os valores do dicionário `update_values` como argumentos nomeados para a função `values()`.
Isso é útil quando queremos passar um número variável de argumentos para uma função, ou quando queremos passar todos os itens de um dicionário como argumentos nomeados.
Por exemplo, se temos um dicionário `kwargs` com os seguintes valores:
```python
kwargs = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
```
Podemos passar esses valores como argumentos nomeados para uma função da seguinte forma:
```python
def print_info(name, age, city):
    print(f'Name: {name}, Age: {age}, City: {city}')
print_info(**kwargs)
# Saída: Name: John, Age: 30, City: New York
```
</details>

### O que fazemos com a `session`?
A `session` é o ponto de contato com o banco de dados. Ela é responsável por gerenciar as transações e as operações de CRUD (Create, Read, Update, Delete) no banco de dados. Quando criamos uma `session`, estamos criando uma conexão com o banco de dados. Essa conexão é utilizada para executar as operações no banco de dados.
Quando chamamos o método `commit()`, estamos confirmando as alterações feitas na `session` e persistindo essas alterações no banco de dados. Se não chamarmos o `commit()`, as alterações não serão salvas no banco de dados. Isso é útil para garantir que as alterações sejam feitas de forma atômica, ou seja, todas as alterações são feitas ou nenhuma delas é feita.
Quando chamamos o método `refresh()`, estamos atualizando o objeto `model` com os dados mais recentes do banco de dados. Isso é útil quando queremos garantir que o objeto esteja atualizado com os dados mais recentes do banco de dados, especialmente após uma operação de `update()`.
Quando chamamos o método `scalar()`, estamos executando a consulta e retornando o primeiro resultado. Se não houver resultados, o método retorna `None`. Isso é útil quando queremos recuperar um único registro do banco de dados.
Quando chamamos o método `scalars()`, estamos executando a consulta e retornando todos os resultados. Isso é útil quando queremos recuperar vários registros do banco de dados.
Quando chamamos o método `execute()`, estamos executando uma consulta SQL no banco de dados. É dessa forma que utilizamos nossos **statements** escritos anteriormente. O `SQLAlchemy` converte esses **statements** em SQL e executa a consulta no banco de dados.

Vale ressaltar que essa é uma versão simplificada da implementação que fazemos com `SQLAlchemy`. Em projetos maiores, utilizamos o `Alembic` para gerenciar as migrações do banco de dados, e o `FastAPI` para criar a API. Além disso, fazemos o tratamento de erros e exceções de forma mais robusta. Mas, para o que precisamos aqui, essa implementação é suficiente.

### Mais um pouco de prática: usando relacionamentos
Agora que já entendemos um pouco de como funciona o `SQLAlchemy`, vamos ver um pouco de como funcionam os relacionamentos entre as tabelas. Vamos criar um arquivo chamado `character_dao.py` dentro da pasta `dao` e adicionar o seguinte código:
```python
# workshop_database/database/dao/character_dao.py
from typing import List, Optional

from sqlalchemy import delete, select, update
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound

from database.connection.connection import get_session
from database.model.character import Character


class CharacterDAO:
    """Data Access Object (DAO) for the Character model.

    This class provides methods to interact with the Character database table.
    It includes methods for creating, reading, updating,
    and deleting character records.
    """

    @staticmethod
    def create(model: Character) -> Character:
        """Creates a new character record in the database.
        Args:
            model (Character): The character model instance to be created.
        Returns:
            Character: The created character model instance.
        """
        session = get_session()
        try:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model
        finally:
            session.close()

    @staticmethod
    def get_one(character_id: int) -> Optional[Character]:
        """Retrieves a character record by its ID.
        Args:
            character_id (int): The ID of the character to retrieve.
        Returns:
            Optional[Character]: The character model instance if found,
                otherwise None.
        """
        session = get_session()
        try:
            stmt = select(Character).where(
                Character.character_id == character_id,
            ).options(
                joinedload(Character.player),
            )
            db_character = session.scalar(stmt)
            if db_character is None:
                raise NoResultFound(f"Character with ID {character_id} "
                                    "not found.")
            return db_character
        finally:
            session.close()

    @staticmethod
    def get_all() -> List[Character]:
        """Retrieves all character records from the database.
        Returns:
            List[Character]: A list of character model instances.
        """
        session = get_session()
        try:
            stmt = select(Character)
            db_characters = session.scalars(stmt).all()
            return db_characters
        finally:
            session.close()

    @staticmethod
    def update(model: Character) -> Character:
        """Updates an existing character record in the database.

        Args:
            model (Character): The character model instance to be updated.

        Returns:
            Character: The updated character model instance.
        """
        session = get_session()
        try:
            update_values = model.as_dict()
            del update_values["character_id"]
            del update_values['player_id']
            stmt = (
                update(Character)
                .where(Character.character_id == model.character_id)
                .values(**update_values)
            )

            session.execute(stmt)
            session.commit()
            return model
        finally:
            session.close()

    @staticmethod
    def delete(character_id: int) -> None:
        """Deletes a character record from the database.
        Args:
            character_id (int): The ID of the character to delete.
        """
        session = get_session()
        try:
            stmt = delete(Character).where(
                Character.character_id == character_id,
            )

            session.execute(stmt)
            session.commit()
        finally:
            session.close()

```

### O que temos de novo aqui?
- `joinedload`: Essa função é utilizada para carregar os relacionamentos de forma antecipada. Isso significa que, quando recuperamos um personagem, também carregamos o jogador associado a ele. Isso evita consultas adicionais ao banco de dados para recuperar os dados do jogador. É o equivalente ao `JOIN` em SQL.
- `options`: Essa função é utilizada para especificar opções adicionais para a consulta. No nosso caso, estamos utilizando o `joinedload` para carregar os relacionamentos de forma antecipada.

# Recursos Adicionais
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [SQLAlchemy ORM Documentation](https://docs.sqlalchemy.org/en/20/orm/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/tutorial.html)
- [Dunossauro: FastAPI do Zero - Aula 4 - Configurando o Banco de Dados e Gerenciando Migrações com Alembic](https://fastapidozero.dunossauro.com/04/)

