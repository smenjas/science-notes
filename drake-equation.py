# The Drake equation estimates how many civilizations we can detect in our
# galaxy.
#
# https://en.wikipedia.org/wiki/Drake_equation
# https://en.wikipedia.org/wiki/Fermi_paradox
# https://en.wikipedia.org/wiki/Rare_Earth_hypothesis

def drake_equation(
    new_star_rate,
    ratio_of_stars_with_planets,
    ratio_of_habitable_planets,
    ratio_of_planets_that_develop_life,
    ratio_of_planets_that_develop_civilization,
    ratio_of_detectable_civilizations,
    how_long_civilizations_are_detectable):
    '''Returns the number of detectable civilizations in our galaxy.'''

    return (new_star_rate
        * ratio_of_stars_with_planets
        * ratio_of_habitable_planets
        * ratio_of_planets_that_develop_life
        * ratio_of_planets_that_develop_civilization
        * ratio_of_detectable_civilizations
        * how_long_civilizations_are_detectable)


# The minimum estimates provided by Drake et al. in 1961:
n_civ_1961_min = drake_equation(
    new_star_rate = 1, # new stars per year
    ratio_of_stars_with_planets = 0.2,
    ratio_of_habitable_planets = 1,
    ratio_of_planets_that_develop_life = 1,
    ratio_of_planets_that_develop_civilization = 1,
    ratio_of_detectable_civilizations = 0.1,
    how_long_civilizations_are_detectable = 1e3)

# The maximum estimates provided by Drake et al. in 1961:
n_civ_1961_max = drake_equation(
    new_star_rate = 1, # new stars per year
    ratio_of_stars_with_planets = 0.5,
    ratio_of_habitable_planets = 5,
    ratio_of_planets_that_develop_life = 1,
    ratio_of_planets_that_develop_civilization = 1,
    ratio_of_detectable_civilizations = 0.2,
    how_long_civilizations_are_detectable = 1e8)

print(f"Minimum civilizations, 1961 estimate: {n_civ_1961_min:.0e}")
print(f"Maximum civilizations, 1961 estimate: {n_civ_1961_max:.0e}")

# The minimum modern estimates:
n_civ_2020_min = drake_equation(
    new_star_rate = 1.5, # new stars per year
    ratio_of_stars_with_planets = 1,
    ratio_of_habitable_planets = 1e-3,
    ratio_of_planets_that_develop_life = 1e-2,
    ratio_of_planets_that_develop_civilization = 1e-9,
    ratio_of_detectable_civilizations = 0.1,
    how_long_civilizations_are_detectable = 304) # in years

# The maximum modern estimates:
n_civ_2020_max = drake_equation(
    new_star_rate = 3, # new stars per year
    ratio_of_stars_with_planets = 1,
    ratio_of_habitable_planets = 0.2,
    ratio_of_planets_that_develop_life = 0.13,
    ratio_of_planets_that_develop_civilization = 1,
    ratio_of_detectable_civilizations = 0.2,
    how_long_civilizations_are_detectable = 1e9) # in years

print(f"Minimum civilizations, 2020 estimate: {n_civ_2020_min:.0e}")
print(f"Maximum civilizations, 2020 estimate: {n_civ_2020_max:.0e}")

odds_of_universal_uniqueness = 2.5e-24
odds_of_galactic_uniqueness = 1.7e-11

print(f"Odds that Earth is universally unique: {odds_of_universal_uniqueness:.1e}")
print(f"Odds that Earth is galactically unique: {odds_of_galactic_uniqueness:.1e}")
