from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from sigenu import serializers
from rest_framework.response import Response
from rest_framework import permissions
from sigenu.models import Student, EntrySource, Career, StudentType, Country ,AcademicSituation, \
    CourseType,Faculty, MaritalStatus,Orphan,PoliticOrg,ScholasticOrigin,Sex,SkinColor, \
    StudentStatus,StudyRegimen,Town,TownUniversity, Groups2Students, Xgroup
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#import passlib.hash
import hashlib



class StudentAllViewSet(viewsets.ModelViewSet):
    """Return all student, inactive and inactive"""
    queryset = Student.objects.using("sigenu_student").all()
    serializer_class = serializers.StudentSerializer


class StudentAllActiveViewSet(viewsets.ModelViewSet):
    """Return all student active"""
    queryset = Student.objects.using("sigenu_student").filter(student_status="02")
    serializer_class = serializers.StudentSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """Return all Country"""
    queryset = Country.objects.using("sigenu_student").all()
    serializer_class = serializers.CountrySerializer


class StudentTypeViewSet(viewsets.ModelViewSet):
    """Return all StudentType"""
    queryset = StudentType.objects.using("sigenu_student").all()
    serializer_class = serializers.StudentTypeSerializer


class CareerViewSet(viewsets.ModelViewSet):
    """Return all Career"""
    queryset = Career.objects.using("sigenu_student").all()
    serializer_class = serializers.CareerSerializer

class EntrySourceViewSet(viewsets.ModelViewSet):
    """Return all EntrySource"""
    queryset = EntrySource.objects.using("sigenu_student").all()
    serializer_class = serializers.EntrySourceSerializer


class CourseTypeViewSet(viewsets.ModelViewSet):
    """Return all CourseType"""
    queryset = CourseType.objects.using("sigenu_student").all()
    serializer_class = serializers.CourseTypeSerializer


class ScholasticOriginViewSet(viewsets.ModelViewSet):
    """Return all ScholasticOrigin"""
    queryset = ScholasticOrigin.objects.using("sigenu_student").all()
    serializer_class = serializers.ScholasticOriginSerializer


class PoliticOrgViewSet(viewsets.ModelViewSet):
    """Return all PoliticOrg"""
    queryset = PoliticOrg.objects.using("sigenu_student").all()
    serializer_class = serializers.PoliticOrgSerializer


class SexViewSet(viewsets.ModelViewSet):
    """Return all Sex"""
    queryset = Sex.objects.using("sigenu_student").all()
    serializer_class = serializers.SexSerializer


class TownUniversityViewSet(viewsets.ModelViewSet):
    """Return all TownUniversity"""
    queryset = TownUniversity.objects.using("sigenu_student").all()
    serializer_class = serializers.TownUniversitySerializer


class MaritalStatusViewSet(viewsets.ModelViewSet):
    """Return all MaritalStatus"""
    queryset = MaritalStatus.objects.using("sigenu_student").all()
    serializer_class = serializers.MaritalStatusSerializer

class StudyRegimenViewSet(viewsets.ModelViewSet):
    """Return all StudyRegimen"""
    queryset = StudyRegimen.objects.using("sigenu_student").all()
    serializer_class = serializers.StudyRegimenSerializer


class AcademicSituationViewSet(viewsets.ModelViewSet):
    """Return all AcademicSituation"""
    queryset = AcademicSituation.objects.using("sigenu_student").all()
    serializer_class = serializers.AcademicSituationSerializer


class TownSituationViewSet(viewsets.ModelViewSet):
    """Return all Town"""
    queryset = Town.objects.using("sigenu_student").all()
    serializer_class = serializers.TownSerializer


class SkinColorViewSet(viewsets.ModelViewSet):
    """Return all SkinColor"""
    queryset = SkinColor.objects.using("sigenu_student").all()
    serializer_class = serializers.SkinColorSerializer


