import xml.etree.ElementTree as ET
root = ET.parse('example.xml').getroot()
print (root)
print (root[11])
i=0
root=root[11]
el=None
for child in root:
    # print(type(child.attrib))
    # print(child.attrib['name'])
    # print(child.tag, child.attrib, i)
    if child.attrib['name'] == 'Q':
        el=child
        # print(child.tag, child.attrib)
    i+=1
print el
contours=[]
for child in el:
    if child.tag == 'contour':
        contours.append(child)
print (contours)
contours_parsed =[]
for c in contours:
    points =[]
    for child in c:
        points.append([float(child.attrib['x']), float(child.attrib['y']), int(child.attrib['on'])])
        # print(child.tag, child.attrib)
    # print ('end')
    contours_parsed.append(points)
print (contours_parsed)
contours_parsed_proccessed = []
for contour in contours_parsed:
    curr_contour = []
    for i in range(len(contour)):
        if contour[i][2] == 1:
            curr_contour.append(contour[i])
        if contour[i][2] == 0 :
            curr_contour.append(contour[i])
            if contour[(i+1)%len(contour)][2] == 0:
                x = float(contour[i][0] + contour[(i+1)%len(contour)][0]) / 2
                y = float(contour[i][1] + contour[(i+1)%len(contour)][1]) / 2
                curr_contour.append([x,y, 1])
    contours_parsed_proccessed.append(curr_contour)

print (contours_parsed_proccessed)

for contour in contours_parsed_proccessed:
    print('new contour')
    for p in contour:
        if p[2] == 0:
            print('myExample.moveTo({x}, {y})'.format(x=p[0], y=p[1]))
    print('end contour')
