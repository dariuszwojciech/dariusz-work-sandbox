import os

from jinja2 import Environment, FileSystemLoader

from incubator.common_utils import create_folder

environment = Environment(loader=FileSystemLoader(r"templates/"))

gen_folder = "../_gen_/"

create_folder(gen_folder)

template = environment.get_template("demo_template.j2t")

filename = f"{gen_folder}generated_file.md"

content = template.render(
    header="Days of the Week",
    days_of_week=["Monday", "Tuesday", "Wednesday", "Friday"],
    team_members=["Alice", "Bob", "Carol", "Dan", "Eve"],
    date="20230609",
    things_to_remember=[
        "black - use it",
        "KISS",
        "More examples in the future",
        "Thanks for your time!",
    ],
)

with open(filename, mode="w", encoding="utf-8") as my_markdown_file:
    my_markdown_file.write(content)
    print(f"... saved {filename}")
