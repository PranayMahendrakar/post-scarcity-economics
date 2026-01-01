#!/usr/bin/env python3
"""Post-Scarcity Economic Simulator - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import *

console = Console()

def main():
    console.print(Panel("💎 POST-SCARCITY ECONOMIC SIMULATOR 💎\nModeling Abundance Economics", style="bold magenta"))
    mods = [("Abundance Modeling", AbundanceModeler()), ("Resource Allocation", ResourceAllocator()),
            ("Value Redefinition", ValueRedefiner()), ("Work Transformation", WorkTransformer()),
            ("Motivation Analysis", MotivationAnalyzer()), ("Distribution Design", DistributionDesigner()),
            ("Governance Modeling", GovernanceModeler()), ("Transition Planning", TransitionPlanner()),
            ("Social Dynamics", SocialDynamicsEngine()), ("Economic Synthesis", EconomicSynthesizer())]
    while True:
        table = Table(title="Economic Modules")
        for i,(n,_) in enumerate(mods,1): table.add_row(str(i),n)
        table.add_row("0","Exit")
        console.print(table)
        c = Prompt.ask("Select", choices=[str(i) for i in range(len(mods)+1)])
        if c == "0": break
        scenario = Prompt.ask("Economic scenario")
        result = mods[int(c)-1][1].model(scenario)
        console.print(Panel(Markdown(result), title=mods[int(c)-1][0], border_style="magenta"))

if __name__ == "__main__": main()
