from django.db import models


class admin_model(models.Model):
    email = models.EmailField(max_length=50,primary_key=True)
    admin_id = models.CharField(max_length=25)

    def __str__(self):
        return self.email + "   --  " + str(self.admin_id)

class staff_model(models.Model):
    email = models.EmailField(max_length=50,primary_key=True)
    staff_id = models.CharField(max_length=25)

    def __str__(self):
        return self.email+ "    --  " + str(self.staff_id)

class venue_model(models.Model):
    class Meta:
        unique_together = (('venue','capacity'))
    venue = models.CharField(max_length=60,primary_key=True)
    capacity = models.IntegerField(null=True)

    def __self__(self):
        return self.venue

class booking_model(models.Model):
    class Meta:
        unique_together = (('venue','booking_date','booking_end_date','month'),)
    venue = models.CharField(max_length=60)
    booking_date = models.DateField()
    booking_end_date = models.DateField(null=True)
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    month = models.CharField(max_length=25,null=True)
    func_days = models.IntegerField(null=True)
    status = models.CharField(max_length=25,null=True)
    
    def __str__(self):
        return self.venue + "   --  " + str(self.booking_date) + "  --  " + str(self.booking_end_date) + " -- " + self.month

class function_model(models.Model):
    ac_arrangement = models.CharField(max_length=5)
    audience = models.IntegerField()
    chief_guest_name = models.CharField(max_length=25)
    dept_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=20)
    dias = models.IntegerField()
    field_type = models.CharField(max_length=10)
    func_date = models.DateField()
    func_end_date = models.DateField(null=True)
    func_days = models.IntegerField()
    func_name = models.CharField(max_length=30,primary_key=True)
    func_students = models.IntegerField()
    func_students_external = models.IntegerField(null=True)
    func_students_external_class = models.CharField(max_length=100,null=True)
    func_students_year_course = models.CharField(max_length=30)
    guest_house = models.CharField(max_length=5)
    guest_house_days = models.IntegerField()
    guest_house_from_date = models.CharField(max_length=30)
    guest_house_persons = models.IntegerField()
    guest_house_to_date = models.CharField(max_length=30)
    laptop = models.CharField(max_length=5)
    lcd_projector = models.CharField(max_length=5)
    lunch_exact_numbers = models.IntegerField()
    lunch_required_time = models.CharField(max_length=30)
    memento = models.CharField(max_length=5)
    memento_quantity = models.IntegerField()
    memento_worth = models.IntegerField()
    mic_arrangement = models.CharField(max_length=5)
    mic_number = models.IntegerField()
    normal_lunch = models.IntegerField()
    organizer_contact = models.IntegerField()
    organizer_mail_id = models.EmailField(max_length=150)
    organizer_name = models.CharField(max_length=25)
    payment_through = models.CharField(max_length=35)
    photography = models.CharField(max_length=5)
    photographer = models.CharField(max_length=50,null=True)
    reception_item_rec = models.CharField(max_length=200)
    refreshment_for_guest = models.CharField(max_length=5)
    refreshment_for_guest_number = models.IntegerField()
    refreshment_for_guest_time = models.CharField(max_length=30)
    refreshment_for_student = models.CharField(max_length=5)
    refreshment_for_student_number = models.IntegerField()
    refreshment_for_student_time = models.CharField(max_length=30)
    refreshment_guest_coffee = models.IntegerField()
    refreshment_guest_snacks = models.IntegerField()
    refreshment_guest_tea = models.IntegerField()
    refreshment_student_coffee = models.IntegerField()
    refreshment_student_snacks = models.IntegerField()
    refreshment_student_tea = models.IntegerField()
    seating_arrangement_numbers = models.IntegerField()
    spl_lunch_non_veg = models.IntegerField()
    spl_lunch_veg = models.IntegerField()
    table_cloth_number = models.IntegerField()
    tiffin = models.IntegerField()
    time_duration_end = models.TimeField()
    time_duration_start = models.TimeField()
    training_type = models.CharField(max_length=50)
    transport_drop_time = models.CharField(max_length=30)
    transport_location = models.CharField(max_length=50)
    transport_pickup_person_contact = models.IntegerField()
    transport_pickup_person_name = models.CharField(max_length=50)
    transport_pickup_time = models.CharField(max_length=30)
    transport_req = models.CharField(max_length=5)
    transport_req_date = models.CharField(max_length=30)
    transport_students = models.CharField(max_length=5)
    transport_students_number = models.IntegerField()
    transport_students_stage = models.CharField(max_length=50)
    type_of_mic = models.CharField(max_length=20)
    venue = models.CharField(max_length=50)
    hod_status = models.CharField(max_length=25,null=True)
    status = models.CharField(max_length=25,null=True)
    principal_status = models.CharField(max_length=25,null=True)
    time_stamp = models.CharField(max_length=50,null=True)
    remarks = models.CharField(max_length=250,null=True)
    document_pdf = models.FileField(upload_to='media',null=True)

    def __str__(self):
        return self.organizer_mail_id + "   --  " + self.func_name 