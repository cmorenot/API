from django.db import models

# Create your models here.


class Country(models.Model):
    id_country = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    code = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class StudentType(models.Model):
    id_student_class = models.CharField(primary_key=True, max_length=1024)
    kind = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'student_type'


class SciencEspecialty(models.Model):
    id_scienc_especialty = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'scienc_especialty'

class NationalCareer(models.Model):
    id_national_career = models.CharField(primary_key=True, max_length=1024)
    code = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    diploma = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    # scienc_especialty = models.CharField(max_length=1024, blank=True, null=True)
    scienc_especialty = models.ForeignKey(SciencEspecialty, models.DO_NOTHING, db_column='scienc_especialty_fk',
                                        blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'national_career'

class Province(models.Model):
    id_province = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    code = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'

class Town(models.Model):
    id_town = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    province = models.ForeignKey(Province, models.DO_NOTHING, db_column='province_fk',
                                        blank=True, null=True)
    code = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'town'


class Course(models.Model):
    id_course = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    matriculate_course = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class University(models.Model):
    id_university = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    initial = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    phone_number = models.CharField(max_length=1024, blank=True, null=True)
    fax = models.CharField(max_length=1024, blank=True, null=True)
    rector_name = models.CharField(max_length=1024, blank=True, null=True)
    general_secretary_name = models.CharField(max_length=1024, blank=True, null=True)
    graduation_date = models.DateField(blank=True, null=True)
    matriculation_begin_date = models.DateField(blank=True, null=True)
    matriculation_end_date = models.DateField(blank=True, null=True)
    rematriculation_begin_date = models.DateField(blank=True, null=True)
    rematriculation_end_date = models.DateField(blank=True, null=True)
    activities = models.CharField(max_length=1024, blank=True, null=True)
    logo = models.CharField(max_length=1024, blank=True, null=True)
    bylaw = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_fk', blank=True,
                             null=True)
    town = models.ForeignKey(Town, models.DO_NOTHING, db_column='town_fk', blank=True,
                             null=True)
    code = models.CharField(max_length=1024, blank=True, null=True)
    closure = models.BooleanField(blank=True, null=True)
    start = models.BooleanField(blank=True, null=True)
    promote = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university'


class TownUniversity(models.Model):
    id_town_university = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    initial = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    phone_number = models.CharField(max_length=1024, blank=True, null=True)
    fax = models.CharField(max_length=1024, blank=True, null=True)
    rector_name = models.CharField(max_length=1024, blank=True, null=True)
    general_secretary_name = models.CharField(max_length=1024, blank=True, null=True)
    graduation_date = models.DateField(blank=True, null=True)
    matriculation_end_date = models.DateField(blank=True, null=True)
    rematriculation_begin_date = models.DateField(blank=True, null=True)
    rematriculation_end_date = models.DateField(blank=True, null=True)
    matriculation_begin_date = models.DateField(blank=True, null=True)
    activities = models.CharField(max_length=1024, blank=True, null=True)
    logo = models.CharField(max_length=1024, blank=True, null=True)
    bylaw = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    town = models.ForeignKey(Town, models.DO_NOTHING, db_column='town_fk', blank=True,
                                        null=True)
    university = models.ForeignKey(University, models.DO_NOTHING, db_column='university_fk', blank=True,
                                        null=True)
    code = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'town_university'

class Faculty(models.Model):
    id_faculty = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    phone_number = models.CharField(max_length=1024, blank=True, null=True)
    dean_name = models.CharField(max_length=1024, blank=True, null=True)
    secretary_name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    town = models.ForeignKey(Town, models.DO_NOTHING, db_column='town_fk', blank=True,
                             null=True)
    university = models.ForeignKey(University, models.DO_NOTHING, db_column='university_fk', blank=True,
                                   null=True)
    code = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty'


class CourseType(models.Model):
    id_course_type = models.CharField(primary_key=True, max_length=1024)
    code = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    debts = models.IntegerField()
    cancelled = models.BooleanField()
    short_name = models.CharField(max_length=1024, blank=True, null=True)
    behavior = models.CharField(max_length=1024, blank=True, null=True)
    modality = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_type'