class StudentStatusViewSet(viewsets.ModelViewSet):
    """Return all StudentStatus"""
    queryset = StudentStatus.objects.using("sigenu_student").all()
    serializer_class = serializers.StudentStatusSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    """Return all Faculty"""
    queryset = Faculty.objects.using("sigenu_student").all()
    serializer_class = serializers.FacultySerializer


class OrphanViewSet(viewsets.ModelViewSet):
    """Return all Orphan"""
    queryset = Orphan.objects.using("sigenu_student").all()
    serializer_class = serializers.OrphanSerializer


@csrf_exempt
def student_dni(request, ci):
    """Returns the active employee given a CI"""
    #92082643541
    try:
        student = Student.objects.using("sigenu_student").filter(identification=str(ci))
        print(ci)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serializers.StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        pass


def student_active_dni(request, ci):
    """Returns the active employee given a CI"""
    #92082643541
    try:
        student = Student.objects.using("sigenu_student").filter(identification=str(ci),student_status="02")
        print(ci)

    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serializers.StudentSerializer(student, many=True)
        # ///////////////////////////
        j = 0

        while j < len(serializer.data):
            # Select Givename
            if serializer.data[j]['name']:
                givename = serializer.data[j]['name']
                print(serializer.data[j]['name'])
            else:
                givename = 'None'
            # Select Middle_Name
            if serializer.data[j]['middle_name']:
                middle_name = serializer.data[j]['middle_name']
                print(serializer.data[j]['middle_name'])
            else:
                middle_name = 'None'
            # Select Last_Name
            if serializer.data[j]['last_name']:
                last_name = serializer.data[j]['last_name']
                print(serializer.data[j]['last_name'])
            else:
                last_name = 'None'

            # Select Country
            if serializer.data[j]['country']:
                if serializer.data[j]['country']['name']:
                    country = serializer.data[j]['country']['name']
                    print(serializer.data[j]['country']['name'])
                else:
                    country = 'None'
            else:
                country = 'None'

            # Select Student_type
            if serializer.data[j]['student_type']:
                if serializer.data[j]['student_type']['kind']:
                    student_type = serializer.data[j]['student_type']['kind']
                    print(serializer.data[j]['student_type']['kind'])
                else:
                    student_type = 'None'
            else:
                student_type = 'None'


            # Select Career
            if serializer.data[j]['career']:
                if serializer.data[j]['career']['national_career']:
                    if serializer.data[j]['career']['national_career']['name']:
                        career = serializer.data[j]['career']['national_career']['name']
                        print(serializer.data[j]['career']['national_career']['name'])
                    else:
                        career = 'None'
                else:
                    career = 'None'
            else:
                career = 'None'


            # Select Faculty
            if serializer.data[j]['faculty']:
                if serializer.data[j]['faculty']['name']:
                    faculty = serializer.data[j]['faculty']['name']
                    print(serializer.data[j]['faculty']['name'])
                else:
                    faculty = 'None'
            else:
                faculty = 'None'

            # Select Course_Type
            if serializer.data[j]['course_type']:
                if serializer.data[j]['course_type']['name']:
                    course_type = serializer.data[j]['course_type']['name']
                    print(serializer.data[j]['course_type']['name'])
                else:
                    course_type = 'None'
            else:
                course_type = 'None'

            # Select scholastic_origin
            if serializer.data[j]['scholastic_origin']:
                if serializer.data[j]['scholastic_origin']['name']:
                    cscholastic_origin = serializer.data[j]['scholastic_origin']['name']
                    print(serializer.data[j]['scholastic_origin']['name'])
                else:
                    cscholastic_origin = 'None'
            else:
                cscholastic_origin = 'None'

            # Select Town_university
            if serializer.data[j]['town_university']:
                if serializer.data[j]['town_university']['town']:
                    if serializer.data[j]['town_university']['town']['name']:
                        town_university = serializer.data[j]['town_university']['town']['name']
                        print(serializer.data[j]['town_university']['town']['name'])
                    else:
                        town_university = 'None'
                else:
                    town_university = 'None'
            else:
                town_university = 'None'

            # Select Matriculation_end_date
            if serializer.data[j]['faculty']:
                if serializer.data[j]['faculty']['university']:
                    if serializer.data[j]['faculty']['university']['matriculation_end_date']:
                        matriculation_end_date = serializer.data[j]['faculty']['university']['matriculation_end_date']
                        print(serializer.data[j]['faculty']['university']['matriculation_end_date'])
                    else:
                        matriculation_end_date = 'None'
                else:
                    matriculation_end_date = 'None'
            else:
                matriculation_end_date = 'None'

            # Select Rematriculation_end_date
            if serializer.data[j]['faculty']:
                if serializer.data[j]['faculty']['university']:
                    if serializer.data[j]['faculty']['university']['rematriculation_end_date']:
                        rematriculation_end_date = serializer.data[j]['faculty']['university']['rematriculation_end_date']
                        print(serializer.data[j]['faculty']['university']['rematriculation_end_date'])
                    else:
                        rematriculation_end_date = 'None'
                else:
                    rematriculation_end_date = 'None'
            else:
                rematriculation_end_date = 'None'

            ######################################
            id_student = serializer.data[j]['id_student']
            print('IDE STUDENT', id_student)

            groups2students = Groups2Students.objects.using("sigenu_student").filter(students_fk=id_student)
            serializer_group2student = serializers.Groups2StudentsSerializer(groups2students, many=True)
            print(len(serializer_group2student.data))
            k = 0
            groupm = 0
            while k < len(serializer_group2student.data):

                if serializer_group2student.data[k]['consecutive'] == 0:
                    print('instance student', serializer_group2student.data[k])
                    groupm = serializer_group2student.data[k]['groups_fk']
                k = k + 1
            xgroup = Xgroup.objects.using("sigenu_student").filter(id_group=groupm)
            serializer_xgroup = serializers.XgroupSerializer(xgroup, many=True)
            print('anno', serializer_xgroup.data[0]['year'])
            year = str(serializer_xgroup.data[0]['year'])

            ########################################

            hash = givename + middle_name + last_name + country + student_type + career + \
                   faculty + course_type + cscholastic_origin + town_university + matriculation_end_date + \
                   rematriculation_end_date + year



            hash_mod = hash.replace(" ", "")  # elimina los espacios de la cadena de caracteres
            print(hashlib.md5(hash_mod.encode("utf-8")).hexdigest())

            serializer.data[j]['hash_mod'] = hashlib.md5(hash_mod.encode("utf-8")).hexdigest()
            serializer.data[j]['year'] = year

            j = j + 1

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        pass



@csrf_exempt
def student_active_name_full(request, name):
    """Returns the active student given a Name"""
    # 92082643541
    try:
        # students = Student.objects.using("sigenu_student").filter(name__contains=str(name), student_status="02")
        a = str(name).split(' ')[1]
        print(a)
        students = Student.objects.using("sigenu_student").filter(name__contains=str(name), student_status="02")

    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serializers.StudentSerializerLinked(students, many=True)

        j = 0
        while j < len(serializer.data):
            id = serializer.data[j]['identification']
            serializer.data[j]['uri'] = str(
                request.build_absolute_uri().split('student_active_name_full')[0]) + "student_active_dni/" + id
            j = j + 1

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        pass



#import django_filters.rest_framework
#from django.contrib.auth.models import User
from sigenu.serializers import StudentSerializer
from rest_framework import generics
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ActivosList(generics.ListAPIView):
    # serializer_class = StudentSerializer
    serializer_class = serializers.StudentSerializerLinked
    queryset = Student.objects.using("sigenu_student").filter(student_status="02")
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'middle_name', 'last_name']

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     return Student.objects.using("sigenu_student").filter(student_status="02")


#
# class ProductList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     name = 'student-list'
#
#     filter_fields = (
#         'name',
#         'middle_name',
#     )