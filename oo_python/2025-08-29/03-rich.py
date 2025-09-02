from rich.console import Console
from rich.table import Table
console = Console()
console.print("[bold green]Sucesso![/] [red]Erro![/]")
table = Table(title='Tarefas')
table.add_column('ID', justify='right')
table.add_column('Nome')
table.add_column('Concluída')
table.add_row('1', 'Aprender Python', '✅')
table.add_row('2', 'Passar na cadeira', '❌')
console.print(table)