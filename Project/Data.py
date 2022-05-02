capitals = {# Capital,        State,            Latitude, Longitude
    "AL" : ["Montgomery",     "Alabama",        32.3792, -86.3077],
    "AR" : ["Little Rock",    "Arkansas",       34.7465, -92.2896],
    "AZ" : ["Pheonix",        "Arizona",        33.4484, -112.0740],
    "CA" : ["Sacramento",     "California",     38.5816, -121.4944],
    "CO" : ["Denver",         "Colorado",       39.7392, -104.9903],
    "CT" : ["Hartford",       "Connecticut",    41.7658, -72.6734],
    "DC" : ["Washington",     "DC",             38.9072, -77.0369],
    "DE" : ["Dover",          "Delaware",       39.1582, -75.5244],
    "FL" : ["Tallahassee",    "Florida",        30.4383, -84.2807],
    "GA" : ["Atlanta",        "Georgia",        33.7490, -84.3880],
    "IA" : ["Des Moines",     "Iowa",           41.5868, -93.6250],
    "ID" : ["Boise",          "Idaho",          43.6150, -116.2023],
    "IL" : ["Springfield",    "Illinois",       39.7817, -89.6501],
    "IN" : ["Indianapolis",   "Indiana",        39.7684, -86.1581],
    "KS" : ["Topeka",         "Kansas",         39.0473, -95.6752],
    "KY" : ["Frankfort",      "Kentucky",       38.2009, -84.8733],
    "LA" : ["Baton Rouge",    "Louisiana",      30.4515, -91.1871],
    "MA" : ["Boston",         "Massachusetts",  42.3601, -71.0589],
    "MD" : ["Annapolis",      "Maryland",       38.9784, -76.4922],
    "ME" : ["Augusta",        "Maine",          44.3106, -69.7795],
    "MI" : ["Lansing",        "Michigan",       42.7325, -84.5555],
    "MN" : ["St. Paul",       "Minnesota",      44.9537, -93.0900],
    "MO" : ["Jefferson City", "Missouri",       38.5767, -92.1735],
    "MS" : ["Jackson",        "Mississippi",    32.2988, -90.1848],
    "MT" : ["Helena",         "Montana",        46.5891, -112.0391],
    "NC" : ["Raleigh",        "North Carolina", 35.7796, -78.6382],
    "ND" : ["Bismarck",       "North Dakota",   46.8083, -100.7837],
    "NE" : ["Lincoln",        "Nebraska",       40.8136, -96.7026],
    "NH" : ["Concord",        "New Hampshire",  43.2081, -71.5376],
    "NJ" : ["Trenton",        "New Jersey",     40.2206, -74.7597],
    "NM" : ["Santa Fe",       "New Mexico",     35.6870, -105.9378],
    "NV" : ["Carson City",    "Nevada",         39.1638, -119.7674],
    "NY" : ["Albany",         "New York",       42.6526, -73.7562],
    "OH" : ["Columbus",       "Ohio",           39.9612, -82.9988],
    "OK" : ["Oklahoma City",  "Oklahoma",       35.4676, -97.5164],
    "OR" : ["Salem",          "Oregon",         44.9429, -123.0351],
    "PA" : ["Harrisburg",     "Pennsylvania",   40.2732, -76.8867],
    "RI" : ["Providence",     "Rhode Island",   41.8240, -71.4128],
    "SC" : ["Columbia",       "South Carolina", 34.0007, -81.0348],
    "SD" : ["Pierre",         "South Dakota",   44.3668, -100.3538],
    "TN" : ["Nashville",      "Tennesee",       36.1627, -86.7816],
    "TX" : ["Austin",         "Texas",          30.2672, -97.7431],
    "UT" : ["Salt Lake City", "Utah",           40.7608, -111.8910],
    "VA" : ["Richmond",       "Virginia",       37.5407, -77.4360],
    "VT" : ["Montpelier",     "Vermont",        44.2601, -72.5754],
    "WA" : ["Olympia",        "Washington",     47.0379, -122.9007],
    "WI" : ["Madison",        "Wisconsin",      43.0722, -89.4008],
    "WY" : ["Cheyenne",       "Wyoming",        32.7765, -79.9311],
    "WV" : ["Charleston",     "West Virginia",  38.3498, -81.6326]
}

