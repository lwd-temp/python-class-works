studentinfo = [{'id': 1, 'name': 'Rose', 'score': 80}, {'id': 2, 'name': 'Cindy', 'score': 98}, {
    'id': 3, 'name': 'Lily', 'score': 78}, {'id': 4, 'name': 'Gary', 'score': 90}, {'id': 5, 'name': 'Joan', 'score': 89}]


def get_struct_info(dict):
    output = {}
    for i in dict:
        output.update({i['id']: [i['name'], i['score']]})
    return output


if __name__ == '__main__':
    studentdata = get_struct_info(studentinfo)
    exitFlag = True
    while exitFlag:
        getid = input('Please input the student id: ')
        if getid == 'q':
            exitFlag = False
        else:
            try:
                intid = int(getid)
                try:
                    print(studentdata[intid][0], studentdata[intid][1])
                except Exception as e:
                    print('No such student id: '+str(e))
            except Exception as e:
                print('No such student id: '+str(e))
