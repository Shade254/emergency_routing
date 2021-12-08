import xml.etree.ElementTree as et
import json
import copy


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
            j = 0
            i = 0
            for child1 in child:
                j = j + 1
                if child1.tag == 'nd' and i != 0 and j != len(child.findall('nd')):
                    ndChild = et.SubElement(wayChild, 'nd')
                    for key, value in child1.attrib.items():
                        if key == 'ref':
                            ndChild.set(key, value)
                        dupe = copy.deepcopy(child1)
                        wayChild.append(dupe)
                if child1.tag == 'nd' and i == 0 or j == len(child.findall('nd')):
                    ndChild = et.SubElement(wayChild, 'nd')
                    for key, value in child1.attrib.items():
                        if key == 'ref':
                            ndChild.set(key, value)
                    i = 1
    tree = et.ElementTree(root)
    tree.write('temp.xml')
    nodeTree = et.parse('temp.xml')
    nodeRoot = nodeTree.getroot()
    a = []
    for node in nodeRoot.findall('node'):
        b = []
        for way in nodeRoot.findall('way'):
            j = 0
            for nd in way.findall('nd'):
                if j == 0:
                    b.append(nd.attrib['ref'])
                if j == len(way.findall('nd')) - 1:
                    b.append(nd.attrib['ref'])
                j = j + 1
            if b[len(b) - 1] == b[len(b) - 2]:
                nodeRoot.remove(way)
            for nd in way.findall('nd'):
                if nd.attrib['ref'] == node.attrib['id']:
                    nd.attrib.update(node.attrib)
                    a.append(nd.attrib['ref'])
        if node.attrib['id'] not in a:
            nodeRoot.remove(node)
    nodeTree.write('temp.xml')
    return 'temp.xml'


def xml_to_json(filename):
    i = 1
    list = []
    list2 = []
    building = {"type": "FeatureCollection"}
    originalTree = et.parse(filename)
    originalNode = originalTree.getroot()
    for nodeChild in originalNode:
        coor = []
        if nodeChild.tag == 'node':
            singlearray = {"type"    : "Feature", "properties": {"name": nodeChild.attrib['id']},
                           "geometry": {"type": "Point", "coordinates": [float(nodeChild.attrib['lon']),
                                                                         float(nodeChild.attrib['lat'])]}}
            list.append(singlearray)
        if nodeChild.tag == 'way':
            coor = []
            for ndChild in nodeChild:
                coor.append([float(ndChild.attrib['lon']), float(ndChild.attrib['lat'])])
                if i % 2 != 0:
                    fm = ndChild.attrib['id']
                if i % 2 == 0:
                    t = ndChild.attrib['id']
                    single = {"type"    : 'Feature', "properties": {"from": fm, "to": t},
                              "geometry": {"type"       : "LineString",
                                           "coordinates": coor}}
                    list2.append(single)
                    coor = []
                i = i + 1
    combined = list + list2
    building.update({"features": combined})
    with open("map.json", 'w') as f:
        f.write(json.dumps(building, indent=4))
    return


xml_to_json(extract_xml('zoo.osm'))
