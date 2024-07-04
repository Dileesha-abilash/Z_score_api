import json

def zScore(district, mark):
    
    # Districs 
    locations = ['COLOMBO', 'GAMPAHA', 'KALUTARA', 'MATALE', 'KANDY', 'NUWARA ELIYA',
                 'GALLE', 'MATARA', 'HAMBANTOTA', 'JAFFNA', 'KILINOCHCHI', 'MANNAR',
                 'MULLAITIVU', 'VAVUNIYA', 'TRINCOMALEE', 'BATTICALOA', 'AMPARA',
                 'PUTTALAM', 'KURUNEGALA', 'ANURADHAPURA', 'POLONNARUWA', 'BADULLA',
                 'MONARAGALA', 'KEGALLE', 'RATNAPURA']

    # Course Name and Location
    data_list = ['MEDICINE || (University of Colombo)', 'MEDICINE || (University of Peradeniya)', 'MEDICINE || (University of Sri Jayewardenepura)', 'MEDICINE || (University of Kelaniya)', 'MEDICINE || (University of Jaffna)', 'MEDICINE || (University of Ruhuna)', 'MEDICINE || (University of Moratuwa)', 'MEDICINE || (Eastern University, Sri Lanka)', 'MEDICINE || (Rajarata University of Sri Lanka)', 'MEDICINE || (Sabaragamuwa University of Sri Lanka)', 'MEDICINE || (Wayamba University of Sri Lanka)', 'DENTAL SURGERY || (University of Peradeniya)', 'DENTAL SURGERY || (University of Sri Jayewardenepura)', 'VETERINARY SCIENCE || (University of Peradeniya)', 'BIOCHEMISTRY & MOLECULAR BIOLOGY || (University of Colombo)', 'AGRICULTURAL TECHNOLOGY & MANAGEMENT || (University of Peradeniya)', 'AGRICULTURE || (University of Jaffna)', 'AGRICULTURE || (Eastern University, Sri Lanka)', 'AGRICULTURE || (Rajarata University of Sri Lanka)', 'AGRICULTURE || (Sabaragamuwa University of Sri Lanka)', 'AGRICULTURE || (Wayamba University of Sri Lanka)', 'FOOD SCIENCE & NUTRITION || (Wayamba University of Sri Lanka)', 'FOOD SCIENCE & TECHNOLOGY || (University of Peradeniya)', 'FOOD SCIENCE & TECHNOLOGY || (University of Sri Jayewardenepura)', 'FOOD SCIENCE & TECHNOLOGY || (Sabaragamuwa University of Sri Lanka)', 'BIOLOGICAL SCIENCE || (University of Colombo)', 'NURSING || (University of Peradeniya)', 'NURSING || (University of Sri Jayewardenepura)', 'NURSING || (University of Jaffna)', 'NURSING || (University of Ruhuna)', 'NURSING || (Eastern University, Sri Lanka)', 'PHARMACY || (University of Peradeniya)', 'PHARMACY || (University of Sri Jayewardenepura)', 'PHARMACY || (University of Jaffna)', 'PHARMACY || (University of Ruhuna)', 'MEDICAL LABORATORY SCIENCES || (University of Peradeniya)', 'MEDICAL LABORATORY SCIENCES || (University of Sri Jayewardenepura)', 'MEDICAL LABORATORY SCIENCES || (University of Jaffna)', 'MEDICAL LABORATORY SCIENCES || (University of Ruhuna)', 'RADIOGRAPHY || (University of Peradeniya)', 'PHYSIOTHERAPY || (University of Colombo)', 'PHYSIOTHERAPY || (University of Peradeniya)', 'OCCUPATIONAL THERAPY || (University of Kelaniya)', 'OPTOMETRY || (University of Sri Jayewardenepura)', 'ENVIRONMENTAL CONSERVATION & MANAGEMENT || (University of Kelaniya)', 'APPLIED CHEMISTRY || (University of Kelaniya)', 'ELECTRONICS AND COMPUTER SCIENCE || (University of Kelaniya)', 'ACCOUNTING INFORMATION SYSTEMS || (University of Kelaniya)', 'FISHERIES & MARINE SCIENCES || (University of Ruhuna)', 'MARINE AND FRESHWATER SCIENCES || (University of Ruhuna)', 'ANIMAL SCIENCE & FISHERIES || (University of Peradeniya)', 'FOOD PRODUCTION & TECHNOLOGY MANAGEMENT || (Wayamba University of Sri Lanka)', 'FOOD BUSINESS MANAGEMENT || (Sabaragamuwa University of Sri Lanka)', 'MANAGEMENT AND INFORMATION TECHNOLOGY || (South Eastern University of Sri Lanka)', 'COMPUTING & INFORMATION SYSTEMS || (Sabaragamuwa University of Sri Lanka)', 'PHYSICAL EDUCATION || (University of Jaffna)', 'PHYSICAL EDUCATION || (Sabaragamuwa University of Sri Lanka)', 'SPORTS SCIENCE & MANAGEMENT || (University of Sri Jayewardenepura)', 'SPORTS SCIENCE & MANAGEMENT || (University of Kelaniya)', 'SPORTS SCIENCE & MANAGEMENT || (Sabaragamuwa University of Sri Lanka)', 'SPEECH AND HEARING SCIENCES || (University of Kelaniya)', 'TOURISM & HOSPITALITY MANAGEMENT || (Rajarata University of Sri Lanka)', 'TOURISM & HOSPITALITY MANAGEMENT || (Sabaragamuwa University of Sri Lanka)', 'AGRICULTURAL RESOURCE MANAGEMENT AND TECHNOLOGY || (University of Ruhuna)', 'AGRI BUSINESS MANAGEMENT || (University of Ruhuna)', 'GREEN TECHNOLOGY || (University of Ruhuna)', 'SCIENCE AND TECHNOLOGY || (Uva Wellassa University of Sri Lanka)', 'COMPUTER SCIENCE & TECHNOLOGY || (Uva Wellassa University of Sri Lanka)', 'ENTREPRENEURSHIP AND MANAGEMENT || (Uva Wellassa University of Sri Lanka)', 'ANIMAL PRODUCTION AND FOOD TECHNOLOGY || (Uva Wellassa University of Sri Lanka)', 'EXPORT AGRICULTURE || (Uva Wellassa University of Sri Lanka)', 'TEA TECHNOLOGY & VALUE ADDITION || (Uva Wellassa University of Sri Lanka)', 'INDUSTRIAL INFORMATION TECHNOLOGY || (Uva Wellassa University of Sri Lanka)', 'MINERAL RESOURCES AND TECHNOLOGY || (Uva Wellassa University of Sri Lanka)', 'AQUATIC RESOURCES TECHNOLOGY || (Uva Wellassa University of Sri Lanka)', 'PALM AND LATEX TECHNOLOGY & VALUE ADDITION || (Uva Wellassa University of Sri Lanka)', 'HOSPITALITY, TOURISM AND EVENTS MANAGEMENT || (Uva Wellassa University of Sri Lanka)', 'ENGLISH LANGUAGE & APPLIED LINGUISTICS || (Uva Wellassa University of Sri Lanka)', 'ENGINEERING TECHNOLOGY (ET) || (University of Colombo)', 'ENGINEERING TECHNOLOGY (ET) || (University of Sri Jayewardenepura)', 'ENGINEERING TECHNOLOGY (ET) || (University of Kelaniya)', 'ENGINEERING TECHNOLOGY (ET) || (University of Jaffna)', 'ENGINEERING TECHNOLOGY (ET) || (University of Ruhuna)', 'ENGINEERING TECHNOLOGY (ET) || (Rajarata University of Sri Lanka)', 'ENGINEERING TECHNOLOGY (ET) || (Sabaragamuwa University of Sri Lanka)', 'ENGINEERING TECHNOLOGY (ET) || (Wayamba University of Sri Lanka)', 'ENGINEERING TECHNOLOGY (ET) || (Uva Wellassa University of Sri Lanka)', 'BIOSYSTEMS TECHNOLOGY (BST) || (University of Colombo)', 'BIOSYSTEMS TECHNOLOGY (BST) || (University of Sri Jayewardenepura)', 'BIOSYSTEMS TECHNOLOGY (BST) || (University of Jaffna)', 'BIOSYSTEMS TECHNOLOGY (BST) || (University of Ruhuna)', 'BIOSYSTEMS TECHNOLOGY (BST) || (Eastern University, Sri Lanka)', 'BIOSYSTEMS TECHNOLOGY (BST) || (South Eastern University of Sri Lanka)', 'BIOSYSTEMS TECHNOLOGY (BST) || (Rajarata University of Sri Lanka)', 'BIOSYSTEMS TECHNOLOGY (BST) || (Sabaragamuwa University of Sri Lanka)', 'BIOSYSTEMS TECHNOLOGY (BST) || (Wayamba University of Sri Lanka)', 'BIOSYSTEMS TECHNOLOGY (BST) || (Uva Wellassa University of Sri Lanka)', 'INFORMATION COMMUNICATION TECHNOLOGY || (University of Colombo)', 'INFORMATION COMMUNICATION TECHNOLOGY || (University of Sri Jayewardenepura)', 'INFORMATION COMMUNICATION TECHNOLOGY || (University of Kelaniya)', 'INFORMATION COMMUNICATION TECHNOLOGY || (University of Ruhuna)', 'INFORMATION COMMUNICATION TECHNOLOGY || (South Eastern University of Sri Lanka)', 'INFORMATION COMMUNICATION TECHNOLOGY || (Rajarata University of Sri Lanka)', 'ARTS-INFORMATION TECHNOLOGY || (University of Sri Jayewardenepura)', 'AQUATIC BIORESOURCES || (University of Sri Jayewardenepura)', 'URBAN BIORESOURCES || (University of Sri Jayewardenepura)', 'SOCIAL WORK || (University of Peradeniya)', 'HUMAN RESOURCE DEVELOPMENT || (Uva Wellassa University of Sri Lanka)', 'MANAGEMENT STUDIES (TV) - A || (University of Vavuniya, Sri Lanka)', 'MANAGEMENT STUDIES (TV) - A || (Eastern University - Trincomalee Campus)', 'MANAGEMENT STUDIES (TV) - B || (University of Vavuniya, Sri Lanka)', 'MANAGEMENT STUDIES (TV) - B || (Eastern University - Trincomalee Campus)', 'COMMUNICATION STUDIES || (Eastern University - Trincomalee Campus)', 'FINANCIAL ECONOMICS || (University of Sri Jayewardenepura)', 'CREATIVE MUSIC TECHNOLOGY & PRODUCTION || (University of Sri Jayewardenepura)', 'PEACE & CONFLICT RESOLUTION || (University of Kelaniya)', 'ISLAMIC STUDIES || (South Eastern University of Sri Lanka)', 'ARABIC LANGUAGE || (South Eastern University of Sri Lanka)', 'ARCHITECTURE || (University of Moratuwa)', 'DESIGN || (University of Moratuwa)', 'LANDSCAPE ARCHITECTURE || (University of Moratuwa)', 'TOWN & COUNTRY PLANNING || (University of Moratuwa)', 'FASHION DESIGN & PRODUCT DEVELOPMENT || (University of Moratuwa)', 'ARTIFICIAL INTELLIGENCE || (University of Moratuwa)', 'INFORMATION TECHNOLOGY (IT) || (University of Moratuwa)', 'INFORMATION TECHNOLOGY & MANAGEMENT || (University of Moratuwa)', 'FACILITIES MANAGEMENT || (University of Moratuwa)', 'TRANSPORT MANAGEMENT & LOGISTICS ENGINEERING (TMLE) || (University of Moratuwa)', 'BUSINESS SCIENCE || (University of Moratuwa)', 'MANAGEMENT AND INFORMATION TECHNOLOGY (MIT) || (University of Kelaniya)', 'INDUSTRIAL STATISTICS & MATHEMATICAL FINANCE || (University of Colombo)', 'FINANCIAL MATHEMATICS AND INDUSTRIAL STATISTICS || (University of Ruhuna)', 'STATISTICS & OPERATIONS RESEARCH || (University of Peradeniya)', 'GEOGRAPHICAL INFORMATION SCIENCE || (University of Peradeniya)', 'INFORMATION AND COMMUNICATION TECHNOLOGY (ICT) || (Rajarata University of Sri Lanka)', 'INFORMATION AND COMMUNICATION TECHNOLOGY (ICT) || (University of Vavuniya, Sri Lanka)', 'INFORMATION SYSTEMS || (University of Colombo School of Computing)', 'INFORMATION SYSTEMS || (University of Sri Jayewardenepura)', 'SOFTWARE ENGINEERING || (University of Kelaniya)', 'SOFTWARE ENGINEERING || (Sabaragamuwa University of Sri Lanka)', 'SOFTWARE ENGINEERING || (University of Sri Jayewardenepura)', 'AYURVEDIC MEDICINE & SURGERY || (Institute of Indigenous Medicine)', 'AYURVEDIC MEDICINE & SURGERY || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'UNANI MEDICINE & SURGERY || (Institute of Indigenous Medicine)', 'SIDDHA MEDICINE & SURGERY || (University of Jaffna)', 'SIDDHA MEDICINE & SURGERY || (Eastern University - Trincomalee Campus)', 'INDIGENOUS MEDICINAL RESOURCES || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'HEALTH INFORMATION AND COMMUNICATION TECHNOLOGY || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'HEALTH TOURISM AND HOSPITALITY MANAGEMENT || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'BIOMEDICAL TECHNOLOGY || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'INDIGENOUS PHARMACEUTICAL TECHNOLOGY || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'YOGA AND PARAPSYCHOLOGY || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'SOCIAL STUDIES IN INDIGENOUS KNOWLEDGE || (The Gampaha Wickramarachchi University of Indigenous Medicine, Sri Lanka)', 'HEALTH PROMOTION || (Rajarata University of Sri Lanka)', 'NURSING || (University of Colombo)', 'BIOLOGICAL SCIENCE || (University of Peradeniya)', 'BIOLOGICAL SCIENCE || (University of Sri Jayewardenepura)', 'BIOLOGICAL SCIENCE || (University of Kelaniya)', 'BIOLOGICAL SCIENCE || (University of Jaffna)', 'BIOLOGICAL SCIENCE || (University of Ruhuna)', 'BIOLOGICAL SCIENCE || (Eastern University, Sri Lanka)', 'BIOLOGICAL SCIENCE || (South Eastern University of Sri Lanka)', 'APPLIED SCIENCES (Biological Science) || (Rajarata University of Sri Lanka)', 'APPLIED SCIENCES (Biological Science) || (Sabaragamuwa University of Sri Lanka)', 'APPLIED SCIENCES (Biological Science) || (University of Vavuniya, Sri Lanka)', 'ENGINEERING || (University of Peradeniya)', 'ENGINEERING || (University of Sri Jayewardenepura)', 'ENGINEERING || (University of Jaffna)', 'ENGINEERING || (University of Ruhuna)', 'ENGINEERING || (University of Moratuwa)', 'ENGINEERING || (South Eastern University of Sri Lanka)', 'ENGINEERING (EM) || (University of Moratuwa)', 'ENGINEERING (TM) || (University of Moratuwa)', 'QUANTITY SURVEYING || (University of Moratuwa)', 'COMPUTER SCIENCE || (University of Kelaniya)', 'COMPUTER SCIENCE || (University of Jaffna)', 'COMPUTER SCIENCE || (University of Ruhuna)', 'COMPUTER SCIENCE || (University of Colombo School of Computing)', 'COMPUTER SCIENCE || (Eastern University - Trincomalee Campus)', 'COMPUTER SCIENCE || (University of Sri Jayewardenepura)', 'PHYSICAL SCIENCE || (University of Colombo)', 'PHYSICAL SCIENCE || (University of Peradeniya)', 'PHYSICAL SCIENCE || (University of Sri Jayewardenepura)', 'PHYSICAL SCIENCE || (University of Kelaniya)', 'PHYSICAL SCIENCE || (University of Jaffna)', 'PHYSICAL SCIENCE || (University of Ruhuna)', 'PHYSICAL SCIENCE || (Eastern University, Sri Lanka)', 'PHYSICAL SCIENCE || (South Eastern University of Sri Lanka)', 'SURVEYING SCIENCE || (Sabaragamuwa University of Sri Lanka)', 'APPLIED SCIENCES (Physical Science) || (Rajarata University of Sri Lanka)', 'APPLIED SCIENCES (Physical Science) || (Sabaragamuwa University of Sri Lanka)', 'APPLIED SCIENCES (Physical Science) || (Wayamba University of Sri Lanka)', 'APPLIED SCIENCES (Physical Science) || (University of Vavuniya, Sri Lanka)', 'APPLIED SCIENCES (Physical Science) || (Eastern University - Trincomalee Campus)', 'MANAGEMENT || (University of Colombo)', 'MANAGEMENT || (University of Peradeniya)', 'MANAGEMENT || (University of Sri Jayewardenepura)', 'MANAGEMENT || (University of Kelaniya)', 'MANAGEMENT || (University of Jaffna)', 'MANAGEMENT || (University of Ruhuna)', 'MANAGEMENT || (Eastern University, Sri Lanka)', 'MANAGEMENT || (South Eastern University of Sri Lanka)', 'MANAGEMENT || (Rajarata University of Sri Lanka)', 'MANAGEMENT || (Sabaragamuwa University of Sri Lanka)', 'MANAGEMENT || (Wayamba University of Sri Lanka)']

# read the Zscores 
    district_index = locations.index(district)
    file = open("DataFiles/zScore.csv", "r")

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
    s1 = s1.strip()
    s2 = s2.strip()
    s3 = s3.strip()
    
    file_subject_req = open("DataFiles/data_file")
    main_file_lines = file_subject_req.readlines()
    
    cap_subjects = []

    for i in range(len(main_file_lines)):
        
        if "$" not in main_file_lines[i]:
            # $ not # not
            if "#" not in main_file_lines[i]:
                ## only sets not mandadary subjects
                Main_sets = main_file_lines[i].split("||")[1].split(",")
                for iiiiiii in range(len(Main_sets)):
                    Main_sets[iiiiiii] =Main_sets[iiiiiii].strip()
                if (s1 in Main_sets)and(s2 in Main_sets)and (s3 in Main_sets):
                    cap_subjects.append(main_file_lines[i].split("||")[0].strip())
            else:
                        Main_splitted =  main_file_lines[i].split("||")[1]
                        my_sub = [s1,s2,s3]
                        my_sub2 = [s1,s2,s3]
                        split_subs_mand_or_not = Main_splitted.split("#")
                        mand = split_subs_mand_or_not[0].split(",")
                        opt = split_subs_mand_or_not[1].split(",")
                        for ssss in range(len(mand)):
                           mand[ssss]= mand[ssss].strip()
                            
                        for kkkk in range(len(opt)):
                            opt[kkkk]= opt[kkkk].strip()
                        
                        #Have mandadary subjects s2,s3
                        #have specific subjects s1,s2,s3
                        for mys in my_sub2:
                            if mys in mand:
                                my_sub.pop(my_sub.index(mys))
                                mand.pop(mand.index(mys))
                                if len(mand) == 0 :
                                    for sub_opt in my_sub2:
                                        try:
                                                my_sub.pop(my_sub.index(sub_opt))
                                        except:
                                                pass
                                        if len(my_sub)==0:
                                            cap_subjects.append(main_file_lines[i].split("||")[0].strip())   
                                            break          
            # $ have # have
        else:
                # $ have
                
                sub_sets = main_file_lines[i].split("||")[1].split("$")
                for  subset_iter_number_dolor in range(len(sub_sets)):
                    # $ have # not
                    if "#" not in sub_sets[ subset_iter_number_dolor]:
                        split_subs = sub_sets[ subset_iter_number_dolor].split(",")
                        for bkkk in range(len(split_subs)):
                            split_subs[bkkk] = split_subs[bkkk].strip()
                        
                        if (s1 in split_subs) and (s2 in split_subs) and (s3 in split_subs):
                            cap_subjects.append(main_file_lines[i].split("||")[0].strip())
                            break
                    
                     # $ have # have
                    else:
                        my_sub = [s1,s2,s3]
                        my_sub2 = [s1,s2,s3]
                        split_subs_mand_or_not = sub_sets[ subset_iter_number_dolor].split("#")
                        mand = split_subs_mand_or_not[0].split(",")
                        opt = split_subs_mand_or_not[1].split(",")
                        for ssss in range(len(mand)):
                           mand[ssss]= mand[ssss].strip()
                            
                        for kkkk in range(len(opt)):
                            opt[kkkk]= opt[kkkk].strip()
                        
                        #ex man s2,s3
                        #have s1,s2,s3
                        for mys in my_sub2:
                            if mys in mand:
                                my_sub.pop(my_sub.index(mys))
                                mand.pop(mand.index(mys))
                                if len(mand) == 0 :
                                    for sub_opt in my_sub2:
                                        if sub_opt in opt:
                                            try:
                                                my_sub.pop(my_sub.index(sub_opt))
                                            except:
                                                pass
                                        if len(my_sub)==0:
                                            cap_subjects.append(main_file_lines[i].split("||")[0].strip())
                                            break 
                        if (main_file_lines[i].split("||")[0].strip()) in cap_subjects:
                            break
                        
        

    return cap_subjects


def Main(ss1, ss2, ss3, district, zScr, bais=0.4):
    com = []
    sub_pos = subs(ss1, ss2, ss3)
    z_pos = zScore(district, zScr + bais)
    for i in z_pos:
        if i.split("||")[0].strip() in sub_pos:
            com.append(i)
       
            

    return com


def stru_json(com):
    converted_data = []

    for item in com:
        category, university_and_amount = item.split("||")
        university, amount = university_and_amount.split(" $ ")
        university = university.replace("(","").replace(")","").strip()
        amount = float(amount)
        converted_data.append({'category': f"{category}", 'university': f"{university}", 'z-score': f'{amount}'})

    return converted_data


def json_out(json_not_stuc):
    json_data_cleaned2 = json_not_stuc.replace('\n', '').replace('\"', '')
    json_data_cleaned = json_data_cleaned2.replace('    ', '')

    return json_data_cleaned


if __name__ == "__main__":
    Distric = "RATNAPURA"
    z = 1.372
     #Bais is add to the Zscore  
    Bais = 0.04
    s1 = "PHYSICS"
    s2 = "HIGHER MATHEMATICS"
    s3 = "CHEMISTRY"
    
    print(stru_json(Main(s1,s3,s2,Distric,z,Bais)))