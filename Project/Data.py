capitals = {  # Capital,        State,            Latitude, Longitude
    "AL": ["Montgomery",     "Alabama",        32.3792, -86.3077],
    "AR": ["Little Rock",    "Arkansas",       34.7465, -92.2896],
    "AZ": ["Pheonix",        "Arizona",        33.4484, -112.0740],
    "CA": ["Sacramento",     "California",     38.5816, -121.4944],
    "CO": ["Denver",         "Colorado",       39.7392, -104.9903],
    "CT": ["Hartford",       "Connecticut",    41.7658, -72.6734],
    "DC": ["Washington",     "DC",             38.9072, -77.0369],
    "DE": ["Dover",          "Delaware",       39.1582, -75.5244],
    "FL": ["Tallahassee",    "Florida",        30.4383, -84.2807],
    "GA": ["Atlanta",        "Georgia",        33.7490, -84.3880],
    "IA": ["Des Moines",     "Iowa",           41.5868, -93.6250],
    "ID": ["Boise",          "Idaho",          43.6150, -116.2023],
    "IL": ["Springfield",    "Illinois",       39.7817, -89.6501],
    "IN": ["Indianapolis",   "Indiana",        39.7684, -86.1581],
    "KS": ["Topeka",         "Kansas",         39.0473, -95.6752],
    "KY": ["Frankfort",      "Kentucky",       38.2009, -84.8733],
    "LA": ["Baton Rouge",    "Louisiana",      30.4515, -91.1871],
    "MA": ["Boston",         "Massachusetts",  42.3601, -71.0589],
    "MD": ["Annapolis",      "Maryland",       38.9784, -76.4922],
    "ME": ["Augusta",        "Maine",          44.3106, -69.7795],
    "MI": ["Lansing",        "Michigan",       42.7325, -84.5555],
    "MN": ["St. Paul",       "Minnesota",      44.9537, -93.0900],
    "MO": ["Jefferson City", "Missouri",       38.5767, -92.1735],
    "MS": ["Jackson",        "Mississippi",    32.2988, -90.1848],
    "MT": ["Helena",         "Montana",        46.5891, -112.0391],
    "NC": ["Raleigh",        "North Carolina", 35.7796, -78.6382],
    "ND": ["Bismarck",       "North Dakota",   46.8083, -100.7837],
    "NE": ["Lincoln",        "Nebraska",       40.8136, -96.7026],
    "NH": ["Concord",        "New Hampshire",  43.2081, -71.5376],
    "NJ": ["Trenton",        "New Jersey",     40.2206, -74.7597],
    "NM": ["Santa Fe",       "New Mexico",     35.6870, -105.9378],
    "NV": ["Carson City",    "Nevada",         39.1638, -119.7674],
    "NY": ["Albany",         "New York",       42.6526, -73.7562],
    "OH": ["Columbus",       "Ohio",           39.9612, -82.9988],
    "OK": ["Oklahoma City",  "Oklahoma",       35.4676, -97.5164],
    "OR": ["Salem",          "Oregon",         44.9429, -123.0351],
    "PA": ["Harrisburg",     "Pennsylvania",   40.2732, -76.8867],
    "RI": ["Providence",     "Rhode Island",   41.8240, -71.4128],
    "SC": ["Columbia",       "South Carolina", 34.0007, -81.0348],
    "SD": ["Pierre",         "South Dakota",   44.3668, -100.3538],
    "TN": ["Nashville",      "Tennesee",       36.1627, -86.7816],
    "TX": ["Austin",         "Texas",          30.2672, -97.7431],
    "UT": ["Salt Lake City", "Utah",           40.7608, -111.8910],
    "VA": ["Richmond",       "Virginia",       37.5407, -77.4360],
    "VT": ["Montpelier",     "Vermont",        44.2601, -72.5754],
    "WA": ["Olympia",        "Washington",     47.0379, -122.9007],
    "WI": ["Madison",        "Wisconsin",      43.0722, -89.4008],
    "WY": ["Cheyenne",       "Wyoming",        32.7765, -79.9311],
    "WV": ["Charleston",     "West Virginia",  38.3498, -81.6326]
}


