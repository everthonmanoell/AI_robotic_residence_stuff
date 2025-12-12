# Exercícios Aula 2
Para os exercícios da aula 2, utilize o banco de dados no arquivo [`exa2_dnd.sql`](../database_backup/exa2_dnd.sql).

**[Questão 1.]** Encontre todos os personagens e seus jogadores. Exiba o nome do personagem associado ao nome do jogador em uma coluna chamada `Character` com o formato `Personagem (Jogador)`. E as colunas `Class`, `Race` e `Level`.
Ex.: 

| Character | Class | Race | Level |
| --------- | ----- | ---- | ----- |
| Tharion (Alice)| Wizard | Elf | 5 |

**[Questao 2.]**  Liste todas as campanhas e os personagens participantes. Exiba as seguintes colunas: `Character` (que representa o nome do personagem), `Class`, `Level`, `Adventure`(que representa o nome da campanha) e a string "DM `dungeon_master`".
Ex.:

| Character | Class | Level | Adventure | DM |
| --------- | ----- | ----- | --------- | -- |
| Tharion | Wizard | 5 | The Lost Mines | DM Alice |

**[Questão 3.]** Encontre todos os itens com o tipo `Weapon` ou a raridade `Legendary`

**[Questão 4.]** Encontre todos os itens cujo nome seja `Ring`.

**[Questão 5.]** Adicione novos monstros com as seguintes informações:
```json
{
    "monster_name": "Goblin",
    "monster_type": "humanoid",
    "hit_points": 12,
    "challenge_rating": 1,
    "description": "A small and cruel creature, often found in caves and forests."
},
{
    "monster_name": "Dragon",
    "monster_type": "dragon",
    "hit_points": 200,
    "challenge_rating": 10,
    "description": "A large and powerful creature, often hoarding treasure."
}
{
    "monster_name": "Giant",
    "monster_type": "giant",
    "hit_points": 150,
    "challenge_rating": 7,
    "description": "A massive creature, often found in mountains and hills."
}
```
**[Questão 6.]** O personagem **Drex** acabou de passar de nível, e agora é nível 3. Altere seu valor na tabela.

**[Questão 7.]** Na última luta, a personagem **Luna** perdeu seu **Ring of Invisibility**. Exclua essa relação da tabela `Character_Items`.