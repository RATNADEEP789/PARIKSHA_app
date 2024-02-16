# Generated by Django 4.2.2 on 2023-08-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

 # Generated by Django 4.2.2 on 2023-08-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsMaster',
            fields=[
                ('fld_slno', models.AutoField(primary_key=True, serialize=False)),
                ('fld_rn', models.IntegerField(db_index=True, null=True)),
                ('fld_rf_id', models.IntegerField(db_index=True, null=True)),
                ('fld_total_exp_id', models.IntegerField(db_index=True, null=True)),
                ('fld_total_exp_name', models.CharField(db_index=True, max_length=250)),
                ('fld_post_applied_for_id', models.IntegerField(db_index=True, null=True)),
                ('fld_post_applied_for_name', models.CharField(db_index=True, max_length=250)),
                ('fld_question_number', models.IntegerField(db_index=True, null=True)),
                ('fld_question_text', models.TextField(db_index=True, null=True)),
                ('fld_option_id', models.IntegerField(db_index=True, null=True)),
                ('fld_option_name', models.TextField(db_index=True, null=True)),
                ('fld_correct_option_id', models.IntegerField(db_index=True, null=True)),
                ('fld_correct_option_name', models.TextField(db_index=True, null=True)),
                ('fld_is_active', models.CharField(db_index=True, max_length=2)),
                ('fld_sys_inserted_datetime', models.CharField(max_length=50)),
                ('fld_modified_no', models.IntegerField(null=True)),
                ('fld_modified_datetime', models.CharField(max_length=50, null=True)),
                ('fld_is_deleted', models.CharField(db_index=True, max_length=2, null=True)),
                ('fld_reason_for_delete', models.TextField(null=True)),
                ('fld_deletion_datetime', models.CharField(max_length=50, null=True)),
                ('fld_form_start_time', models.CharField(max_length=50, null=True)),
                ('fld_form_end_time', models.CharField(max_length=50, null=True)),
                ('fld_is_logged_in_user_id', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'questionsmaster',
            },
        ),
        migrations.CreateModel(
            name='registab',
            fields=[
                ('fld_slno', models.AutoField(primary_key=True, serialize=False)),
                ('fld_rn', models.IntegerField(db_index=True)),
                ('fld_rf_id', models.IntegerField(db_index=True)),
                ('full_name', models.CharField(db_index=True, max_length=50, null=True)),
                ('dateofbirth', models.DateField(max_length=8)),
                ('gender', models.CharField(db_index=True, max_length=250)),
                ('mobile_number', models.CharField(db_index=True, max_length=100, null=True)),
                ('email_id', models.TextField(db_index=True, null=True)),
                ('Expereince', models.CharField(db_index=True, max_length=250)),
                ('possition', models.CharField(db_index=True, max_length=250)),
                ('referd_by', models.CharField(db_index=True, max_length=250)),
                ('home_town', models.CharField(db_index=True, max_length=250)),
                ('Username', models.CharField(db_index=True, max_length=250)),
                ('password', models.CharField(db_index=True, max_length=250)),
                ('attempts', models.IntegerField(null=True)),
                ('fld_is_active', models.IntegerField(db_index=True)),
                ('fld_user_type', models.CharField(max_length=50)),
                ('fld_user_type_id', models.IntegerField(db_index=True)),
                ('sys_insert_datetime', models.CharField(max_length=100, null=True)),
                ('modified_no', models.IntegerField(db_index=True)),
                ('modified_datetime', models.CharField(max_length=100, null=True)),
                ('is_deleted', models.IntegerField(db_index=True, default=0)),
                ('reason_for_deleted', models.CharField(max_length=50)),
                ('deletion_datetime', models.CharField(max_length=100, null=True)),
                ('form_start_time', models.CharField(max_length=100, null=True)),
                ('form_end_time', models.CharField(max_length=100, null=True)),
                ('File', models.FileField(upload_to='media/resumes/')),
            ],
            options={
                'db_table': 'registab',
            },
        ),
        migrations.CreateModel(
            name='show_user_result',
            fields=[
                ('fld_slno', models.AutoField(primary_key=True, serialize=False)),
                ('fld_rn_id', models.IntegerField(db_index=True, null=True)),
                ('fld_rf_id', models.IntegerField(db_index=True, null=True)),
                ('fld_user_id', models.IntegerField(db_index=True, null=True)),
                ('fld_user_name', models.CharField(db_index=True, max_length=50, null=True)),
                ('fld_experience', models.CharField(db_index=True, max_length=250)),
                ('fld_post_applied_for_name', models.CharField(db_index=True, max_length=250)),
                ('fld_total_mark', models.IntegerField()),
                ('fld_user_result', models.IntegerField()),
                ('fld_user_percentage', models.FloatField()),
                ('fld_sys_inserted_datetime', models.CharField(max_length=50)),
                ('fld_is_active', models.IntegerField(db_index=True)),
                ('fld_is_deleted', models.CharField(db_index=True, max_length=2, null=True)),
                ('fld_is_deleted_by', models.CharField(db_index=True, max_length=2, null=True)),
                ('fld_reason_for_delete', models.TextField(null=True)),
                ('fld_is_logged_in_user', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'show_user_result',
            },
        ),
        migrations.CreateModel(
            name='trn_tbl_user_answered',
            fields=[
                ('fld_slno', models.AutoField(primary_key=True, serialize=False)),
                ('fld_rn_id', models.IntegerField(db_index=True, null=True)),
                ('fld_rf_id', models.IntegerField(db_index=True, null=True)),
                ('fld_user_id', models.IntegerField(db_index=True, null=True)),
                ('fld_user_name', models.CharField(db_index=True, max_length=50, null=True)),
                ('fld_experience', models.CharField(db_index=True, max_length=250)),
                ('fld_post_applied_for_name', models.CharField(db_index=True, max_length=250)),
                ('fld_question_text', models.TextField(db_index=True, null=True)),
                ('fld_correct_option_name', models.TextField(db_index=True, null=True)),
                ('fld_user_answer_name', models.TextField(db_index=True, null=True)),
                ('fld_total_mark', models.IntegerField()),
                ('fld_user_result', models.IntegerField()),
                ('fld_user_percentage', models.FloatField()),
                ('fld_sys_inserted_datetime', models.CharField(max_length=50)),
                ('fld_is_active', models.IntegerField(db_index=True)),
                ('fld_is_deleted', models.CharField(db_index=True, max_length=2, null=True)),
                ('fld_is_deleted_by', models.CharField(db_index=True, max_length=2, null=True)),
                ('fld_reason_for_delete', models.TextField(null=True)),
                ('fld_is_logged_in_user', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'trn_tbl_user_answered',
            },
        ),
    ]
