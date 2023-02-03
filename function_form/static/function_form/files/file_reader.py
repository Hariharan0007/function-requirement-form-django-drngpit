# from docx import Document 


dict = {'lunch_required_time': '00:30', 
        'refreshment_for_guest_number': None, 
        'reception_item_rec': 'Flowers', 
        'payment_through': 'Association Account', 
        'table_cloth_number': '1', 
        'spl_lunch_veg': '0', 
        'tiffin': '0', 
        'mic_arrangement': 'yes', 
        'chief_guest_name': 'Hariharan', 
        'func_name': 'Python training', 
        'laptop': 'yes', 
        'designation': 'College', 
        'dias': '5', 
        'transport_drop_time': None, 
        'refreshment_student_tea': None, 
        'field_type': 'College', 
        'guest_house_pesons': '',
        'normal_lunch' : '0', 
        'transport_pickup_person_contact': None, 
        'func_students_year_course': 'III-CSE-A & B', 
        'time_duration_end': '3:30 PM', 
        'photography': 'yes',
        'venue': 'Seminar hall(D-Block 1st Floor)',
        'refreshment_guest_snacks': None,
        'transport_req_date': None,
        'training_type': 'Software',
        'organizer_mail_id': 'hari@drngpit.ac.in',
        'seating_arrangement_numbers': '150',
        'func_date': '2022-11-15', 
        'transport_req': 'No', 
        'audience': '200', 
        'func_days': '1', 
        'lunch_exact_numbers': '12000', 
        'organizer_name': 'HHP', 
        'ac_arrangement': 'yes', 
        'refreshment_for_guest': 'No', 
        'transport_pickup_time': '9:00', 
        'lcd_projector': 'yes', 
        'transport_pickup_person_name': None, 
        'refreshment_for_student': 'No', 
        'spl_lunch_non_veg': '0', 
        'organizer_contact': '123456789', 
        'type_of_mic': 'Wired Mic', 
        'memento': 'yes', 
        'func_students': '150', 
        'guest_house_days': '', 
        'refreshment_guest_tea': None, 
        'dept_name': 'CSE', 
        'mic_number': '5',  
        'mic_arrangement': 'yes', 
        'tiffin': '0', 
        'table_cloth_number': '1', 
        'chief_guest_name': 'Hariharan', 
        'func_name': 'Trainee', 
        'laptop': 'yes', 'designation': 
        'College', 'dias': '5', 
        'transport_drop_time': '12:58', 
        'refreshment_student_tea': None, 
        'field_type': 'Industry', 
        'guest_house_persons': '2', 
        'transport_pickup_person_contact': '123456789', 
        'func_students_year_course': 'II-CSE-A & B', 
        'time_duration_end': '12:30 AM', 
        'photography': 'yes', 
        'venue': 'West seminar hall(A-Block)', 
        'refreshment_guest_snacks': None, 
        'transport_req_date': '2022-11-19', 
        'training_type': 'Software', 
        'organizer_mail_id': 'hari@drngpit.ac.in', 
        'seating_arrangement_numbers': '400', 
        'organizer_name': 'HHP', 
        'transport_req': 'Yes', 
        'audience': '500', 
        'func_days': '2',  
        'func_date': '2022-11-23', 
        'ac_arrangement': 'yes', 
        'refreshment_for_guest': 'Yes',  
        'lcd_projector': 'yes', 
        'transport_pickup_person_name': 'Hari', 
        'refreshment_for_guest_time': '10:20', 
        'refreshment_for_student': 'Yes', 
        'spl_lunch_non_veg': '0', 
        'guest_house_days': '1', 
        'type_of_mic': 'Wired Mic', 
        'memento': 'yes',
        'memento_worth':'2000',
        'memento_quantity':'1', 
        'func_students': '200', 
        'organizer_contact': '9865364629', 
        'refreshment_guest_tea': None, 
        'dept_name': 'CSE', 
        'mic_number': '5', 
        'refreshment_guest_coffee': None, 
        'time_duration_start': '10:20 AM', 
        'refreshment_student_snacks': None, 
        'refreshment_student_coffee': None, 
        'guest_house': 'Yes', 
        'refreshment_for_student_number': '0', 
        'transport_location': 'chitra',
        'guest_house_from_date':'10/11/2022',
        'guest_house_to_date':'10/11/2022',
        'refreshment_guest_tea' : '0',
        'refreshment_guest_coffee' : '0',
        'refreshment_guest_snacks' : '3',
        'refreshment_student_coffee' : '10',
        'refreshment_student_tea' : '10',
        'refreshment_student_snacks':'10',
        'refreshment_for_student_time' : '00:10',
        'transport_students':'No',
        'transport_students_stage':'--',
        'transport_students_number':'--',
        'status':'waiting',
        'time_stamp' : '12/29/2022, 08:36:22'}