cities = [
"Birmingham", "Bloomington", "Champaign", "Chattanooga", "Cincinnati", "Cleveland",
"Dallas", "Interstate 65-90", "Kansas City", "Los Angeles", "Louisville", "St. Louis"
]

intersections = [
["I-10","I-12"],  ["I-10","I-20"],  ["I-10","I-25"],  ["I-10","I-35"],  ["I-10","I-45"],
["I-10","I-49"],  ["I-10","I-59"],  ["I-10","I-65"],  ["I-10","I-75"],  ["I-10","I-95"],
["I-15","I-40"],  ["I-15","I-70"],  ["I-15","I-80"],  ["I-15","I-84"],  ["I-15","I-86"],
["I-15","I-90"],  ["I-20","I-49"],  ["I-20","I-59"],  ["I-20","I-95"],  ["I-24","I-57"],
["I-25","I-40"],  ["I-25","I-80"],  ["I-25","I-90"],  ["I-26","I-81"],  ["I-29","I-94"],
["I-35","I-135"], ["I-35","I-335"], ["I-35","I-90"],  ["I-40","I-17"],  ["I-40","I-26"],
["I-40","I-55"],  ["I-40","I-73"],  ["I-40","I-75"],  ["I-40","I-77"],  ["I-40","I-85"],
["I-40","I-95"],  ["I-5", "I-84"],  ["I-5","I-90"],   ["I-55","I-12"],  ["I-55","I-39"],
["I-55","I-57"],  ["I-57","I-64"],  ["I-64","I-75"],  ["I-64","I-81"],  ["I-66","I-81"],
["I-68","I-79"],  ["I-69","I-90"],  ["I-70","I-135"], ["I-70","I-57"],  ["I-70","I-68"],
["I-70","I-75"],  ["I-70","I-76"],  ["I-70","I-77"],  ["I-70","I-79"],  ["I-70","I-81"],
["I-70","I-99"],  ["I-75","I-16"],  ["I-75","I-64"],  ["I-75","I-81"],  ["I-75","I-90"],
["I-76","I-99"],  ["I-77","I-81"],  ["I-79","I-68"],  ["I-80","I-29"],  ["I-80","I-39"],
["I-80","I-76"],  ["I-80","I-90"],  ["I-81","I-66"],  ["I-81","I-74"],  ["I-82","I-84"],
["I-82","I-90"],  ["I-84","I-5"],   ["I-84","I-86"],  ["I-85","I-26"],  ["I-85","I-74"],
["I-85","I-77"],  ["I-89","I-91"],  ["I-90","I-29"],  ["I-90","I-5"],   ["I-90","I-57"],
["I-90","I-69"],  ["I-90","I-82"],  ["I-90","I-91"],  ["I-90","I-94"],  ["I-95","I-16"],
["I-95","I-26"],  ["I-95","US-64"]
]

