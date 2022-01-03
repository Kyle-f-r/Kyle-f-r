from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(
    ":blush: [link=https://github.com/Kyle-f-r]kyle ramos",
    guide_style="bold bright_black",
)
online_tree = tree.add(":wave: hey, i'm kyle", guide_style="bright_black")
online_tree.add(
    "[bold link=https://kyleramosdesign.com]kyleramosdesign.com[/]         - [bright_black]personal website"
)
online_tree.add(
    "[bold link=https://www.linkedin.com/in/kyle-ramos-339625126/]linkedin/kyle-ramos [/]        - [bright_black]personal linkedin page"
)


python_tree = tree.add(":seedling: Projects and Interests", guide_style="bright_black")
python_tree.add(
    "[bold link=https://github.com/Kyle-f-r/Conditional-Monitoring]PCA and Mahalanobis Dist.[/]   - [bright_black]anomoly detection for MOCVD reactors"
)
python_tree.add(
    "[bold link=https://www.kyleramosdesign.com/ideo-nike]Nike Grind Challenge[/]        - [bright_black]sustainable bike lane divider"
)

python_tree = tree.add(":microscope: Coursework", guide_style="bright_black")
python_tree.add(
    "[bold link=https://github.com/Kyle-f-r/Time-Series-Carbon-Emission-Forecasting]Time-Series SARIMAX Model[/]   - [bright_black]forcasting U.S. co2 emissions"
)
python_tree.add(
    "[bold link=https://github.com/Kyle-f-r/Loan-Eligibility-Prediction]Random Forest Classifier [/]   - [bright_black]loan eligibility classifier"
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
