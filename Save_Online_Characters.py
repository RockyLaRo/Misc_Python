import requests
import json
import time
import logging
import os

# Set up logging
logging.basicConfig(filename='save_characters.log', level=logging.INFO)

# Set the list of worlds to iterate over
worlds = [
    "Adra", "Alumbra", "Antica", "Ardera", "Astera", "Axera", "Bastia",
    "Batabra", "Belobra", "Bombra", "Bona", "Cadebra", "Calmera", "Castela",
    "Celebra", "Celesta", "Collabra", "Damora", "Descubra", "Dibra", "Epoca",
    "Esmera", "Famosa", "Fera", "Ferobra", "Firmera", "Gentebra", "Gladera",
    "Harmonia", "Havera", "Honbra", "Illusera", "Impulsa", "Inabra", "Issobra",
    "Kalibra", "Kardera", "Karna", "Libertabra", "Lobera", "Luminera", "Lutabra",
    "Marbera", "Marcia", "Menera", "Monza", "Mudabra", "Mykera", "Nadora",
    "Nefera", "Nossobra", "Ocebra", "Olima", "Ombra", "Optera", "Ousabra",
    "Pacera", "Peloria", "Premia", "Quelibra", "Quintera", "Refugia",
    "Reinobra", "Seanera", "Secura", "Serdebra", "Solidera", "Suna", "Syrena",
    "Talera", "Tembra", "Thyria", "Trona", "Utobra", "Venebra", "Versa",
    "Visabra", "Vunira", "Wintera", "Wizera", "Xandebra", "Yonabra", "Zenobra",
    "Zuna", "Zunera"
]

while True:
    # Get current time
    start_time = time.perf_counter()

    # Iterate over each world
    for world in worlds:
        # Create a folder for each world if it doesn't already exist
        if not os.path.exists(world):
            os.makedirs(world)

        # Generate file name with timestamp
        file_name = f'{world}/character_names_{time.strftime("%Y-%m-%d-%H-%M-%S")}.txt'

        # Open the file in write mode
        with open(file_name, 'w') as f:
            # Send request to API endpoint
            response = requests.get(f'https://api.tibiadata.com/v3/world/{world}')

            # Check if the request was successful
            if response.status_code != 200:
                # Log an error message
                logging.error(f'Request to {world} failed with status code {response.status_code}')
                continue

            # Parse JSON data
            data = response.json()

            # Check if the data contains character names
            if 'worlds' not in data or 'world' not in data['worlds'] or 'online_players' not in data['worlds']['world'] or data['worlds']['world']['online_players'] is None:
                # Log an error message
                logging.error(f'No character names found for {world}')
                continue

            # Extract character names from JSON data
            character_names = [character['name'] for character in data['worlds']['world']['online_players']]

            # Write all names to file
            for name in character_names:
                f.write(name + '\n')

            # Log time taken to save character names for this world
            elapsed_time = time.perf_counter() - start_time
            logging.info(f'{world} took {elapsed_time:.2f} secs to save {len(character_names)} characters on {time.ctime()}')

    # Pause for 5 minutes before running again
    time.sleep(300)