roads = {# Road:[[Distance, From, To], ...]
"I-5" :[
    [113, "WA", "I-84"],
    [60,  "WA", "I-90"],
    [386, "CA", "Los Angeles"],
    [46,  "OR", "I-84"],
    [534, "OR", "CA"]],
"I-10" :[
    [53,  "LA",   "I-49"],
    [330, "AZ",   "Los Angeles"],
    [390, "AZ",   "I-25"],
    [96,  "FL",   "I-75"],
    [249, "FL",   "I-65"],
    [206, "I-20", "I-25"],
    [384, "I-35", "I-20"],
    [197, "I-45", "I-35"],
    [224, "I-45", "I-49"],
    [104, "I-65", "I-59"],
    [61,  "I-95", "I-75"]],
"I-12" :[
    [44, "LA",   "I-55"],
    [43, "I-10", "I-55"]],
"I-135" :[
    [102, "I-70", "I-35"]],
"I-15" :[
    [69,  "MT",          "I-90"],
    [71,  "Los Angeles", "I-40"],
    [398, "I-40",        "I-70"],
    [93,  "I-84",        "I-86"],
    [245, "I-90",        "I-86"],
    [121, "UT",          "I-70"]],
"I-16" :[
    [156, "I-95", "I-75"]],
"I-17" :[
    [142, "AZ", "I-40"]],
"I-20" :[
    [147, "GA",         "Birmingham"],
    [214, "GA",         "SC"],
    [217, "MS",         "I-49"],
    [88,  "MS",         "I-59"],
    [76,  "SC",         "I-95"],
    [149, "Birmingham", "I-59"],
    [467, "Dallas",     "I-10"],
    [188, "Dallas",     "I-49"]],
"I-24" :[
    [134, "TN", "Chattanooga"],
    [182, "TN", "I-57"]],
"I-25" :[
    [100, "WY",   "CO"],
    [291, "WY",   "I-90"],
    [393, "NM",   "CO"],
    [64,  "NM",   "I-40"],
    [227, "I-10", "I-40"]],
"I-26" :[
    [93, "SC",   "I-85"],
    [60, "SC",   "I-95"],
    [75, "I-40", "I-81"],
    [69, "I-85", "I-40"]],
"I-29" :[
    [184, "I-90",        "I-80"],
    [232, "I-90",        "I-94"],
    [175, "Kansas City", "I-80"]],
"I-29" :[
    [319, "AR", "Dallas"]],
"I-335" :[
    [60, "KS", "I-35"]],
"I-35" :[
    [195, "TX",          "Dallas"],
    [80,  "TX",          "I-10"],
    [151, "IA",          "I-90"],
    [196, "IA",          "Kansas City"],
    [85,  "I-135",       "I-335"],
    [111, "Kansas City", "I-335"],
    [207, "OK",          "Dallas"],
    [153, "OK",          "I-135"],
    [71,  "MN",          "I-90"]],
"I-39" :[
    [64,  "Bloomington", "I-80"],
    [138, "WI",          "I-80"]],
"I-40" :[
    [137, "AR",   "I-55"],
    [212, "TN",   "I-55"],
    [180, "TN",   "I-75"],
    [541, "OK",   "I-25"],
    [340, "OK",   "AR"],
    [38,  "NC",   "I-85"],
    [32,  "NC",   "I-95"],
    [351, "I-15", "I-17"],
    [324, "I-17", "I-25"],
    [104, "I-26", "I-77"],
    [115, "I-75", "I-26"],
    [39,  "I-85", "I-73"],
    [67,  "I-85", "I-77"]],
"I-44" :[
    [420, "OK", "MO"]],
"I-45" :[
    [239, "Dallas", "I-10"]],
"I-49" :[
    [213, "I-10", "I-20"]],
"I-55" :[
    [140, "I-40",      "I-57"],
    [131, "MS",        "I-12"],
    [210, "MS",        "I-40"],
    [68,  "IL",        "Bloomington"],
    [96,  "IL",        "St. Louis"],
    [143, "St. Louis", "I-57"]],
"I-57" :[
    [79,  "Champaign", "I-70"],
    [132, "Champaign", "Interstate 65-90"],
    [66,  "I-55",      "I-24"],
    [53,  "I-64",      "I-24"],
    [69,  "I-70",      "I-64"]],
"I-59" :[
    [147, "Chattanooga", "Birmingham"],
    [160, "I-10",        "I-20"]],
"I-64" :[
    [175, "WV",         "I-75"],
    [212, "WV",         "I-81"],
    [29,  "KY",         "I-75"],
    [55,  "KY",         "Louisville"],
    [104, "VA",         "I-81"],
    [182, "Louisville", "I-57"],
    [80,  "St. Louis",  "I-57"]],
"I-65" :[
    [150, "IN", "Interstate 65-90"],
    [115, "IN", "Louisville"],
    [91,  "AL", "Birmingham"],
    [169, "AL", "I-10"],
    [191, "TN", "Birmingham"],
    [176, "TN", "Louisville"]],
"I-66" :[
    [77, "DC", "I-81"]],
"I-68" :[
    [112, "I-70", "I-79"]],
"I-69" :[
    [171, "IN", "I-90"],
    [83,  "MI", "I-90"]],
"I-70" :[
    [67,  "OH",        "I-75"],
    [80,  "OH",        "I-77"],
    [432, "CO",        "I-135"],
    [511, "CO",        "I-15"],
    [142, "IN",        "I-57"],
    [109, "IN",        "I-75"],
    [157, "MO",        "Kansas City"],
    [132, "MO",        "St. Louis"],
    [112, "KS",        "I-135"],
    [61,  "KS",        "Kansas City"],
    [71,  "DC",        "I-81"],
    [25,  "I-68",      "I-81"],
    [23,  "I-68",      "I-99"],
    [37,  "I-76",      "I-79"],
    [77,  "I-77",      "I-79"],
    [101, "St. Louis", "I-57"]],
"I-71" :[
    [107, "OH",         "Cincinnati"],
    [125, "OH",         "Cleveland"],
    [100, "Louisville", "Cincinnati"]],
"I-72" :[
    [87, "IL", "Champaign"]],
"I-74" :[
    [127, "IN",          "Champaign"],
    [112, "IN",          "Cincinnati"],
    [110, "I-85",        "I-81"],
    [51,  "Bloomington", "Champaign"]],
"I-75" :[
    [118, "GA",          "Chattanooga"],
    [82,  "GA",          "I-16"],
    [201, "I-10",        "I-16"],
    [180, "I-64",        "I-81"],
    [134, "I-70",        "I-90"],
    [112, "Chattanooga", "I-40"],
    [83,  "Cincinnati",  "I-64"],
    [61,  "Cincinnati",  "I-70"]],
"I-76" :[
    [189, "CO",        "I-80"],
    [83,  "PA",        "I-99"],
    [130, "PA",        "NJ"],
    [87,  "I-70",      "I-99"],
    [155, "Cleveland", "I-70"]],
"I-77" :[
    [132, "WV",        "I-70"],
    [131, "WV",        "I-81"],
    [93,  "SC",        "I-85"],
    [91,  "I-40",      "I-81"],
    [42,  "I-85",      "I-40"],
    [103, "Cleveland", "I-70"]],
"I-79" :[
    [151, "WV",   "I-68"],
    [46,  "I-70", "I-68"]],
"I-80" :[
    [534, "NV",               "UT"],
    [145, "WY",               "I-76"],
    [440, "WY",               "UT"],
    [128, "IA",               "I-29"],
    [253, "IA",               "I-39"],
    [60,  "NE",               "I-29"],
    [298, "NE",               "I-76"],
    [144, "CA",               "NV"],
    [98,  "Interstate 65-90", "I-39"]],
"I-81" :[
    [78, "PA",    "I-70"],
    [79, "I-64",  "I-66"],
    [53, "I-70",  "I-66"],
    [91, "I-75",  "I-26"],
    [99, "I-77",  "I-26"],
    [144, "I-77", "I-64"]],
"I-82" :[
    [132, "I-90", "I-84"]],
"I-83" :[
    [111, "PA", "MD"]],
"I-84" :[
    [252, "ID",   "I-82"],
    [170, "ID",   "I-86"],
    [73,  "CT",   "RI"],
    [106, "I-15", "I-86"],
    [177, "I-5",  "I-82"],
    [73,  "UT",   "I-15"]],
"I-85" :[
    [176, "GA",   "I-26"],
    [161, "GA",   "AL"],
    [74,  "I-77", "I-26"],
    [89,  "I-77", "I-40"],
    [164, "VA",   "I-40"]],
"I-86" :[
    [63, "I-84", "I-15"]],
"I-87" :[
    [195, "NY", "NJ"]],
"I-89" :[
    [62, "NH", "I-91"],
    [54, "VT", "I-91"]],

"I-90" :[
    [79,  "NY",               "I-91"],
    [91,  "MA",               "I-91"],
    [258, "WI",               "I-35"],
    [397, "SD",               "I-25"],
    [222, "SD",               "I-29"],
    [244, "I-15",             "I-94"],
    [175, "I-35",             "I-29"],
    [108, "I-5",              "I-82"],
    [78,  "I-75",             "I-69"],
    [481, "I-82",             "I-15"],
    [156, "I-94",             "I-25"],
    [110, "Cleveland",        "I-75"],
    [128, "Interstate 65-90", "I-69"]],
"I-91" :[
    [31,  "CT",   "I-90"],
    [114, "I-90", "I-89"]],
"I-93" :[
    [68, "MA", "NH"]],
"I-94" :[
    [191, "ND", "I-29"],
    [410, "ND", "I-90"],
    [246, "MN", "I-29"],
    [163, "MN", "WI"]],
"I-95" :[
    [167, "ME",   "MA"],
    [112, "DE",   "NJ"],
    [59,  "RI",   "MA"],
    [119, "VA",   "US-64"],
    [181, "NJ",   "CT"],
    [109, "DC",   "VA"],
    [129, "I-10", "I-16"],
    [75,  "I-20", "I-26"],
    [119, "I-20", "I-40"],
    [99,  "I-26", "I-16"],
    [58,  "I-40", "US-64"]],
"US-301" :[
    [65, "DE", "MD"]],
"US-50" :[
    [32, "DC", "MD"]],
"US-64" :[
    [52, "NC", "I-95"]],
}

