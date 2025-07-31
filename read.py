def load_lands():
    try:
        lands = {}
        with open('land.txt', 'r') as file:
            for line in file:
                kitta, city, direction, area, price, status = line.strip().split(', ')
                lands[kitta] = {'city': city, 'direction': direction, 'area': int(area), 'price': int(price), 'status': status}
        return lands
    except FileNotFoundError:
        print("No existing land data found. Starting with an empty dataset.")
        return {}

def save_lands(lands):
    with open('land.txt', 'w') as file:
        for kitta, land in lands.items():
            line = kitta + ", " + land['city'] + ", " + land['direction'] + ", " + str(land['area']) + ", " + str(land['price']) + ", " + land['status']
            file.write(line + '\n')
    print("Land data saved successfully.")
