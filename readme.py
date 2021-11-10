from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(
    ":blush: [link=https://github.com/Kyle-f-r]kyle ramos",
    guide_style="bold bright_black",
)
online_tree = tree.add(":wave: hey, i'm kyle", guide_style="bright_black")
online_tree.add(
    "[bold link=https://github.com/Kyle-f-r]ramos.io[/]              - [bright_black]resume and professional statement"
)
online_tree.add(
    "[bold link=https://https://www.linkedin.com/in/kyle-ramos-339625126?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BZa2HExBwRy%2BVw73mcaiGcw%3D%3D]linkedin/kyle-ramos[/]   - [bright_black]personal linkedin page"
)

python_tree = tree.add(":seedling: Projects and Interests", guide_style="bright_black")
python_tree.add(
    "[bold link=https://github.com/Kyle-f-r]condition-monitoring[/]  - [bright_black]anomoly detection for MOCVD reactors"
)
python_tree.add(
    "[bold link=https://github.com/Kyle-f-r]emissions[/]             - [bright_black]studying time-series forecasting methods"
)
python_tree.add(
    "[bold link=https://github.com/Kyle-f-r]prodeus.app[/]           - [bright_black]user machine learning"
)
python_tree.add(
    "[bold link=https://github.com/Kyle-f-r]paintings.me[/]          - [bright_black]personal painting studies"
)


console.print(tree)
console.print("")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html(
    "c:/Users/Kyle/Kyle-f-r/README.md",
    inline_styles=True,
    code_format=CONSOLE_HTML_FORMAT,
)
