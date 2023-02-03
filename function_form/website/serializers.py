from rest_framework import serializers

from .models import admin_model,staff_model,function_model,venue_model,booking_model

class admin_serializer(serializers.ModelSerializer):

    class Meta:
        model = admin_model
        fields = ['email','admin_id']

class staff_serializer(serializers.ModelSerializer):

    class Meta:
        model = staff_model
        fields = ['email','staff_id']

class venue_serializer(serializers.ModelSerializer):

    class Meta:
        model = venue_model
        fields = ['venue']

class booking_serializer(serializers.ModelSerializer):

    class Meta:
        model = booking_model
        fields = ['venue','booking_date','starting_time','ending_time','status']

class function_serializer(serializers.ModelSerializer):

    class Meta:
        model = function_model
        fields = ['ac_arrangement', 'audience', 'chief_guest_name', 'dept_name', 'designation', 'dias', 'field_type', 'func_date', 'func_days', 'func_name', 'func_students', 'func_students_year_course', 'guest_house', 'guest_house_days', 'guest_house_from_date', 'guest_house_persons', 'guest_house_to_date', 'laptop', 'lcd_projector', 'lunch_exact_numbers', 'lunch_required_time', 'memento', 'memento_quantity', 'memento_worth', 'mic_arrangement', 'mic_number', 'normal_lunch', 'organizer_contact', 'organizer_mail_id', 'organizer_name', 'payment_through', 'photography', 'reception_item_rec', 'refreshment_for_guest', 'refreshment_for_guest_number', 'refreshment_for_guest_time', 'refreshment_for_student', 'refreshment_for_student_number', 'refreshment_for_student_time', 'refreshment_guest_coffee', 'refreshment_guest_snacks', 'refreshment_guest_tea', 'refreshment_student_coffee', 'refreshment_student_snacks', 'refreshment_student_tea', 'seating_arrangement_numbers', 'spl_lunch_non_veg', 'spl_lunch_veg', 'table_cloth_number', 'tiffin', 'time_duration_end', 'time_duration_start', 'training_type', 'transport_drop_time', 'transport_location', 'transport_pickup_person_contact', 'transport_pickup_person_name', 'transport_pickup_time', 'transport_req', 'transport_req_date', 'transport_students', 'transport_students_number', 'transport_students_stage', 'type_of_mic', 'venue','status','time_stamp','document_pdf']

        
# class function_serializer(serializers.ModelSerializer):

#     class Meta:
#         model = ""
#         fields = []
