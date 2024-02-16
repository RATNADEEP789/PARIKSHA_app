from django.db import models
# Create your models here.
class registab(models.Model):
    fld_slno=models.AutoField(primary_key=True)
    fld_rn= models.IntegerField(db_indefrom django.db import models
# Create your models here.
class registab(models.Model):
    fld_slno=models.AutoField(primary_key=True)
    fld_rn= models.IntegerField(db_index=True,null=False)
    fld_rf_id= models.IntegerField(db_index=True,null=False)
    full_name= models.CharField(db_index=True,max_length=50, null=True)
    dateofbirth= models.DateField(max_length=8)
    gender=models.CharField(db_index=True,max_length=250, null=False)
    mobile_number= models.CharField(db_index=True,max_length=100, null=True)
    email_id=models.TextField(db_index=True,null=True)
    Expereince=models.CharField(db_index=True,max_length=250, null=False)
    possition=models.CharField(db_index=True,max_length=250, null=False)
    referd_by=models.CharField(db_index=True,max_length=250, null=False)
    home_town=models.CharField(db_index=True,max_length=250, null=False)
    Username=models.CharField(db_index=True,max_length=250, null=False)
    password=models.CharField(db_index=True,max_length=250, null=False)
    attempts= models.IntegerField(null=True)
    fld_is_active=models.IntegerField(db_index=True,null=False)
    fld_user_type=models.CharField(max_length=50,null=False)
    fld_user_type_id=models.IntegerField(db_index=True,null=False)
    sys_insert_datetime=models.CharField(max_length =100, null=True)
    modified_no=models.IntegerField(db_index=True,null=False)
    modified_datetime=models.CharField(max_length =100, null=True)
    is_deleted=models.IntegerField(db_index=True,null=False,default=0)
    reason_for_deleted=models.CharField(max_length=50,null=False)
    deletion_datetime=models.CharField(max_length =100, null=True)
    form_start_time=models.CharField(max_length =100, null=True)
    form_end_time=models.CharField(max_length =100, null=True)
    File=models.FileField(upload_to ='media/resumes/')
    class Meta:
        db_table = "registab"

class QuestionsMaster(models.Model):
    fld_slno = models.AutoField(primary_key=True)
    fld_rn = models.IntegerField(db_index=True,null=True)
    fld_rf_id = models.IntegerField(db_index=True,null=True,serialize=True)
    fld_total_exp_id = models.IntegerField(db_index=True,null=True,serialize=True)
    fld_total_exp_name =models.CharField(db_index=True,max_length=250, null=False)
    fld_post_applied_for_id = models.IntegerField(db_index=True,null=True,serialize=True)
    fld_post_applied_for_name = models.CharField(db_index=True,max_length=250, null=False)
    fld_question_number = models.IntegerField(db_index=True,null=True,serialize=True)
    fld_question_text = models.TextField(db_index=True, null=True)
    fld_option_id = models.IntegerField(db_index=True,null=True,serialize=True)
    fld_option_name = models.TextField(db_index=True, null=True)
    fld_correct_option_id = models.IntegerField(db_index=True,null=True,serialize=True)
    fld_correct_option_name = models.TextField(db_index=True, null=True)
    fld_is_active = models.CharField(db_index=True,max_length =2,null=False)
    fld_sys_inserted_datetime = models.CharField(max_length=50)
    fld_modified_no = models.IntegerField(null=True)
    fld_modified_datetime = models.CharField(max_length=50,null=True)
    fld_is_deleted = models.CharField(db_index=True,max_length =2, null=True)
    fld_reason_for_delete = models.TextField(null=True)
    fld_deletion_datetime = models.CharField(max_length=50,null=True)
    fld_form_start_time = models.CharField(max_length=50,null=True)
    fld_form_end_time = models.CharField(max_length=50,null=True)
    fld_is_logged_in_user_id = models.CharField(max_length=50,null=True)
    class Meta:
        db_table="questionsmaster"

    
class trn_tbl_user_answered(models.Model):
     fld_slno = models.AutoField(primary_key=True)
     fld_rn_id = models.IntegerField(db_index=True,null=True)
     fld_rf_id = models.IntegerField(db_index=True,null=True,serialize=True)
     fld_user_id = models.IntegerField(db_index=True,null=True,serialize=True)
     fld_user_name= models.CharField(db_index=True,max_length=50, null=True)
     fld_experience = models.CharField(db_index=True,max_length=250, null=False)
     fld_post_applied_for_name = models.CharField(db_index=True,max_length=250, null=False)
     fld_question_text =  models.TextField(db_index=True, null=True)
     fld_correct_option_name = models.TextField(db_index=True, null=True)
     fld_user_answer_name = models.TextField(db_index=True, null=True)
     fld_total_mark = models.IntegerField()
     fld_user_result = models.IntegerField()
     fld_user_percentage = models.FloatField()
     fld_sys_inserted_datetime = models.CharField(max_length=50)
     fld_is_active= models.IntegerField(db_index=True,null=False)
     fld_is_deleted = models.CharField(db_index=True,max_length =2, null=True)
     fld_is_deleted_by = models.CharField(db_index=True,max_length =2, null=True)
     fld_reason_for_delete = models.TextField(null=True)
     fld_is_logged_in_user = models.CharField(max_length=50,null=True)
     class Meta:
        db_table="trn_tbl_user_answered"

class show_user_result(models.Model):
     fld_slno = models.AutoField(primary_key=True)
     fld_rn_id = models.IntegerField(db_index=True,null=True)
     fld_rf_id = models.IntegerField(db_index=True,null=True,serialize=True)
     fld_user_id = models.IntegerField(db_index=True,null=True,serialize=True)
     fld_user_name= models.CharField(db_index=True,max_length=50, null=True)
     fld_experience = models.CharField(db_index=True,max_length=250, null=False)
     fld_post_applied_for_name = models.CharField(db_index=True,max_length=250, null=False)
     fld_total_mark = models.IntegerField()
     fld_user_result = models.IntegerField()
     fld_user_percentage = models.FloatField()
     fld_sys_inserted_datetime = models.DateTimeField()
     fld_is_active= models.IntegerField(db_index=True,null=False)
     fld_is_deleted = models.CharField(db_index=True,max_length =2, null=True)
     fld_is_deleted_by = models.CharField(db_index=True,max_length =2, null=True)
     fld_reason_for_delete = models.TextField(null=True)
     fld_is_logged_in_user = models.CharField(max_length=50,null=True)
     class Meta:
        db_table="show_user_result"

