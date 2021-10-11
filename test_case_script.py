import json
import sys


def remove_properties(feature):
    unwanted_properties = ["stroke", "stroke-width", "stroke-opacity", "fill", "fill-opacity", "marker-color", "marker"
                                                                                                               "-size",
                           "marker-symbol"]
    for p in unwanted_properties:
        if p in feature['properties']:
            del feature['properties'][p]

    return feature


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Enter test case file path as program argument")

    for path in sys.argv[1:]:
        max_index = 0

        with open(path, "r") as read_file:
            json_content = json.load(read_file)
            edges = []
            nodes = []
            areas = []
            for feature in json_content["features"]:
                if feature["geometry"]["type"] == "Point":
                    nodes.append(feature)
                elif feature["geometry"]["type"] == "LineString":
                    edges.append(feature)
                else:
                    areas.append(feature)

            for n in nodes:
                remove_properties(n)
                if "name" in n["properties"] and "crossroad" in n["properties"]["name"]:
                    max_index = max(max_index, int(n["properties"]["name"].split("_")[-1]))
                elif "name" not in n["properties"]:
                    max_index += 1
                    n["properties"]["name"] = "crossroad_" + max_index.__str__()

            for e in edges:
                remove_properties(e)
                if "from" not in e["properties"]:
                    first_location = e["geometry"]["coordinates"][0]
                    for n in nodes:
                        if first_location == n["geometry"]["coordinates"]:
                            e["properties"]["from"] = n["properties"]["name"]
                            break

                if "to" not in e["properties"]:
                    last_location = e["geometry"]["coordinates"][-1]
                    for n in nodes:
                        if last_location == n["geometry"]["coordinates"]:
                            e["properties"]["to"] = n["properties"]["name"]
                            break

            for a in areas:
                remove_properties(a)

            for n in nodes:
                for e in edges:
                    if "to" in e["properties"] and e["properties"]["to"] == n["properties"]["name"]:
                        n["geometry"]["coordinates"] = e["geometry"]["coordinates"][-1]
                        break
                    elif "from" in e["properties"] and e["properties"]["from"] == n["properties"]["name"]:
                        n["geometry"]["coordinates"] = e["geometry"]["coordinates"][0]
                        break

        with open(path, "w") as write_file:
            features = []
            features.extend(nodes)
            features.extend(edges)
            features.extend(areas)

            feature_collection = {"type": "FeatureCollection", "features": features}
            json.dump(feature_collection, write_file, indent=3)