likely_routes = {# From :{ To:[Distance, Road1, Road2, Etc...], ... }
"NY" :{
    "MA" : [170, "I-90"],
    "PA" : [298, "I-87", "I-84", "I-81"],
    "CT" : [113, "I-90", "I-91"],
    "NJ" : [201, "I-87", "I-287"]},
"MD" :{
    "DE" : [65, "US-50", "US-301"],
    "DC" : [32, "US-50"]},
"GA" :{
    "SC" : [214, "I-20"],
    "MS" : [381, "I-20"],
    "AL" : [161, "I-85"],
    "TN" : [250, "I-75", "I-24"],
    "NC" : [405, "I-85", "I-40"],
    "VA" : [530, "I-85"],
    "FL" : [373, "I-75", "I-10"]},
"ME" :{
    "MA" : [167, "I-95"]},
"TX" :{
    "LA" : [530, "I-35", "I-10"],
    "OK" : [388, "I-35"],
    "AZ" : [1059,"I-35", "I-10"],
    "NM" : [992, "I-35", "I-40", "I-25"]},
"LA" :{
    "MS" : [117, "I-12", "I-55"],
    "AL" : [367, "I-10", "I-65"],
    "FL" : [443, "I-10"]},
"ND" :{
    "MT" : [703, "I-94", "I-90", "I-15"],
    "SD" : [205, "US-83"],
    "MN" : [435, "I-94"]},
"ID" :{
    "WA" : [536, "I-84", "I-5"],
    "OR" : [476, "I-84", "I-5"],
    "UT" : [339, "I-84"]},
"MA" :{
    "NH" : [68,  "I-93"],
    "CT" : [101, "I-90", "I-84"],
    "RI" : [59,  "I-90", "I-95"]},
"NV" :{
    "CA" : [163, "I-580", "I-80"],
    "UT" : [546, "I-580", "I-80"]},
"WV" :{
    "SC" : [355, "I-64", "I-77"],
    "OH" : [212, "I-77", "I-70"],
    "KY" : [197, "I-64"],
    "PA" : [366, "I-79", "I-68", "I-81"],
    "TN" : [389, "I-64", "I-65"],
    "NC" : [366, "I-64", "I-77", "I-40"],
    "VA" : [317, "I-64"]},
"WY" :{
    "CO" : [100, "I-25"],
    "MT" : [699, "I-25", "I-90", "I-15"],
    "NE" : [442, "I-80"],
    "SD" : [694, "I-25", "I-90", "US-83"],
    "UT" : [439, "I-80"],
    "KS" : [631, "I-25", "I-70"]},
"SC" :{
    "KY" : [458, "I-26", "I-40", "I-75"],
    "NC" : [456, "I-20", "I-95", "I-40"],
    "FL" : [203, "I-26", "I-95", "I-10"]},
"OH" :{
    "KY" : [203, "I-71", "I-75", "I-64"],
    "PA" : [368, "I-70", "I-76"],
    "IN" : [176, "I-70"],
    "MI" : [338, "I-70", "I-75", "I-96"]},
"NH" :{
    "VT" : [116, "I-89"],
    "RI" : [120, "I-93", "I-95"]},
"CO" :{
    "NE" : [485, "I-76", "I-80"],
    "UT" : [599, "I-70", "I-15"],
    "NM" : [390, "I-25"],
    "KS" : [542, "I-70"]},
"IA" :{
    "MO" : [349, "I-35", "I-70"],
    "NE" : [190, "I-80"],
    "WI" : [354, "I-80", "I-88", "I-90"],
    "IL" : [337, "I-80", "I-74", "I-55"],
    "MN" : [248, "I-35"],
    "KS" : [225, "I-35", "I-70"]},
"DE" :{
    "NJ" : [106, "US-13", "I-95"]},
"KY" :{
    "IN" : [165, "I-64", "I-65"],
    "MO" : [445, "I-64", "I-70", "US-54"],
    "TN" : [219, "I-64", "I-65"]},
"PA" :{
    "TN" : [720, "I-81", "I-40"],
    "NJ" : [130, "I-76"],
    "DC" : [120, "I-83", "I-95"]},
"CT" :{
    "VT" : [119, "I-91", "I-89"],
    "RI" : [78,  "I-84", "US-44"],
    "NJ" : [184, "I-91", "I-95"]},
"MT" :{
    "WA" : [720, "I-15", "I-90", "I-5"],
    "SD" : [856, "I-15", "I-90", "US-83"],
    "UT" : [484, "I-15"]},
"IN" :{
    "MI" : [255, "I-69"],
    "WI" : [334, "I-65", "I-90"],
    "TN" : [289, "I-65"],
    "IL" : [212, "I-74", "I-72"]},
"MS" :{
    "AR" : [347, "I-55", "I-40"],
    "AL" : [248, "I-20", "US-80"],
    "IL" : [588, "I-55"]},
"MO" :{
    "AR" : [521, "I-70", "I-55", "I-40"],
    "IL" : [221, "I-70", "I-55"],
    "KS" : [219, "I-70"]},
"MI" :{
    "WI" : [364, "I-69", "I-94", "I-90"],
    "IL" : [391, "I-69", "I-94", "I-55"]},
"NE" :{
    "SD" : [461, "I-80", "I-29", "I-90", "US-83"],
    "KS" : [284, "I-80", "I-29", "I-70"]},
"AR" :{
    "TN" : [349, "I-40"],
    "OK" : [339, "I-40"]},
"WI" :{
    "IL" : [264, "I-55", "I-39", "I-90"],
    "MN" : [262, "I-94"]},
"AL" :{
    "TN" : [280, "I-65"],
    "FL" : [412, "I-65", "I-10"]},
"TN" :{
    "NC" : [539, "I-40"]},
"OK" :{
    "AZ" : [1007,"I-40", "I-17"],
    "NM" : [603, "I-40", "I-25"],
    "KS" : [293, "I-35", "I-335"]},
"WA" :{
    "OR" : [159, "I-5"]},
"AZ" :{
    "CA" : [755, "I-10", "I-5"],
    "UT" : [663, "I-17", "I-15"],
    "NM" : [527, "I-17", "I-40", "I-25"]},
"SD" :{
    "MN" : [490, "US-80", "I-90", "I-35"]},
"NC" :{
    "VA" : [208, "I-40", "I-95"]},
"VA" :{
    "DC" : [108, "I-95"]},
"CA" :{
    "OR" : [536, "I-5"],
    "UT" : [649, "I-80"]},
"NJ" :{
    "DC" : [182, "I-95"]},
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

# Combine and assign ids to vertices
vertices = []

for x in capitals:
    vertices.append([x, True])
for x in cities:
    vertices.append([x, False])
for x in intersections:
    vertices.append(x)

# Lazy getter for vertex index
def get_vertex_id(point, road):
    for i, v in enumerate(vertices):
        a, b = v[0], v[1]
        # Capital, City, or Intersection
        if a == point:
            if b == True or b == False or b == road:
                return i
        # Intersection (Inverse)
        elif a == road and b == point:
            return i

# Create adjacency list of edges ({int:{int = [int,str]}})
edges = {}
for i in range(len(vertices)):
    edges[i] = {}
for road, route in roads.items():
    for x in route:
        r, dist, v1, v2 = road, x[0], x[1], x[2]
        
        id1 = get_vertex_id(v1, r)
        id2 = get_vertex_id(v2, r)
        edge = [dist, r]

        edges[id1][id2] = edge
        edges[id2][id1] = edge

#for x, column in edges.items():
#    for y, dis_road in column.items():
#        print(vertices[x], "---[ " + dis_road[1] + " ] (", dis_road[0], ")-->", vertices[y])

# Returns the shortest weighted paths from a starting node
def dijkstra_algorithm(start_node):
    unvisited_nodes = list(range(len(vertices))) # Pointer List of verices to visit
    shortest_paths  = {} # Use this dict to save the cost of visiting each node and updates as it moves along the graph   
    previous_nodes  = {} # Use this dict to save the shortest known path to a node found so far {int = [int, str]}

    max_value = 1e100 # Use a huge value to initialize the "infinity" value of the unvisited nodes
    for i in unvisited_nodes:
        shortest_paths[i] = max_value

    shortest_paths[start_node] = 0  # Starting node always has 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # Finds the vertex with the shortest path
        current_min_node = None
        for i in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = i
            elif shortest_paths[i] < shortest_paths[current_min_node]:
                current_min_node = i

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = []
        for i, v in enumerate(vertices):
            if edges[current_min_node].get(i, False) != False:
                neighbors.append(i)

        for i in neighbors:
            tentative_value = shortest_paths[current_min_node] + edges[current_min_node][i][0]
            if tentative_value < shortest_paths[i]:
                shortest_paths[i]  = tentative_value
                previous_nodes[i] = [current_min_node, edges[current_min_node][i][1]] # We also update the best path to the current node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_paths


# Finally, create the complete dictionary of Capital routes
all_routes = {}
for start in capitals:
    source = get_vertex_id(start, True)
    all_routes[start] = {}
    previous_nodes, shortest_paths = dijkstra_algorithm(source)
    
    for finish in capitals:
        target = get_vertex_id(finish, True)
        path = []
        node = target
        
        # Loop and append, ignoring the source node
        while node != source:
            path.append([node, previous_nodes[node][1]])
            node = previous_nodes[node][0]
        
        result = shortest_paths[target]
        all_routes[start][finish] = [result]
        last_road = ""

        for x in reversed(path):
            current_road = x[1]
            if current_road != last_road:
                all_routes[start][finish].append(current_road)
            last_road = current_road

    del all_routes[start][start] # Remove path to itself (Optional, as it is always [0])

