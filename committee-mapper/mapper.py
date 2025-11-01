# committee-mapper/mapper.py
import requests
from bs4 import BeautifulSoup
import json

def get_team(url):
    print(f"Scraping {url}...")
    # NOTE: LinkedIn blocks scrapers. Use manually for now.
    print("FOR MVP: Paste 3 decision-makers below")
    people = []
    for i in range(3):
        name = input(f"Name {i+1}: ")
        role = input(f"Role {i+1}: ")
        people.append({"name": name, "role": role})
    return people

# Run
if __name__ == "__main__":
    url = input("LinkedIn Company URL: ")
    team = get_team(url)
    print("\n--- BUYING COMMITTEE ---")
    for p in team:
        print(f"{p['name']} – {p['role']}")
    # Save
    with open("committee.json", "w") as f:
        json.dump(team, f, indent=2)
    print("\nSaved to committee.json")