d_list = []
for dit in dict:
        d_list.append(dit)
d_list.sort()

# print(d_list)

for dit in d_list:
        print(dit + " = request.POST.get(\'" + dit + "\')")
        # laptop = request.POST.get('laptop')

"""
var text = $('input[name="text"]').val();
var text_label = $('label[for="text"]').text();
var text_data = '<p><strong>' + text_label + '</strong> : ' + text + '</p>';
"""

# for dit in dict:
#         val_str = "var "+ dit + "= $(\'input[name=\""+dit+"\"]\').val();"
#         # print("var "+ dit + "= $(\'input[name=\""+dit+"\"]\').val();")
#         print(val_str)
#         label_str = "var "+ dit + "_label = $(\'label[for=\"" + dit +"\"]\').text();"
#         # print("var "+ dit + "= $(\'label[for=\"" + dit +"\"]\').text();")
#         print(label_str)
#         print("var "+ dit + "_data = \'<p><strong>\' + " + dit + "_label + \'</strong> : \' + " + dit + "<")


# doc = Document('C:\\functional requirement form\\static\\form.docx')

# for key in dict:
#         # print("run.text = dict[\'",key,"\'] if string==\"",key,"\" else continue")
#         print(key)


        

# for para in doc.paragraphs:
#         for run in para.runs:
#                 # print(run.text.strip(' ')+">##")
#                 string = run.text.strip(' ')
#                 string = string.strip("        ")
#                 print(string+">##")
#                 temp = []
#                 for i in string.split(' '):
#                         if i!='':
#                                 temp.append(i)
#                 print(temp)
#                 temp_str = ""
#                 for string in temp:
#                         if string=="ac_ar":
#                                 temp_str +=  dict['ac_arrangement']
#                         elif string=="audi":
#                                 temp_str +=  dict['audience']
#                         elif string=="cgn":
#                                 temp_str +=  dict['chief_guest_name']
#                         elif string=="dept_name":
#                                 temp_str +=  dict['dept_name']
#                         elif string=="dsg":
#                                 temp_str +=  dict['designation']
#                         elif string=="dias":
#                                 temp_str +=  dict['dias']
#                         elif string=="field_t":
#                                 temp_str +=  dict['field_type']
#                         elif string=="func_date":
#                                 temp_str +=  dict['func_date']
#                         elif string=="func_days":
#                                 temp_str +=  dict['func_days'] + " days"
#                         elif string=="func_name":
#                                 temp_str +=  dict['func_name']
#                         elif string=="func_stud":
#                                 temp_str +=  dict['func_students']
#                         elif string=="fsyc":
#                                 temp_str +=  dict['func_students_year_course']
#                         elif string=="gh":
#                                 temp_str +=  dict['guest_house']
#                         elif string=="ghd":
#                                 temp_str +=  dict['guest_house_days']
#                         elif string=="ghp":
#                                 temp_str +=  dict['guest_house_persons']
#                         elif string=="gh_f_dt":
#                                 temp_str +=  dict['guest_house_from_date']
#                         elif string=="gh_t_dt":
#                                 temp_str +=  dict['guest_house_to_date']
#                         elif string.strip(' ')=="lrt":
#                                 temp_str +=  " " + dict['lunch_required_time']
#                         elif string=="ltp":
#                                 temp_str +=  dict['laptop']
#                         elif string=="lcd_ar":
#                                 temp_str +=  dict['lcd_projector']
#                         elif string=="le_num":
#                                 temp_str +=  " " + dict['lunch_exact_numbers']
#                         elif string=="memento":
#                                 temp_str +=  dict['memento']
#                         elif string=="m_w":
#                                 temp_str += " " + dict['memento_worth']
#                         elif string=="m_q":
#                                 temp_str += " " + dict['memento_quantity'] 
#                         elif string.strip(' ')=="m_ar":
#                                 temp_str +=  "           "+ dict['mic_arrangement']+"        "
#                         elif string.strip(' ')=="mic_n":
#                                 temp_str +=  dict['mic_number']
#                         elif string.strip(' ')=="nm_lh":
#                                 temp_str +=  " " + dict['normal_lunch']
#                         elif string=="oc":
#                                 temp_str +=  dict['organizer_contact']
#                         elif string=="org_name":
#                                 temp_str +=  dict['organizer_name']
#                         elif string=="pymt":
#                                 temp_str +=  dict['payment_through']
#                         elif string=="pic":
#                                 temp_str +=  dict['photography']
#                         elif string=="reception_item_req":
#                                 temp_str +=  dict['reception_item_rec']
#                         elif string=="r_g":
#                                 temp_str +=  dict['refreshment_for_guest'] + "   " + "Tea : " + dict['refreshment_guest_tea'] + "    " + "Coffee : " + dict['refreshment_guest_coffee'] + "      " + "Snacks : " + dict['refreshment_guest_snacks']
#                         elif string=="-gtm-":
#                                 temp_str +="           : " +  dict['refreshment_for_guest_time']
#                         elif string=="-rs-":
#                                 temp_str +=  dict['refreshment_for_student'] + "   " + "Tea : " + dict['refreshment_student_tea'] + "    " + "Coffee : " + dict['refreshment_student_coffee'] + "      " + "Snacks : " + dict['refreshment_student_snacks']
#                         # elif string=="-":
#                         #         temp_str +=" "
#                         elif string=="--s-":
#                                 temp_str +=  " " + dict['refreshment_for_student_time']
#                         elif string=="san":
#                                 temp_str +=  dict['seating_arrangement_numbers']
#                         elif string.strip(' ')=="l_n_v":
#                                 temp_str +=  " " + dict['spl_lunch_non_veg']
#                         elif string.strip(' ')=="l_v":
#                                 temp_str +=  " "+ dict['spl_lunch_veg']
#                         elif string=="tcn":
#                                 temp_str +=  dict['table_cloth_number']
#                         elif string=="tiffin":
#                                 temp_str +=  dict['tiffin']
#                         elif string=="tm_d_e":
#                                 temp_str +=  dict['time_duration_end']
#                         elif string=="tm_d_s":
#                                 temp_str +=  dict['time_duration_start']
#                         elif string=="tn_t":
#                                 temp_str +=  dict['training_type']
#                         elif string=="tr_pk_tm":
#                                 temp_str +=  dict['transport_pickup_time']
#                         elif string=="tr_dp_tm":
#                                 temp_str +=  dict['transport_drop_time']
#                         elif string=="tr_loc":
#                                 temp_str +=  dict['transport_location']
#                         elif string=="tr_pc":
#                                 temp_str +=  dict['transport_pickup_person_contact']
#                         elif string=="tr_nm":
#                                 temp_str +=  dict['transport_pickup_person_name'] + " & "
#                         elif string=="tr_rec":
#                                 temp_str +=  dict['transport_req']
#                         elif string=="tr_rq_dt":
#                                 temp_str +=  dict['transport_req_date']
#                         elif string=="trs":
#                                 temp_str += dict['transport_students']
#                         elif string=="trs_s":
#                                 temp_str += dict['transport_students_stage'] + " & " + dict['transport_students_number']
#                         elif string.strip(' ')=="mic_type":
#                                 temp_str +=  dict['type_of_mic']+" & "
#                         elif string=="venue":
#                                 temp_str +=  dict['venue']
#                         else:
#                                 pass
#                 if temp_str!="":
#                         run.text = temp_str
                
                        
                                
                
# doc.save(dict['func_name']+".docx")