likely_routes = {
    "NY": {
        "MA": [170, "I-90"],
        "PA": [298, "I-87", "I-84", "I-81"],
        "CT": [113, "I-90", "I-91"],
        "NJ": [201, "I-87", "I-287"]},
    "MD": {
        "DE": [65, "US-50", "US-301"],
        "DC": [32, "US-50"]},
    "GA": {
        "SC": [214, "I-20"],
        "MS": [381, "I-20"],
        "AL": [161, "I-85"],
        "TN": [250, "I-75", "I-24"],
        "NC": [405, "I-85", "I-40"],
        "VA": [530, "I-85"],
        "FL": [373, "I-75", "I-10"]},
    "ME": {
        "MA": [167, "I-95"]},
    "TX": {
        "LA": [530, "I-35", "I-10"],
        "OK": [388, "I-35"],
        "AZ": [1059, "I-35", "I-10"],
        "NM": [992, "I-35", "I-40", "I-25"]},
    "LA": {
        "MS": [117, "I-12", "I-55"],
        "AL": [367, "I-10", "I-65"],
        "FL": [443, "I-10"]},
    "ND": {
        "MT": [703, "I-94", "I-90", "I-15"],
        "SD": [205, "US-83"],
        "MN": [435, "I-94"]},
    "ID": {
        "WA": [536, "I-84", "I-5"],
        "OR": [476, "I-84", "I-5"],
        "UT": [339, "I-84"]},
    "MA": {
        "NH": [68,  "I-93"],
        "CT": [101, "I-90", "I-84"],
        "RI": [59,  "I-90", "I-95"]},
    "NV": {
        "CA": [163, "I-580", "I-80"],
        "UT": [546, "I-580", "I-80"]},
    "WV": {
        "SC": [355, "I-64", "I-77"],
        "OH": [212, "I-77", "I-70"],
        "KY": [197, "I-64"],
        "PA": [366, "I-79", "I-68", "I-81"],
        "TN": [389, "I-64", "I-65"],
        "NC": [366, "I-64", "I-77", "I-40"],
        "VA": [317, "I-64"]},
    "WY": {
        "CO": [100, "I-25"],
        "MT": [699, "I-25", "I-90", "I-15"],
        "NE": [442, "I-80"],
        "SD": [694, "I-25", "I-90", "US-83"],
        "UT": [439, "I-80"],
        "KS": [631, "I-25", "I-70"]},
    "SC": {
        "KY": [458, "I-26", "I-40", "I-75"],
        "NC": [456, "I-20", "I-95", "I-40"],
        "FL": [203, "I-26", "I-95", "I-10"]},
    "OH": {
        "KY": [203, "I-71", "I-75", "I-64"],
        "PA": [368, "I-70", "I-76"],
        "IN": [176, "I-70"],
        "MI": [338, "I-70", "I-75", "I-96"]},
    "NH": {
        "VT": [116, "I-89"],
        "RI": [120, "I-93", "I-95"]},
    "CO": {
        "NE": [485, "I-76", "I-80"],
        "UT": [599, "I-70", "I-15"],
        "NM": [390, "I-25"],
        "KS": [542, "I-70"]},
    "IA": {
        "MO": [349, "I-35", "I-70"],
        "NE": [190, "I-80"],
        "WI": [354, "I-80", "I-88", "I-90"],
        "IL": [337, "I-80", "I-74", "I-55"],
        "MN": [248, "I-35"],
        "KS": [225, "I-35", "I-70"]},
    "DE": {
        "NJ": [106, "US-13", "I-95"]},
    "KY": {
        "IN": [165, "I-64", "I-65"],
        "MO": [445, "I-64", "I-70", "US-54"],
        "TN": [219, "I-64", "I-65"]},
    "PA": {
        "TN": [720, "I-81", "I-40"],
        "NJ": [130, "I-76"],
        "DC": [120, "I-83", "I-95"]},
    "CT": {
        "VT": [119, "I-91", "I-89"],
        "RI": [78,  "I-84", "US-44"],
        "NJ": [184, "I-91", "I-95"]},
    "MT": {
        "WA": [720, "I-15", "I-90", "I-5"],
        "SD": [856, "I-15", "I-90", "US-83"],
        "UT": [484, "I-15"]},
    "IN": {
        "MI": [255, "I-69"],
        "WI": [334, "I-65", "I-90"],
        "TN": [289, "I-65"],
        "IL": [212, "I-74", "I-72"]},
    "MS": {
        "AR": [347, "I-55", "I-40"],
        "AL": [248, "I-20", "US-80"],
        "IL": [588, "I-55"]},
    "MO": {
        "AR": [521, "I-70", "I-55", "I-40"],
        "IL": [221, "I-70", "I-55"],
        "KS": [219, "I-70"]},
    "MI": {
        "WI": [364, "I-69", "I-94", "I-90"],
        "IL": [391, "I-69", "I-94", "I-55"]},
    "NE": {
        "SD": [461, "I-80", "I-29", "I-90", "US-83"],
        "KS": [284, "I-80", "I-29", "I-70"]},
    "AR": {
        "TN": [349, "I-40"],
        "OK": [339, "I-40"]},
    "WI": {
        "IL": [264, "I-55", "I-39", "I-90"],
        "MN": [262, "I-94"]},
    "AL": {
        "TN": [280, "I-65"],
        "FL": [412, "I-65", "I-10"]},
    "TN": {
        "NC": [539, "I-40"]},
    "OK": {
        "AZ": [1007, "I-40", "I-17"],
        "NM": [603, "I-40", "I-25"],
        "KS": [293, "I-35", "I-335"]},
    "WA": {
        "OR": [159, "I-5"]},
    "AZ": {
        "CA": [755, "I-10", "I-5"],
        "UT": [663, "I-17", "I-15"],
        "NM": [527, "I-17", "I-40", "I-25"]},
    "SD": {
        "MN": [490, "US-80", "I-90", "I-35"]},
    "NC": {
        "VA": [208, "I-40", "I-95"]},
    "VA": {
        "DC": [108, "I-95"]},
    "CA": {
        "OR": [536, "I-5"],
        "UT": [649, "I-80"]},
    "NJ": {
        "DC": [182, "I-95"]},
}

# Add redundant elements to create a 2-way 2-dimensional dictionary
for origin in list(likely_routes):
    data = likely_routes[origin]
    for target, data in data.items():
        if not target in likely_routes:
            likely_routes[target] = {}

        # Set distance and reverse the routes
        likely_routes[target][origin] = [data[0]]
        for i, route in reversed(list(enumerate(data))[1:]):
            likely_routes[target][origin].append(route)
