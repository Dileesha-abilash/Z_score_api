import json

def zScore(district, mark):
    locations = ['COLOMBO', 'GAMPAHA', 'KALUTARA', 'MATALE', 'KANDY', 'NUWARA ELIYA',
                 'GALLE', 'MATARA', 'HAMBANTOTA', 'JAFFNA', 'KILINOCHCHI', 'MANNAR',
                 'MULLAITIVU', 'VAVUNIYA', 'TRINCOMALEE', 'BATTICALOA', 'AMPARA',
                 'PUTTALAM', 'KURUNEGALA', 'ANURADHAPURA', 'POLONNARUWA', 'BADULLA',
                 'MONARAGALA', 'KEGALLE', 'RATNAPURA']

    data_list = [
        "INFORMATION COMMUNICATION TECHNOLOGY  ||  University of Vavuniya Sri Lanka",
    "INFORMATION COMMUNICATION TECHNOLOGY  ||  Uva Wellassa University of Sri Lanka",
    "PHYSICAL SCIENCE -ICT  ||  University of Sri Jayewardenepura",
    "PHYSICAL SCIENCE -ICT  ||  University of Kelaniya",
    "TRANSLATION STUDIES  ||  University of Kelaniya",
    "TRANSLATION STUDIES  ||  Sabaragamuwa University of Sri Lanka",
    "TRANSLATION STUDIES  ||  University of Jaffna",
    "TRANSLATION STUDIES  ||  Eastern University Sri Lanka",
    "FILM & TELEVISION STUDIES  ||  University of Kelaniya",
    "PROJECT MANAGEMENT  ||  University of Vavuniya Sri Lanka",
    "TEACHING ENGLISH AS A SECOND LANGUAGE (TESL)  ||  University of Sri Jayewardenepura",
    "TEACHING ENGLISH AS A SECOND LANGUAGE (TESL)  ||  University of Kelaniya",
    "VISUAL ARTS  ||  University of the Visual & Performing Arts",
    "MUSIC  ||  University of the Visual & Performing Arts",
    "DANCE  ||  University of the Visual & Performing Arts",
    "DRAMA & THEATRE  ||  University of the Visual & Performing Arts",
    "ART & DESIGN  ||  Ramanathan Academy of Fine Arts",
    "MUSIC  ||  Ramanathan Academy of Fine Arts",
    "DANCE  ||  Ramanathan Academy of Fine Arts",
    "VISUAL & TECHNOLOGICAL ARTS  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "MUSIC  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "DANCE  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "DRAMA & THEATRE  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "FOOD BUSINESS MANAGEMENT [Commerce Stream]  ||  Sabaragamuwa University of Sri Lanka"]

    district_index = locations.index(district)
    file = open("firstpage_175_no_col.csv", "r")

    f = file.readlines()
    file.close()
    my_district = f[district_index].split(",")
    selected_index = []
    selected = []

    for i in range(len(my_district)):
        try:
            if float(my_district[i]) <= mark:
                combine = f"{i}||{my_district[i]}"
                selected_index.append(combine)
        except:
            pass

    for j in selected_index:
        pp = int(j.split("||")[0])
        selected.append(f"{data_list[pp]} $ {(j.split('||')[1])}")

    return selected


def subs(s1, s2, s3):
    subjects_all = {
        "COMBINED MATHEMATICS", "BUDDHISM", "HINDUISM",  # ... (other subjects)
        "GEOGRAPHY", "COMMUNICATION & MEDIA STUDIES"
    }
    
    file_subject_req = open("test")
    k = file_subject_req.readlines()
    cap_subjects = []

    for i in range(len(k)):
        one_line_sub = k[i].split("||")[1].split(",")

        for p in range(len(one_line_sub)):
            one_line_sub[p] = one_line_sub[p].strip()

        if (s1 in one_line_sub) and (s2 in one_line_sub) and (s3 in one_line_sub):
            cap_subjects.append(k[i].split("||")[0])

    return cap_subjects


def Main(ss1, ss2, ss3, district, zScr, bais=0.4):
    com = []
    sub_pos = subs(ss1, ss2, ss3)
    z_pos = zScore(district, zScr + bais)

    for i in z_pos:
        if i.split("||")[0] in sub_pos:
            com.append(i)

    return com


def stru_json(com):
    original_data = [
        'VISUAL ARTS  ||  University of the Visual & Performing Arts $ 1.7720000000000002',
        'MUSIC  ||  University of the Visual & Performing Arts $ 1.7720000000000002',
        'MUSIC  ||  Ramanathan Academy of Fine Arts $ 1.7720000000000002',
        'MUSIC  ||  Swami Vipulananda Institute of Aesthetic Studies $ 1.7720000000000002'
    ]

    converted_data = []

    for item in com:
        category, university_and_amount = item.split("  ||  ")
        university, amount = university_and_amount.split(" $ ")
        amount = float(amount)
        converted_data.append({'category': f"{category}", 'university': f"{university}", 'z-score': f'{amount}'})

    # json_data = json.dumps(converted_data, indent=2)
    return converted_data


def json_out(json_not_stuc):
    json_data_cleaned2 = json_not_stuc.replace('\n', '').replace('\"', '')
    json_data_cleaned = json_data_cleaned2.replace('    ', '')

    return json_data_cleaned


if __name__ == "__main__":
    gg = "RATNAPURA"
    z = 1.372
    bb = 0.4
    Main(ss1, ss2, ss3, gg, z, bb)
