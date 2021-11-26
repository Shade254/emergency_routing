import xml.etree.ElementTree as et
import json


def extract_xml(filename):
    originalTree = et.parse(filename)
    originalNode = originalTree.getroot()
    root = et.Element(originalNode.tag)
    for child in originalNode:
        if child.tag == 'node':
            nodeChild = et.SubElement(root, 'node')
            for key, value in child.attrib.items():
                if key == 'id' or key == 'lon' or key == 'lat':
                    nodeChild.set(key, value)
        if child.tag == 'way':
            wayChild = et.SubElement(root, 'way')
            for key, value in child.attrib.items():
                if key == 'id':
                    wayChild.set(key, value)
            for child1 in child:
                if child1.tag == 'nd':
                    ndChild = et.SubElement(wayChild, 'nd')
                    for key, value in child1.attrib.items():
                        if key == 'ref':
                            ndChild.set(key, value)
    tree = et.ElementTree(root)
    tree.write('temp.xml')
    nodeTree = et.parse('temp.xml')
    nodeRoot = nodeTree.getroot()
    root2 = et.Element(nodeRoot.tag)
    for node in nodeRoot.findall('node'):
        for way in nodeRoot.findall('way'):
            for nd in way.findall('nd'):
                if nd.attrib['ref'] == node.attrib['id']:
                    nd.attrib.update(node.attrib)
    nodeTree.write('temp.xml')
    return 'temp.xml'


def xml_to_json(filename):
    i = 0
    list = []
    list2 = []
    building = {"type": "FeatureCollection"}
    originalTree = et.parse(filename)
    originalNode = originalTree.getroot()
    for nodeChild in originalNode:
        coor = []
        if nodeChild.tag == 'node':
            singlearray = {"type": "Feature", "properties": {"name": nodeChild.attrib['id']},
                           "geometry": {"type": "Point", "coordinates": [nodeChild.attrib['lat'],
                                                                         nodeChild.attrib['lon']]}}
            list.append(singlearray)
        if nodeChild.tag == 'way':
            for ndChild in nodeChild:
                coor.append([ndChild.attrib['lat'], ndChild.attrib['lon']])
                if i == 0:
                    firstNd = ndChild.attrib['id']
                if i == len(nodeChild) - 1:
                    lastNd = ndChild.attrib['id']
                i = i + 1
            i = 0
            single = {"type": 'Feature', "properties": {"from": firstNd, "to": lastNd},
                      "geometry": {"type": "LineString",
                                   "coordinates": coor}}
            list2.append(single)
    combined = list + list2
    building.update({"features": combined})
    with open("map.json", 'w') as f:
        f.write(json.dumps(building, indent=4))
    return