class Career(models.Model):
    id_career = models.CharField(primary_key=True, max_length=1024)
    cancelled = models.BooleanField()
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='faculty_fk',blank=True, null=True)
    town_university = models.ForeignKey(TownUniversity, models.DO_NOTHING, db_column='town_university_fk',blank=True, null=True)
    national_career = models.ForeignKey(NationalCareer, models.DO_NOTHING, db_column='national_career_fk',
                                           blank=True, null=True)
    course_type = models.ForeignKey(CourseType, models.DO_NOTHING, db_column='course_type_fk',
                                           blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'career'


class EntrySource(models.Model):
    id_entry_source = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'entry_source'





class ScholasticOrigin(models.Model):
    id_scholastic_origin = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'scholastic_origin'


class PoliticOrg(models.Model):
    id_politic_org = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'politic_org'


class Sex(models.Model):
    id_sex = models.CharField(primary_key=True, max_length=1024)
    kind = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sex'


class MaritalStatus(models.Model):
    id_marital_status = models.CharField(primary_key=True, max_length=1024)
    kind = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'marital_status'


class StudyRegimen(models.Model):
    id_study_regimen = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'study_regimen'


class StudentStatus(models.Model):
    id_student_status = models.CharField(primary_key=True, max_length=1024)
    kind = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'student_status'


class AcademicSituation(models.Model):
    id_academic_situation = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    student_status = models.ForeignKey(StudentStatus, models.DO_NOTHING, db_column='student_status_fk',
                                           blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_situation'


class SkinColor(models.Model):
    id_skin_color = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'skin_color'


class Orphan(models.Model):
    id_orphan = models.CharField(primary_key=True, max_length=1024)
    kind = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'orphan'


class Student(models.Model):
    id_student = models.CharField(primary_key=True, max_length=1024)
    identification = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    middle_name = models.CharField(max_length=1024, blank=True, null=True)
    last_name = models.CharField(max_length=1024, blank=True, null=True)
    native_of = models.CharField(max_length=1024, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    son_count = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    higher_education_in_date = models.DateField(blank=True, null=True)
    university_in_date = models.DateField(blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)
    scale = models.FloatField(blank=True, null=True)
    academic_index = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country_fk')
    student_type = models.ForeignKey(StudentType, models.DO_NOTHING, db_column='student_type_fk')
    career = models.ForeignKey(Career, models.DO_NOTHING, db_column='career_fk', blank=True, null=True)
    entry_source = models.ForeignKey(EntrySource, models.DO_NOTHING, db_column='entry_source_fk')
    course_type = models.ForeignKey(CourseType, models.DO_NOTHING, db_column='course_type_fk')
    scholastic_origin = models.ForeignKey(ScholasticOrigin, models.DO_NOTHING, db_column='scholastic_origin_fk')
    politic_org = models.ForeignKey(PoliticOrg, models.DO_NOTHING, db_column='politic_org_fk')
    sex = models.ForeignKey(Sex, models.DO_NOTHING, db_column='sex_fk')
    town_university = models.ForeignKey(TownUniversity, models.DO_NOTHING, db_column='town_university_fk', blank=True, null=True)
    marital_status = models.ForeignKey(MaritalStatus, models.DO_NOTHING, db_column='marital_status_fk')
    study_regimen = models.ForeignKey(StudyRegimen, models.DO_NOTHING, db_column='study_regimen_fk')
    academic_situation = models.ForeignKey(AcademicSituation, models.DO_NOTHING, db_column='academic_situation_fk')
    town = models.ForeignKey(Town, models.DO_NOTHING, db_column='town_fk', blank=True, null=True)
    skin_color = models.ForeignKey(SkinColor, models.DO_NOTHING, db_column='skin_color_fk')
    student_status = models.ForeignKey(StudentStatus, models.DO_NOTHING, db_column='student_status_fk', blank=True, null=True)
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='faculty_fk', blank=True, null=True)
    orphan = models.ForeignKey(Orphan, models.DO_NOTHING, db_column='orphan_fk')
    photo = models.CharField(max_length=1024, blank=True, null=True)
    reoffer = models.BooleanField(blank=True, null=True)
    option = models.IntegerField(blank=True, null=True)
    block = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

    def hash_mod(self):
        return ''

    def year(self):
        return ''

class Xgroup(models.Model):
    id_group = models.CharField(primary_key=True, max_length=1024)
    name = models.CharField(max_length=1024, blank=True, null=True)
    cancelled = models.BooleanField()
    #group_type_fk = models.ForeignKey(GroupType, models.DO_NOTHING, db_column='group_type_fk', blank=True, null=True)
    #career_fk = models.ForeignKey(Career, models.DO_NOTHING, db_column='career_fk', blank=True, null=True)
    group_fk = models.ForeignKey('self', models.DO_NOTHING, db_column='group_fk', blank=True, null=True)
    #course_fk = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_fk', blank=True, null=True)
    #study_program_version_fk = models.ForeignKey(StudyProgramVersion, models.DO_NOTHING, db_column='study_program_version_fk', blank=True, null=True)
    # period_ini = models.IntegerField(blank=True, null=True)
    # period_end = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    # terminal = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xgroup'


class Groups2Students(models.Model):
    students_fk = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='students_fk', blank=True, null=True)

    groups_fk = models.ForeignKey(Xgroup, models.DO_NOTHING, db_column='groups_fk', blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=1024)

    consecutive = models.IntegerField(blank=True, null=True)
    # student_group_type_fk = models.ForeignKey('StudentGroupType', models.DO_NOTHING, db_column='student_group_type_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups2students'
        # unique_together = (('students_fk', 'groups_fk'),)