def favorite_bond(year_born):
    bond_actors = {
        1973: "Roger Moore",
        1987: "Timothy Dalton",
        1995: "Pierce Brosnan",
        2006: "Daniel Craig"
    }

    for year, actor in sorted(bond_actors.items(), reverse=True):
        if year <= year_born:
            return f"Your favorite James Bond actor is {actor}."

    return "Sorry, we couldn't determine your favorite James Bond actor."

# Example usage:
birth_year = 1990
print(favorite_bond(birth_year))

