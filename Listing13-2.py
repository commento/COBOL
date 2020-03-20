states = [
{"code" : "AL", "name" : "ALABAMA", "capital" : "MONTGOMERY"},
{"code" : "AK", "name" : "ALASKA", "capital" : "JUNEAU"},
{"code" : "AZ", "name" : "ARIZONA", "capital" : "PHOENIX"},
{"code" : "AR", "name" : "ARKANSAS", "capital" : "LITTLE ROCK"},
{"code" : "CA", "name" : "CALIFORNIA", "capital" : "SACRAMENTO"},
{"code" : "CO", "name" : "COLORADO", "capital" : "DENVER"},
{"code" : "CT", "name" : "CONNECTICUT", "capital" : "HARTFORD"},
{"code" : "DE", "name" : "DELAWARE", "capital" : "DOVER"},
{"code" : "FL", "name" : "FLORIDA", "capital" : "TALLAHASSE"},
{"code" : "GA", "name" : "GEORGIA", "capital" : "ATLANTA"},
{"code" : "HI", "name" : "HAWAII", "capital" : "HONOLULU"},
{"code" : "ID", "name" : "IDAHO", "capital" : "BOISE"},
{"code" : "IL", "name" : "ILLINOIS", "capital" : "SPRINGFIELD"},
{"code" : "IN", "name" : "INDIANA", "capital" : "INDIANAPOLIS"},
{"code" : "IA", "name" : "IOWA", "capital" : "DES"},
{"code" : "KS", "name" : "KANSAS", "capital" : "TOPEKA"},
{"code" : "KY", "name" : "KENTUCKY", "capital" : "FRANKFORT"},
{"code" : "LA", "name" : "LOUISIANA", "capital" : "BATON ROUGE"},
{"code" : "ME", "name" : "MAINE", "capital" : "AUGUSTA"},
{"code" : "MD", "name" : "MARYLAND", "capital" : "ANNAPOLIS"},
{"code" : "MA", "name" : "MASSACHUSETTS", "capital" : "BOSTON"},
{"code" : "MI", "name" : "MICHIGAN", "capital" : "LANSING"},
{"code" : "MN", "name" : "MINNESOTA", "capital" : "SAINT"},
{"code" : "MS", "name" : "MISSISSIPPI", "capital" : "JACKSON"},
{"code" : "MO", "name" : "MISSOURI", "capital" : "JEFFERSON"},
{"code" : "MT", "name" : "MONTANA", "capital" : "HELENA"},
{"code" : "NE", "name" : "NEBRASKA", "capital" : "LINCOLN"},
{"code" : "NV", "name" : "NEVADA", "capital" : "CARSON CITY"},
{"code" : "NH", "name" : "NEW", "capital" : "CONCORD"},
{"code" : "NJ", "name" : "NEW", "capital" : "TRENTON"},
{"code" : "NM", "name" : "NEW", "capital" : "SANTA"},
{"code" : "NY", "name" : "NEW", "capital" : "ALBANY"},
{"code" : "NC", "name" : "NORTH", "capital" : "RALEIGH"},
{"code" : "ND", "name" : "NORTH", "capital" : "BISMARCK"},
{"code" : "OH", "name" : "OHIO", "capital" : "COLUMBUS"},
{"code" : "OK", "name" : "OKLAHOMA", "capital" : "OKLAHOMA CITY"},
{"code" : "OR", "name" : "OREGON", "capital" : "SALEM"},
{"code" : "PA", "name" : "PENNSYLVANIA", "capital" : "HARRISBURG"},
{"code" : "RI", "name" : "RHODE", "capital" : "PROVIDENCE"},
{"code" : "SC", "name" : "SOUTH", "capital" : "COLUMBIA"},
{"code" : "SD", "name" : "SOUTH", "capital" : "PIERRE"},
{"code" : "TN", "name" : "TENNESSEE", "capital" : "NASHVILLE"},
{"code" : "TX", "name" : "TEXAS", "capital" : "AUSTIN"},
{"code" : "UT", "name" : "UTAH", "capital" : "SALT LAKE CITY"},
{"code" : "VT", "name" : "VERMONT", "capital" : "MONTPELIER"},
{"code" : "VA", "name" : "VIRGINIA", "capital" : "RICHMOND"},
{"code" : "WA", "name" : "WASHINGTON", "capital" : "OLYMPIA"},
{"code" : "WV", "name" : "WEST", "capital" : "CHARLESTON"},
{"code" : "WI", "name" : "WISCONSIN", "capital" : "MADISON"},
{"code" : "WY", "name" : "WYOMING", "capital" : "CHEYENNE"}]


sel = input("search by 1 state code, 2 state name, 3 state capital: ")

if sel == "1":
    name = input("input state code: ")
    ret = next((item for item in states if item["code"] == name.upper()), None)
    if ret is None:
        print("state not found")
    else:
        print("state name", ret["name"], "state capital", ret["capital"])
elif sel == "2":
    name = input("input state name: ")
    ret = next((item for item in states if item["name"] == name.upper()), None)
    if ret is None:
        print("state not found")
    else:
        print("state code", ret["code"], "state capital", ret["capital"])
elif sel == "3":
    name = input("input state capital: ")
    ret = next((item for item in states if item["capital"] == name.upper()), None)
    if ret is None:
        print("state not found")
    else:
        print("state code", ret["code"], "state name", ret["name"])